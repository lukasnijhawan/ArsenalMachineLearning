import requests
import json
import pandas as pd
from pprint import pprint

def createdataframe():
    #get a dictionary that matches teams with teamid
    teamdict = {}
    teams = requests.get('https://fantasy.premierleague.com/drf/teams')
    teams = teams.json()
    for team in teams:
        teamdict[team['code']] = team['name']


    #element type for positions
    elementdict = {1:'Goalkeeper',2:'Defender',3:'Midfielder',4:'Forward'}

    #start by loading the data i want into a dataframe for each player
    playerdata = pd.DataFrame(columns = ['id','Team','Current Form','Position'])
    #start by getting the names of each of the players matched up with their ids, adding them to new dictionary
    playersdict = {}
    players = requests.get('https://fantasy.premierleague.com/drf/bootstrap-static')
    players = players.json()
    for player in players['elements']:
        playersdict[player['first_name']+' '+player['second_name']] = player['id']
        playerdata.loc[player['first_name']+' '+player['second_name']] = [player['id'],teamdict[player['team_code']],player['form'],elementdict[player['element_type']]]


    return playerdata

def getpastdata(name, playersdataframe, stat):
    import matplotlib.pyplot as plt
    playerid = playersdataframe.loc[name][0]
    urlrequest = requests.get('https://fantasy.premierleague.com/drf/element-summary/{}'.format(playerid))
    historicaldata = urlrequest.json()
    historydataframe = pd.DataFrame(columns = ['Yellow Cards','Red Cards','Goals Scored','Goals Conceded','Total Minutes','Cleansheets','Saves','Assists'])


    for season in historicaldata['history_past']:
        if season['minutes'] != 0:
            historydataframe.loc[season['season_name']] = [90*season['yellow_cards']/season['minutes'],90*season['red_cards']/season['minutes'],90*season['goals_scored']/season['minutes'],90*season['goals_conceded']/season['minutes'],season['minutes'],season['clean_sheets'],90*season['saves']/season['minutes'],90*season['assists']/season['minutes']]
    if stat == 'Total Minutes' or stat == 'Cleansheets':
        plt.plot(historydataframe['{}'.format(stat)],marker = 'o')
        plt.title('{} by Season'.format(stat))
        plt.grid(True)
        plt.xlabel('Season')
        plt.ylabel('Number of {}'.format(stat))
        plt.show()
    else:
        plt.plot(historydataframe['{}'.format(stat)],marker = 'o')
        plt.title('{} per 90 Minutes by Season'.format(stat))
        plt.grid(True)
        plt.xlabel('Season')
        plt.ylabel('Number of {}'.format(stat))
        plt.show()

def compareplayers(player1, player2, playersdataframe, stat):
    import matplotlib.pyplot as plt
    player1id = playersdataframe.loc[player1][0]
    player2id = playersdataframe.loc[player2][0]
    player1data = requests.get('https://fantasy.premierleague.com/drf/element-summary/{}'.format(player1id))
    player2data = requests.get('https://fantasy.premierleague.com/drf/element-summary/{}'.format(player2id))
    player1data = player1data.json()
    player2data = player2data.json()
    player1dataframe = pd.DataFrame(columns = ['Yellow Cards','Red Cards','Goals Scored','Goals Conceded','Total Minutes','Cleansheets','Saves','Assists'])
    player2dataframe = pd.DataFrame(columns = ['Yellow Cards','Red Cards','Goals Scored','Goals Conceded','Total Minutes','Cleansheets','Saves','Assists'])

    for season1 in player1data['history_past']:
        for season2 in player2data['history_past']:
            if season1['season_name'] == season2['season_name']:
                if season1['minutes'] != 0 and season2['minutes'] != 0:
                    player1dataframe.loc[season1['season_name']] = [90*season1['yellow_cards']/season1['minutes'],90*season1['red_cards']/season1['minutes'],90*season1['goals_scored']/season1['minutes'],90*season1['goals_conceded']/season1['minutes'],season1['minutes'],season1['clean_sheets'],90*season1['saves']/season1['minutes'],90*season1['assists']/season1['minutes']]
                    player2dataframe.loc[season2['season_name']] = [90*season2['yellow_cards']/season2['minutes'],90*season2['red_cards']/season2['minutes'],90*season2['goals_scored']/season2['minutes'],90*season2['goals_conceded']/season2['minutes'],season2['minutes'],season2['clean_sheets'],90*season2['saves']/season2['minutes'],90*season2['assists']/season2['minutes']]

    if stat == 'Total Minutes' or stat == 'Cleansheets':
        plt.plot(player1dataframe['{}'.format(stat)],marker = 'o', label = '{}'.format(player1))
        plt.plot(player2dataframe['{}'.format(stat)],marker = 'o', label = '{}'.format(player2))
        plt.title('{} by Season'.format(stat))
        plt.grid(True)
        plt.xlabel('Season')
        plt.ylabel('Number of {}'.format(stat))
        plt.legend()
        plt.show()
    else:
        plt.plot(player1dataframe['{}'.format(stat)],marker = 'o', label = '{}'.format(player1))
        plt.plot(player2dataframe['{}'.format(stat)],marker = 'o', label = '{}'.format(player2))
        plt.title('{} per 90 Minutes by Season'.format(stat))
        plt.grid(True)
        plt.xlabel('Season')
        plt.ylabel('Number of {}'.format(stat))
        plt.legend()
        plt.show()
