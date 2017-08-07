# TwitchFetchScripts
### [Download .zip](https://github.com/WhiteBombo/TwitchFetchScripts/archive/master.zip)

### [Get Python 3](https://www.python.org/downloads/)

### [Get Pillow](http://pillow.readthedocs.io/en/3.0.x/installation.html)

Python scripts aimed to be used by streamers and channel administrators to interact with several API's to fetch useful information.

## Requirements
Tested with Python 3.6.1. Needs [Python version 3](https://www.python.org/) or further. twitchLogo.py needs [Pillow](https://python-pillow.org).

## Twitch profile logo fetcher - twitchLogo.py
![Logo fetcher in action](docs/Logo.png)
#### V. 1.1
Added a thumbnail maker thing. Now uses [Pillow](https://python-pillow.org). Install instructions [here](http://pillow.readthedocs.io/en/3.0.x/installation.html).

#### V. 1.0
Fetches a Twitch user's logo from the [Kraken API](https://dev.twitch.tv/docs/) and saves it in the same directory with the script.

#### How to use
Run and follow instructions.

## Twitch ingest server list - twitchIngests.py
![Ingest script in action](docs/Ingest.png)
#### V. 1.1
Cleaned up the script of excess stuff and published Client-ID in 'cred.py' file.
#### V. 1.0
Currently only shows all the information of Twitch's ingest servers provided by the [Kraken API](https://dev.twitch.tv/docs/).

#### How to use
Just run.
