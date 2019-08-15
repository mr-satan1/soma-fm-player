import requests
import sys
from colorama import Fore, Back, Style
import json
import collections
import subprocess

url = "https://somafm.com/channels.json" 
fetchChannels = requests.get(url)
listChannels = fetchChannels.json()['channels']

channelDict = {'id': 'url'}
for channel in listChannels:
    channelID = channel['id']
    channelTitle = channel['title']
    channelURL = channel['playlists'][0]['url']
    channelDesc = channel['description']
    print(f"{Fore.BLUE}{channelTitle}{Fore.RESET} aka {Fore.RED}'{channelID}' {Fore.RESET} \t\n {Fore.GREEN}:::{Fore.RESET} {Fore.MAGENTA}{channelDesc}{Fore.RESET}")
    # Build ID:URL dict
    channelDict[channelID] = channelURL

## Get channel ID as input
try:
    chanInput = input("\nSelect Soma FM channel (ex: poptron): ")
    chanSelection = channelDict.get(chanInput)
    print(f"Playing {chanInput} on Soma FM!")
    # Enable stdout for debugging
    soma = subprocess.call(['mpv', chanSelection], stderr=subprocess.STDOUT, shell=False)
    # soma = subprocess.call(['mpv', chanSelection], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=False)
except:
    print(f"{Fore.RED} \nBYE!")
    sys.exit(1)