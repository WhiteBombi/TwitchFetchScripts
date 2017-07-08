# Script Name        :  twitchIngests.py
# Author             :  WhiteBombo
# Created            :  July 9th 2017
# Last modified      :
# Version            :  1.0
# Description        :  Show basic information of Twitch streaming ingest servers.

import urllib.request
import json
import textwrap
import time

# What information is being gathered
info = [
    '_id',
    'name',
    'availability',
    'url_template',
    'default'
    ]
# Input client_id or update if one exists
def newID():
    client_id = str(input('Input client_id: ')) or ''
    if client_id != '':
        if input('Are you sure you wish to replace your client_id? (y/n) ') == 'y':
            file = open("cred.py", "w")
            file.write("client_id = '" + client_id + "'")
            file.close()
newID()
from cred import *

try:
    if client_id == '':
        print('Missing client_id')
        exit()
except(NameError):
    print('Missing client_id')
    exit()

# Fetch data
url = 'https://api.twitch.tv/kraken/ingests?client_id=' + client_id
with urllib.request.urlopen(url) as f:
    response = f.read()
    decodedResponse = response.decode('utf-8')
    #print(textwrap.fill(decodedResponse, width= 50))

# Data structure magic
obj = json.loads(decodedResponse)
ingests = obj['ingests']

# Printing all the stuff
for ii in range(0, len(ingests)):
    ingest = ingests[ii]
    for iii in info:
        print(str(iii) + ': ' + str(ingest[iii]))
    print()

input('Press enter to exit.')
