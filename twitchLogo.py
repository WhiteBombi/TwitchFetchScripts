# Script Name        :  twitchLogo.py
# Author             :  WhiteBombo
# Created            :  August 4th 2017
# Last modified      :  August 7th 2017
# Version            :  1.1
# Description        :  Fetch a profile picture of a Twitch account.

import urllib.request, json, time
from PIL import Image
from cred import *

checkId()

searchName = str(input('Enter a username: '))
thumbnailSize = int(input('Enter final image size in pixels (64 by default): ') or 64)
pictureName = 'profile' + '.png'    # What would you like to call the picture file?

# Fetch info from the Kraken API
url = 'https://api.twitch.tv/kraken/users/{}?client_id={}'.format(searchName, client_id)
try:
    with urllib.request.urlopen(url) as f:
        response = f.read()
        decodedResponse = response.decode('utf-8')
    obj = json.loads(decodedResponse)

    # Save the picture from the logo url to a file.
    urllib.request.urlretrieve(obj['logo'], pictureName)

    # Make a thumbnail
    pic = Image.open(pictureName)
    pic.thumbnail((thumbnailSize, thumbnailSize))
    pic.save(pictureName, "PNG")

except:
    print(searchName.capitalize(), 'doesn\'t have a profile picture on Twitch.')
    exit()

# Exit
print('Profile picture for', obj['display_name'], 'has been fetched to profile.png.')
time.sleep(1)
