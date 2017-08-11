''' Fetch basic information of Twitch streaming ingest servers.

Script Name        :  TwitchIngests.py
Author             :  WhiteBombo
Created            :  July 9th 2017
Last modified      :  August 12th 2017
Version            :  1.2
'''

import json
import time
import urllib.request
from Cred import CLIENT_ID, check_id

check_id()

# What information is being gathered
INFO = [
    '_id',
    'name',
    'availability',
    'url_template',
    'default'
    ]

# Fetch data
URL = 'https://api.twitch.tv/kraken/ingests?client_id=' + CLIENT_ID
with urllib.request.urlopen(URL) as f:
    RESPONSE = f.read()
    DECODEDRESPONSE = RESPONSE.decode('utf-8')

# Data structure magic
OBJ = json.loads(DECODEDRESPONSE)
INGESTS = OBJ['ingests']

# Printing all the stuff
for ii in range(0, len(INGESTS)):
    INGESTS = INGESTS[ii]
    for iii in INFO:
        print(str(iii) + ': ' + str(INGESTS[iii]))
    print()

time.sleep(1)
input('Press enter to exit.')
