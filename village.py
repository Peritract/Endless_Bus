# This is a random generator for English village names.

from random import choice
from random import getrandbits

front_words = ['High','Low','North','South','East','West','Little','Great','Royal','Upper','Lower','Market']

back_words = ['Grange','Hill','Valley','Croft','Lake','Lakes','Park','Pond','Farm','Lodge','Manor','Town','Green','Hollow','Sands','Hollows', 'End','Row','Pike','Tor','Peak','Wall','Wood','Woods', 'Fell','Cross','Bridge','Heath','Moor','Bois','Wells']

suffixes = ['don','lee','ley','fell','ford','shire','sham','ish','ing','stow','ton','holt','cott','hurst','field','ham','ingham','stead','low','wick','cliffe','borough','wood','woods']

roots = ['Al','They','Asp','Ast','Had','Bing','Bland','Sea','Gar','Scar','Pock','Swin','Stam','Bar','Battle','Bead','Hock','Wych','Ban','Ret','Rom','Hul','Cot','Cots','Cote','Ips','Dean','Wheat','Camp','Cad']

def coinflip():
    return bool(getrandbits(1))

def construct_village():
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
