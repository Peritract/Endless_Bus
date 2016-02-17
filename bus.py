# A whole bunch of import statements.

from random import choice
from random import getrandbits
from random import randint
from time import gmtime, strftime, sleep

import os
import tweepy

import village

C_KEY = os.environ['C_KEY']
C_SECRET = os.environ['C_SECRET']
A_TOKEN = os.environ['A_TOKEN']
A_TOKEN_SECRET = os.environ['A_TOKEN_SECRET']

# The following a lists of sentence starters for the generator:

location_sentences = ['The next stop is','Now approaching','The next stop will be','We will shortly be arriving at']

reminder_sentences = ['Passengers are reminded']

reminders = ['that exact change is preferred','that tickets are only valid on the day of issue','that children under five travel free','that eating is not permitted on this service','that rubbish bins are provided on board this service','that the first three seats are reserved for disabled passengers']

excuses = ['heavy rainfall','inclement weather','snowfall','black ice','fallen leaves','a traffic incident','union action','roadworks']

thanks_sentences = ['Thank you for travelling on this service to', 'We appreciate your patience on this late-running service to']

# The next several functions actually generate the tweets.

def construct_location_tweet():
    # Creates a sentence for the bot to post, about a location.
    place = village.construct_village()
    sentence = choice(location_sentences)

    chance = randint(0,20)
    if chance >=15 and not ("approaching" in sentence):
        time = randint(2,55)
        time = str(time)
        text = sentence + " " + place + ", in approximately " + time + " minutes."
    else:
        text = sentence + " " + place +"."
    return text

def construct_thanks_tweet():
    # Creates a sentence for the bot to post, thanking passengers.
    place = village.construct_village()
    sentence = choice(thanks_sentences)
    text = sentence + " " + place + "."
    return text

def construct_reminder_tweet():
    # Creates a sentence for the bot to post, reminding passengers.
    sentence = choice(reminder_sentences)
    reminder = choice(reminders)
    text = sentence + " " + reminder + "."
    return text

def construct_excuse_tweet():
    # Creates a sentence for the bot to post, making an excuse for lateness.
    place = village.construct_village()
    excuse = choice(excuses)
    excuse_place = village.construct_village()
    text = "This service to " + place + " is delayed due to "
    text = text + excuse + " in the " + excuse_place + " area."
    return text

def construct_tweet():
    #Chooses from different kinds of tweet, generates a tweet, and checks it is short enough.
    length = 141
    tweet = " "
    while length >140:
        chance = randint(0,99)
        if chance < 50:
            tweet = construct_location_tweet()
        elif chance <80:
            tweet = construct_excuse_tweet()
        elif chance <95:
            tweet = construct_thanks_tweet()
        elif chance <100:
            tweet = construct_reminder_tweet()
        length = len(tweet)
    return tweet

# A function to log things, when needed.

# Twitter stuff, that I don't fully understand. Basically, Twitter needs passwords to let the bot do stuff, these functions/variables provide them. Then it posts the tweet. If the tweet doesn't work, it throws an error instead. Currently, none of this gets logged, because I can't work out how.

def tweet(text):
    auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
    auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
    api = tweepy.API(auth)

    # Send the tweet.
    api.update_status(text)

#Actually does stuff.
if __name__ == "__main__":
    message = construct_tweet()
    tweet(message)
    sleep(1800)

