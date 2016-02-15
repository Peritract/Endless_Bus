from random import choice
from random import getrandbits
from random import randint

front_words = ['High','Low','North','South','East','West','Little','Great','Royal','Upper','Lower']

back_words = ['Grange','Hill','Valley','Croft','Lake','Lakes','Park','Pond','Farm','Lodge','Manor','Town','Green','Hollow','Sands','Hollows', 'End','Row','Pike','Tor','Peak','Wall', 'Fell','Cross','Bridge','Heath','Moor','Bois']

suffixes = ['don','lee','ley','fell','ford','shire','sham','ish','ing','stow','ton','holt','cott','hurst','field','ham','ingham','stead','low','wick','cliffe','borough']

roots = ['Al','They','Asp','Ast','Had','Bing','Bland','Sea','Gar','Scar','Pock','Swin','Stam','Bar','Battle','Bead','Hock']

location_sentences = ['The next stop is','Now approaching','The next stop will be','We will shortly be arriving at']

reminder_sentences = ['Passengers are reminded']

reminders = ['that exact change is preferred','that tickets are only valid on the day of issue','that children under five travel free','that eating is not permitted on this service','that rubbish bins are provided for your convenience','that the first three seats are reserved for disabled passengers']

excuses = ['heavy rainfall','inclement weather','snowfall','black ice','fallen leaves','a traffic incident','union action','roadworks']

thanks_sentences = ['Thank you for travelling on this service to', 'We appreciate your patience on this late-running service to']

def coinflip():
    return bool(getrandbits(1))

def construct_place():
    front_word = 0
    back_word = 0
    root = choice(roots)
    suffix = choice(suffixes)
    flip = coinflip()
    if flip:
        front_word = choice(front_words)
    flip = coinflip()
    if flip:
        back_word = choice(back_words)
    text = root+suffix
    if front_word:
        text = front_word + " " + text
    if back_word:
        text = text + " " + back_word
    return text

def construct_location_tweet():
    place = construct_place()
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
    place = construct_place()
    sentence = choice(thanks_sentences)
    text = sentence + " " + place + "."
    return text

def construct_reminder_tweet():
    sentence = choice(reminder_sentences)
    reminder = choice(reminders)
    text = sentence + " " + reminder + "."
    return text

def construct_excuse_tweet():
    place = construct_place()
    excuse = choice(excuses)
    excuse_place = construct_place()
    text = "This service to " + place + " is delayed due to "
    text = text + excuse + " in the " + excuse_place + " area."
    return text

def construct_tweet():
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

for x in range(0,30):
   print construct_tweet()
