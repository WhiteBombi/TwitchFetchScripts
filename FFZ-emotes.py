#! /usr/bin/env python3
'''
Description        :  Fetch FFZ-emotes of a Twitch channel and write the into a
                      file.
Script Name        :  FFZ-emotes.py
Author             :  Bombi(WhiteBombo)
Created            :  January 29th 2018
Last modified      :  January 29th 2018
Version            :  1.0
'''

import requests
import sys

ffz = "https://api.frankerfacez.com/v1/room/"

def getArgs():
    '''Get passed arguments. Channel name and line separation(n).'''
    try:
        channel = sys.argv[1]
    except:
        exit('Needs a channel name.')
    try:
        if sys.argv[2] == 'n':
            line = str('\n')
    except:
        line = ' '
    return channel, line

def getEmotes(channel, line, ffz):
    '''Get emotes from api.frankerfacez.com. Exit if no username or emotes.'''
    emotes = ''
    r = requests.get(ffz + channel)
    try:
        set = str(r.json()['room']['set']) # First get the emote set of the user
    except KeyError:
        exit('No such username.')
    for i in r.json()['sets'][set]['emoticons']: # Get the emotes with set
        emotes += i['name'] + line
    if len(emotes) == 0:
        exit('User has no FFZ-emotes.')
    return emotes

def write(emotes, channel, line):
    '''Write emotes on a file.'''
    file = 'ffzemotes-' + channel + '.txt'
    with open(file, 'w') as f:
        f.write(emotes)
    print(f'Emotes written to "{file}".')
    if line == '\n':
        print('Emotes separated by lines.')
    else:
        print('Emotes separated by spaces.')

# Run program
channel, line = getArgs()
emotes = getEmotes(channel, line, ffz)
write(emotes, channel, line)
