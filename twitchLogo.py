''' Fetch a profile picture of a Twitch account to the local directory.

Script Name        :  TwitchLogo.py
Author             :  WhiteBombo
Created            :  August 4th 2017
Last modified      :  August 12th 2017
Version            :  1.2
'''

import json
import time
import urllib.request
from PIL import Image
from Cred import CLIENT_ID, check_id

check_id()

SEARCHNAME = str(input('Enter a username: '))
THUMBNAILSIZE = int(input('Enter final image size in pixels (64 by default): ') or 64)
PICTURENAME = 'profile' + '.png'    # Set name of the picture file?

# Fetch info from the Kraken API
URL = 'https://api.twitch.tv/kraken/users/{}?client_id={}'.format(SEARCHNAME, CLIENT_ID)
try:
    with urllib.request.urlopen(URL) as f:
        RESPONSE = f.read()
        DECODEDRESPONSE = RESPONSE.decode('utf-8')
    OBJ = json.loads(DECODEDRESPONSE)

    # Save the picture from the logo URL to a file.
    urllib.request.urlretrieve(OBJ['logo'], PICTURENAME)

    # Make a thumbnail
    PIC = Image.open(PICTURENAME)
    PIC.thumbnail((THUMBNAILSIZE, THUMBNAILSIZE))
    PIC.save(PICTURENAME, "PNG")

except TypeError:
    print("{} doesn't have a profile picture on Twitch".format(SEARCHNAME.capitalize()))
    exit()

except urllib.error.HTTPError:
    print("The account '{}' couldn't be found.".format(SEARCHNAME.capitalize()))
    exit()

# Exit
time.sleep(1)
input('Profile picture for {} has been fetched to profile.png.'.format(OBJ['display_name']))
