import json
import numpy as np
import pandas as pd
from pprint import pprint

#first, load the data in. (from previous 4 seasons)
with open('2018_19seasondata.json') as f:
  data4 = json.load(f)


with open('2017_18seasondata.json') as f:
    data3 = json.load(f)

with open('2016_17seasondata.json') as f:
    data2 = json.load(f)

with open('2015_16seasondata.json') as f:
    data1 = json.load(f)


#lets get a list of just all the arsenal games.

arsenal_games = []

for game in data1:
    if game['HomeTeam'] == 'Arsenal' or game['AwayTeam'] == 'Arsenal':
        arsenal_games.append(game)
for game in data2:
    if game['HomeTeam'] == 'Arsenal' or game['AwayTeam'] == 'Arsenal':
        arsenal_games.append(game)
for game in data3:
    if game['HomeTeam'] == 'Arsenal' or game['AwayTeam'] == 'Arsenal':
        arsenal_games.append(game)
for game in data4:
    if game['HomeTeam'] == 'Arsenal' or game['AwayTeam'] == 'Arsenal':
        arsenal_games.append(game)


#the columns we are focused on are hometeam, awayteam, scores, halftime scores (for fun- will c),referee.. will manually create form tables and whatnot later.

ArsenalGamesDF = pd.DataFrame(arsenal_games)
ArsenalGamesDF = ArsenalGamesDF[['Date','HomeTeam','AwayTeam','HTHG','HTAG','FTHG','FTAG','Referee']]
print(ArsenalGamesDF.head())
