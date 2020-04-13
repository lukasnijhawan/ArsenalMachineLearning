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

#add in big six status of opposition
BigSix = ['Tottenham','Liverpool','Man United','Man City','Chelsea']

for i in range(len(ArsenalGamesDF)):
    if ArsenalGamesDF.loc[i,'HomeTeam'] in BigSix or ArsenalGamesDF.loc[i,'AwayTeam'] in BigSix:
        ArsenalGamesDF.loc[i,'BigSix?'] = True
    else:
        ArsenalGamesDF.loc[i,'BigSix?'] = False


#add in the result
for i in range(len(ArsenalGamesDF)):
    if ArsenalGamesDF.loc[i,'HomeTeam'] == 'Arsenal':
        if ArsenalGamesDF.loc[i,'FTHG'] > ArsenalGamesDF.loc[i,'FTAG']:
            ArsenalGamesDF.loc[i,'Result'] = 'W'
        if ArsenalGamesDF.loc[i,'FTHG'] == ArsenalGamesDF.loc[i,'FTAG']:
            ArsenalGamesDF.loc[i,'Result'] = 'D'
        if ArsenalGamesDF.loc[i,'FTHG'] < ArsenalGamesDF.loc[i,'FTAG']:
            ArsenalGamesDF.loc[i,'Result'] = 'L'
    else:
        if ArsenalGamesDF.loc[i,'FTAG'] > ArsenalGamesDF.loc[i,'FTHG']:
            ArsenalGamesDF.loc[i,'Result'] = 'W'
        if ArsenalGamesDF.loc[i,'FTAG'] == ArsenalGamesDF.loc[i,'FTHG']:
            ArsenalGamesDF.loc[i,'Result'] = 'D'
        if ArsenalGamesDF.loc[i,'FTAG'] < ArsenalGamesDF.loc[i,'FTHG']:
            ArsenalGamesDF.loc[i,'Result'] = 'L'

#add in boolean for home team or not
for i in range(len(ArsenalGamesDF)):
    if ArsenalGamesDF.loc[i,'HomeTeam'] == 'Arsenal':
        ArsenalGamesDF.loc[i,'Home?'] = True
    else:
        ArsenalGamesDF.loc[i,'Home?'] = False

#now to try and implemenent some way to keep track of form. i'm thinking look back at the
#last five games and just create an integer of how many wins there are... not the best logic
#considering the starting and stopping of seasons but might be somewhat effective still.
#actually looking at it now im going to implement a method where a draw is worth .25 points at home, .5 away


#edit: also going to take into account big six status of other team.

for i in range(len(ArsenalGamesDF)):
    form = 0
    for j in range(1,6):
        try:
            if ArsenalGamesDF.loc[i-j,'Result'] == 'W':
                form += 1
            if ArsenalGamesDF.loc[i-j,'Result'] == 'D' and ArsenalGamesDF.loc[i-j,'Home?'] == True and ArsenallGamesDF.loc[i-j,'BigSix?'] == True:
                form += .4
            if ArsenalGamesDF.loc[i-j,'Result'] == 'D' and ArsenalGamesDF.loc[i-j,'Home?'] == False and ArsenalGamesDF.loc[i-j,'BigSix?'] == True:
                form += .7
            if ArsenalGamesDF.loc[i-j,'Result'] == 'D' and ArsenalGamesDF.loc[i-j,'Home?'] == True and ArsenalGamesDF.loc[i-j,'BigSix?'] == False:
                form += .25
            if ArsenalGamesDF.loc[i-j,'Result'] == 'D' and ArsenalGamesDF.loc[i-j,'Home?'] == False and ArsenalGamesDF.loc[i-j,'BigSix?'] == False:
                form += .5
        except:
            continue
    ArsenalGamesDF.loc[i,'Form'] = form


#ArsenalGamesDF.sort_values(by=['Date'], inplace=True, ascending=False)
print(ArsenalGamesDF.head())
print(ArsenalGamesDF.tail())
