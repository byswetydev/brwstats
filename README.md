# brwstats
Python API for https://brwserv.net

With this API we can: get all the statistics of a player, ca registration date, if he is banned or not, his rank

I made a discord bot with this API. Link: https://discord.gg/gRWySJBKyq


----- REQUIREMENTS -----

import requests

from bs4 import BeautifulSoup

----- HOW TO USE -----

import brwserv

x = brwserv.brwAPI() # create instance

x.getPseudo("username") # load username

x.getRank() # get rank of player

x.getThePlayTime() # get player playing time

x.getFirstTime() # get the date of registration

x.getPracticeStats() # get practice stats

x.getRushFightStats() # get RushFight stats

x.getFFARushStats() # get ffarush stats

x.getBrainFFAStats() # get brainffa stats

x.getBattleRoyalStats() # get battleroyal stats

x.getPlagiatStats() # get plagiat stats

x.banStatu() # return True if player is ban, False if is not

in new version (1.1):

x.gameStatu() # get if player is online or not

# version of API: 1.1
