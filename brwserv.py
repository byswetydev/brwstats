#import time
# import logging
import sys
import os
# import datetime
import requests

from bs4 import BeautifulSoup
# from datetime import datetime,timezone

#ts = time.time()

#def makeLogs(logs):
#    if os.path.isfile("brwservAPI.log"):
#        with open("brwservAPI.log",'a') as f:
#            f.write(logs+"\n")
#            logging.warning(logs)
#    else:
#        with open("brwservAPI.log",'w') as f:
#            f.write(logs+"\n")
#            logging.warning(logs)

class brwAPI():

    def __init__(self):
        super().__init__()
        self.url = 'https://brwserv.net'
        self.stats = 'https://brwserv.net/profil/'
        self.stock = {}
        self.stock_rank = {}

    def __version__(self):
        return "1.1" # BrwServAPI version

    def getPseudo(self, name):
        name = name
        r_pseudo = requests.get(str(self.stats+name))
        if r_pseudo.ok:
            th = False
            soup_title = BeautifulSoup(r_pseudo.text, 'html.parser')
            title = soup_title.find('h1')
            if str(title) == "<h1>404 - Page introuvable</h1>":
                return th == True
            else:
                self.stock = {'name' : str(name)}
                return name
        else:
            #makeLogs("Impossible Requests")
            sys.exit(1)

    def getRank(self):
        r_rank = requests.get(str(self.stats+self.getPseudo(self.stock.get('name'))))
        if r_rank.ok:
            soup_rank = BeautifulSoup(r_rank.text , 'lxml')
            rank_r = soup_rank.select_one('span[class^="rank"]').text
            self.stock_rank = {'rank' : str(rank_r)}
            return rank_r
        else:
            #makeLogs("Impossible Requests")
            sys.exit(1)
    
    def getThePlayTime(self):
        r_time = requests.get(str(self.stats+self.getPseudo(self.stock.get('name'))))
        if r_time.ok:
            soup_time = BeautifulSoup(r_time.text, 'lxml')
            time_r = soup_time.select_one('h1[class^="total-game"]').text
            time_r = str(time_r).replace("Temps de jeu total ", "")
            return time_r
        else:
            #makeLogs("Impossible Requests")
            sys.exit(1)

    def getFirstTime(self):
        r_firsttime = requests.get(str(self.stats+self.getPseudo(self.stock.get('name'))))
        if r_firsttime.ok:
            soup_firsttime = BeautifulSoup(r_firsttime.text, 'lxml')
            firsttime_r = soup_firsttime.select_one('div[class^="info"]').text
            firsttime_r = str(firsttime_r).replace(self.stock_rank.get('rank'), "").replace(self.stock.get('name'), "")
            return firsttime_r
        else:
            #makeLogs("Impossible Requests")
            sys.exit(1)

    def getPracticeStats(self):
        r_practiceStats = requests.get(str(self.stats+self.getPseudo(self.stock.get('name'))))
        if r_practiceStats.ok:
            soup_practice = BeautifulSoup(r_practiceStats.text, 'lxml')
            practiceStats_r = soup_practice.select_one('div[class^="stat-div practice"]').text
            practiceStats_r = str(practiceStats_r)
            return practiceStats_r
        else:
            #makeLogs("Impossible Requests")
            sys.exit(1)

    def getRushFightStats(self):
        r_rushfightStats = requests.get(str(self.stats+self.getPseudo(self.stock.get('name'))))
        if r_rushfightStats.ok:
            soup_rushfight = BeautifulSoup(r_rushfightStats.text, 'lxml')
            rushfightStats_r = soup_rushfight.select_one('div[class^="stat-div rushfight"]').text
            rushfightStats_r = str(rushfightStats_r)
            return rushfightStats_r
        else:
            #makeLogs("Impossible Requests")
            sys.exit(1)

    def getFFARushStats(self):
        r_FFARushStats = requests.get(str(self.stats+self.getPseudo(self.stock.get('name'))))
        if r_FFARushStats.ok:
            soup_FFARushStats = BeautifulSoup(r_FFARushStats.text, 'lxml')
            FFARushStats_r = soup_FFARushStats.find_all('div', attrs={'class':'stat-div'})
            lines_rush = [title_Rush.get_text() for title_Rush in FFARushStats_r]
            for line_rush in lines_rush:
                if "ffarush" in str(line_rush).lower():
                    FFARushStats_r = str(line_rush)
                else:
                    continue
            return FFARushStats_r
        else:
            #makeLogs("Impossible Requests")
            sys.exit(1)

    def getBrainFFAStats(self):
        r_BrainFFAStats = requests.get(str(self.stats+self.getPseudo(self.stock.get('name'))))
        if r_BrainFFAStats.ok:
            soup_BrainFFAStats = BeautifulSoup(r_BrainFFAStats.text, 'lxml')
            BrainFFAStats_r = soup_BrainFFAStats.find_all('div', attrs={'class':'stat-div'})
            lines_brain = [title_brain.get_text() for title_brain in BrainFFAStats_r]
            for line_brain in lines_brain:
                if "brainffa" in str(line_brain).lower():
                    BrainFFAStats_r = str(line_brain)
                else:
                    continue
            return BrainFFAStats_r
        else:
            #makeLogs("Impossible Requests")
            sys.exit(1)

    def getBattleRoyalStats(self):
        r_BattleRoyalStats = requests.get(str(self.stats+self.getPseudo(self.stock.get('name'))))
        if r_BattleRoyalStats.ok:
            soup_BattleRoyalStats = BeautifulSoup(r_BattleRoyalStats.text, 'lxml')
            BattleRoyalStats_r = soup_BattleRoyalStats.find_all('div', attrs={'class':'stat-div'})
            lines_BattleRoyal = [title_BattleRoyal.get_text() for title_BattleRoyal in BattleRoyalStats_r]
            for line_BattleRoyal in lines_BattleRoyal:
                if "battleroyal" in str(line_BattleRoyal).lower():
                    BattleRoyalStats_r = str(line_BattleRoyal)
                else:
                    continue
            return BattleRoyalStats_r
        else:
            #makeLogs("Impossible Requests")
            sys.exit(1)

    def getPlagiatStats(self):
        r_PlagiatStats = requests.get(str(self.stats+self.getPseudo(self.stock.get('name'))))
        if r_PlagiatStats.ok:
            soup_PlagiatStats = BeautifulSoup(r_PlagiatStats.text, 'lxml')
            PlagiatStats_r = soup_PlagiatStats.find_all('div', attrs={'class':'stat-div'})
            lines_Plagiat = [title_Plagiat.get_text() for title_Plagiat in PlagiatStats_r]
            for line_Plagiat in lines_Plagiat:
                if "plagiat" in str(line_Plagiat).lower():
                    PlagiatStats_r = str(line_Plagiat)
                else:
                    continue
            return PlagiatStats_r
        else:
            #makeLogs("Impossible Requests")
            sys.exit(1)

    def banStatu(self):
        ban_statu = False
        r_ban = requests.get(str(self.stats+self.getPseudo(self.stock.get('name'))))
        if r_ban.ok:
            soup_ban = BeautifulSoup(r_ban.text, 'lxml')
            if soup_ban.find('div', {"class":'banned-div'}) is None:
                return ban_statu == True
            else:
                return ban_statu == False
        else:
            #makeLogs("Impossible Requests")
            sys.exit(1)
    
    def gameStatu(self):
        game_statu = False
        r_game = requests.get(str(self.stats+self.getPseudo(self.stock.get('name'))))
        if r_game.ok:
            soup_game = BeautifulSoup(r_game.text, 'lxml')
            if soup_game.find('div', {"class":'conneted on'}) is None:
                return game_statu == True
            else:
                return game_statu == False
        else:
            #makeLogs("Impossible Requests")
            sys.exit(1)
