# Script Name        :  twitchIngests.py
# Author             :  WhiteBombo
# Created            :  July 9th 2017
# Last modified      :  August 4th 2017
# Version            :  1.1
# Description        :  Show basic information of Twitch streaming ingest servers.

import urllib.request, json, time
from cred import *

checkId()

# What information is being gathered
info = [
    '_id',
    'name',
    'availability',
    'url_template',
    'default'
    ]

# Fetch data
url = 'https://api.twitch.tv/kraken/ingests?client_id=' + client_id
with urllib.request.urlopen(url) as f:
    response = f.read()
    decodedResponse = response.decode('utf-8')

# Data structure magic
obj = json.loads(decodedResponse)
ingests = obj['ingests']

# Printing all the stuff
for ii in range(0, len(ingests)):
    ingest = ingests[ii]
    for iii in info:
        print(str(iii) + ': ' + str(ingest[iii]))
    print()

time.sleep(1)
input('Press enter to exit.')
