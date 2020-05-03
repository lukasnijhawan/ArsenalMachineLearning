from tkinter import *
import datetime
import subprocess as sub
from PIL import Image, ImageTk
from makedataframe import createdataframe
from makedataframe import getpastdata
from makedataframe import compareplayers



currentplayerdata = createdataframe()
PLAYERS = list(currentplayerdata.index.values)
class GUI:
    def __init__(self, master):
        self.master = master
        master.title("English Premier League Stats Application")
        #add title
        self.title = Label(master,height = 1, width = 50,text = 'Welcome to the Premier League Stats Application!')
        self.title.grid(row = 0, column = 1)
        self.title.config(font = ("Courier",20))
        #add premier league logo beneath name
        path = 'pllogo.jpeg'
        image1 = Image.open(path)
        image1 = image1.resize((100,100), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(image1)
        self.logo = Label(master, image = img, height = 100, width = 100)
        self.logo.grid(row = 1, column = 2)
        self.logo.image = img
        #put name in top right
        self.nameframe = Frame(master, height = 5, width = 10,bd = 2, relief = 'ridge')
        self.nameframe.grid(row = 0, column = 2)
        self.name = Label(self.nameframe, text = 'Created by Lukas Nijhawan')
        self.name.grid(row = 0,columnspan = 3)
        self.name.config(font = 'Courier')

        #put date in top left
        self.dateframe = Frame(master, height = 5, width = 10, bd = 2, relief = 'ridge',padx = 20)
        self.dateframe.grid(row = 0, column = 0)
        self.date = Label(self.dateframe, text = datetime.date.today())
        self.date.grid(row = 0, column = 0,columnspan = 3)
        self.date.config(font ='Courier')

        self.variable = StringVar(master)
        self.variable.set('Select Player')

        #make frame/buttons/entry to enter a player's name and get different data
        self.inputframe = Frame(master, bd = 2, relief = 'ridge')
        self.inputframe.grid(row = 1, column = 1)
        self.frame2 = Frame(self.inputframe, bd = 2, relief = 'ridge')
        self.frame2.grid(row = 0, column = 0, columnspan = 2)
        self.enterplayername = OptionMenu(self.frame2, self.variable, *PLAYERS)
        self.enterplayername.grid(row = 0, column = 1)
        self.playernamelabel = Label(self.frame2, text = 'Enter the player name:', height = 1, width = 20)
        self.playernamelabel.grid(row = 0, column = 0)
        self.historiclabel = Label(self.inputframe, text = 'Click buttons below to get data from past seasons:', pady = 20,height =1, width = 36)
        self.historiclabel.grid(row = 3, column = 0, columnspan = 2)
        self.yellowcards = Button(self.inputframe, text = 'Yellow Card Data', height = 1, width = 15, command = self.yellowcards)
        self.yellowcards.grid(row = 4, column = 0)
        self.redcards = Button(self.inputframe, text = 'Red Card Data', height =1, width =10, command =self.redcards)
        self.redcards.grid(row = 4, column = 1)
        self.goals = Button(self.inputframe, text = 'Goals Scored', height =1, width = 10, command = self.goalsscored)
        self.goals.grid(row = 5, column = 0)
        self.assists = Button(self.inputframe, text = 'Assists', height = 1, width = 10, command = self.totalassists)
        self.assists.grid(row = 5, column = 1)
        self.saves = Button(self.inputframe, text = 'Saves (Goalkeepers Only)',height = 1, width = 20, command = self.totalsaves)
        self.saves.grid(row = 6, column = 0)
        self.cleansheets = Button(self.inputframe, text = 'Cleansheets', height = 1, width = 10, command = self.totalcleansheets)
        self.cleansheets.grid(row = 6, column = 1)
        self.totalminutes = Button(self.inputframe, text = 'Total Minutes', height = 1, width = 10, command = self.totalminutesplayed)
        self.totalminutes.grid(row =7, column = 0)
        self.teamgoalsconceded = Button(self.inputframe, text = 'Goals Conceded', height = 1, width = 15, command = self.goalsconceded)
        self.teamgoalsconceded.grid(row =7, column = 1)

        #add frame to put graphs in (eventually)
        # self.graphframe = Canvas(master, width = 300, height = 300)
        # self.graphframe.grid(row = 7, column = 0, columnspan = 3)

        #add place to put current data/information about the player
        self.infoframe = Frame(self.inputframe, bd = 2, relief = 'ridge')
        self.infoframe.grid(row = 1, column = 0,columnspan =2)

        self.currentbutton = Button(self.infoframe, text = 'Press Here to get Current Player Data', command = self.getcurrentdata)
        self.currentbutton.grid(row = 0, column =0)

        #add place to display current data (on left hand side of UI)
        self.currentframe = Frame(master, bd = 2, relief = 'ridge')
        self.currentframe.grid(row = 1, column = 0)

        self.playerposition = Label(self.currentframe, text = 'Player Position:')
        self.playerposition.grid(row = 0,column =0)
        self.team = Label(self.currentframe, text = 'Team:')
        self.team.grid(row = 1,column =0)
        self.currentform = Label(self.currentframe, text = 'Current Form:')
        self.currentform.grid(row = 2, column =0)



        # inititalize two more variables
        self.variable2 = StringVar(master)
        self.variable2.set('Select First Player')
        self.variable3 = StringVar(master)
        self.variable3.set('Select Second Player')
        #make place to compare players
        self.letscompareplayers = Label(master, text = 'Compare Players Below')
        self.letscompareplayers.grid(row = 2, column = 1)
        self.letscompareplayers.config(font = ("Courier",15))
        self.compareplayersframe = Frame(master, bd = 2, relief = 'ridge')
        self.compareplayersframe.grid(row = 3, column = 1)
        self.compareframe1 = Frame(self.compareplayersframe, bd = 2, relief = 'ridge')
        self.compareframe1.grid(row = 0, column = 0, columnspan = 2)
        self.enterplayer1name = OptionMenu(self.compareframe1, self.variable2, *PLAYERS)
        self.enterplayer1name.grid(row = 0, column = 1)
        self.enterplayer2name = OptionMenu(self.compareframe1, self.variable3, *PLAYERS)
        self.enterplayer2name.grid(row = 1, column = 1)
        self.player1namelabel = Label(self.compareframe1, text = 'Enter the first player name:', height = 1, width = 20)
        self.player1namelabel.grid(row = 0, column = 0)
        self.player2namelabel = Label(self.compareframe1, text = 'Enter the second player name', height = 1, width = 25)
        self.player2namelabel.grid(row = 1, column =0)
        self.historiclabel2 = Label(self.compareplayersframe, text = 'Click buttons below to get data from past seasons:', pady = 20,height =1, width = 36)
        self.historiclabel2.grid(row = 3, column = 0, columnspan = 2)
        self.yellowcards2 = Button(self.compareplayersframe, text = 'Yellow Card Data', height = 1, width = 15, command = self.compareyellowcards)
        self.yellowcards2.grid(row = 4, column = 0)
        self.redcards2 = Button(self.compareplayersframe, text = 'Red Card Data', height =1, width =10, command =self.compareredcards)
        self.redcards2.grid(row = 4, column = 1)
        self.goals2 = Button(self.compareplayersframe, text = 'Goals Scored', height =1, width = 10, command = self.comparegoalsscored)
        self.goals2.grid(row = 5, column = 0)
        self.assists2 = Button(self.compareplayersframe, text = 'Assists', height = 1, width = 10, command = self.comparetotalassists)
        self.assists2.grid(row = 5, column = 1)
        self.saves2 = Button(self.compareplayersframe, text = 'Saves (Goalkeepers Only)',height = 1, width = 20, command = self.comparetotalsaves)
        self.saves2.grid(row = 6, column = 0)
        self.cleansheets2 = Button(self.compareplayersframe, text = 'Cleansheets', height = 1, width = 10, command = self.comparecleansheets)
        self.cleansheets2.grid(row = 6, column = 1)
        self.totalminutes2 = Button(self.compareplayersframe, text = 'Total Minutes', height = 1, width = 10, command = self.comparetotalminutesplayed)
        self.totalminutes2.grid(row =7, column = 0)
        self.teamgoalsconceded2 = Button(self.compareplayersframe, text = 'Goals Conceded', height = 1, width = 15, command = self.comparegoalsconceded)
        self.teamgoalsconceded2.grid(row =7, column = 1)


        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.grid(row = 4, column = 1)

    def yellowcards(self):
        playername = self.variable.get()
        getpastdata(playername, currentplayerdata,'Yellow Cards')
    def redcards(self):
        playername = self.variable.get()
        getpastdata(playername,currentplayerdata, 'Red Cards')
    def totalminutesplayed(self):
        playername = self.variable.get()
        getpastdata(playername, currentplayerdata, 'Total Minutes')
    def goalsscored(self):
        playername = self.variable.get()
        getpastdata(playername, currentplayerdata, 'Goals Scored')
    def goalsconceded(self):
        playername = self.variable.get()
        getpastdata(playername, currentplayerdata, 'Goals Conceded')
    def totalsaves(self):
        playername = self.variable.get()
        getpastdata(playername, currentplayerdata, 'Saves')
    def totalcleansheets(self):
        playername = self.variable.get()
        getpastdata(playername, currentplayerdata, 'Cleansheets')
    def totalassists(self):
        playername = self.variable.get()
        getpastdata(playername, currentplayerdata, 'Assists')

    def getcurrentdata(self):

        playername = self.variable.get()
        try:
            self.playerposition.config(text = 'Player Position: {}'.format(currentplayerdata.loc[playername][3]))
            self.currentform.config(text = 'Current Form: {}'.format(currentplayerdata.loc[playername][2]))
            self.team.config(text = 'Team: {}'.format(currentplayerdata.loc[playername][1]))
        except:
            self.playerposition.config(text = 'Player Position: Player Not Found')
            self.currentform.config(text = 'Current Form: Player Not Found')
            self.team.config(text = 'Team: Player Not Found')

    def compareyellowcards(self):
        player1 = self.variable2.get()
        player2 = self.variable3.get()
        compareplayers(player1, player2, currentplayerdata, 'Yellow Cards')
    def compareredcards(self):
        player1 = self.variable2.get()
        player2 = self.variable3.get()
        compareplayers(player1, player2, currentplayerdata, 'Red Cards')
    def comparetotalminutesplayed(self):
        player1 = self.variable2.get()
        player2 = self.variable3.get()
        compareplayers(player1, player2, currentplayerdata, 'Total Minutes')
    def comparegoalsscored(self):
        player1 = self.variable2.get()
        player2 = self.variable3.get()
        compareplayers(player1, player2, currentplayerdata, 'Goals Scored')
    def comparegoalsconceded(self):
        player1 = self.variable2.get()
        player2 = self.variable3.get()
        compareplayers(player1, player2, currentplayerdata, 'Goals Conceded')
    def comparetotalsaves(self):
        player1 = self.variable2.get()
        player2 = self.variable3.get()
        compareplayers(player1, player2, currentplayerdata, 'Saves')
    def comparecleansheets(self):
        player1 = self.variable2.get()
        player2 = self.variable3.get()
        compareplayers(player1, player2, currentplayerdata, 'Cleansheets')
    def comparetotalassists(self):
        player1 = self.variable2.get()
        player2 = self.variable3.get()
        compareplayers(player1, player2, currentplayerdata, 'Assists')



root = Tk()

root.configure(background = 'grey20')
root.resizable(False, False)
my_gui = GUI(root)
root.mainloop()
