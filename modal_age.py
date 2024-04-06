# This file will store the data required to predict the age into data_age.csv file

import csv
import math
import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import openpyxl


class Main():

    # this function defines variable which will be further used in the code
    def __init__(self, player_name):
        self.dataframe1 = pd.read_excel(
            "data/"+player_name, sheet_name="Test")
        self.scores = []
        self.innings = []
        self.ages = []
        self.count = 1
        self.age_num = []
        self.moving_avg = []

    # this function opens the player excel file while and returns the following data in the form of list - 1. Age of Player at every inning, 2. Runs scored in every inning, 3. Number of Inning
    def file_open(self):
        try:
            while (True):
                self.count += 1
                if self.dataframe1['Column7'][self.count][-1] == "*":
                    add = ''
                    for i in self.dataframe1['Column7'][self.count]:
                        if (i != "*"):
                            add += i
                elif (self.dataframe1['Column7'][self.count] == '-'):
                    continue
                else:
                    add = self.dataframe1['Column7'][self.count]
                if (str(self.dataframe1['Column18'][self.count]) != "nan"):
                    self.ages.append(self.dataframe1['Column18'][self.count])
                else:
                    self.ages.append(self.ages[-1])
                self.scores.append(float(add))
                self.innings.append(
                    int(self.dataframe1['Column2'][self.count]))
        except:
            return (self.ages, self.scores, self.innings)
            # pass

    # this function converts the age from "24 years 213 days" format to a float number which tells the age of player and returns the list of that age
    def age_list(self, ages_list):
        for i in ages_list:
            self.age = float(i[0]+i[1])
            if (i[11] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
                self.age += (float(i[9]+i[10]+i[11])/365)
            elif (i[10] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
                self.age += (float(i[9]+i[10])/365)
            else:
                self.age += (float(i[9])/365)
            self.age_num.append(self.age)
        return self.age_num

    # this function plots the graph between x and y values passed in the argument and name the axis as x_axis and y_axis
    def plot_graph(self, x, y, x_axis, y_axis):
        plt.plot(x, y)
        plt.xlabel(x_axis)
        plt.ylabel(y_axis)
        plt.title('My first graph!')
        plt.show()

    # this function calculates the moving average of the player by considering "ini" innings at a time and returns the list of moving average and one more list to plot at x-axis
    def cal_mov_avg(self, runs_scored, ini):
        self.for_x_axis = []
        for i in range(len(runs_scored)-ini):
            self.avg = 0
            for j in range(ini):
                self.avg += runs_scored[i+j]
            self.avg = self.avg/ini
            self.moving_avg.append(self.avg)
            self.for_x_axis.append(len(self.moving_avg))
        return (self.moving_avg, self.for_x_axis)

    # this function takes the list of age of the player at every inning and returns the list of gap between two consecutive innings in days
    def gap_innings(self, ini):
        ini_gap = []
        for i in range(len(ini)-1):
            ini_gap.append(round((ini[i+1]-ini[i])*365))
        return (ini_gap)


# *******************************************************************************

def add_data(filename, data):
    to_add = []
    with open(filename, mode='r')as csvfile:
        csvFile = csv.reader(csvfile)
        for lines in csvFile:
            to_add.append(lines)

    # data rows of csv file
    rows = [data]

    for i in rows:
        to_add.append(i)

    # writing to csv file
    with open(filename, 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the data rows
        for j in to_add:
            if (j == []):
                continue
            else:
                csvwriter.writerow(j)


files = ["AB de Villiers.xlsx", "abdur razzak.xlsx", "Adam Bacher.xlsx", "Adam Craig Gilchrist.xlsx", "Adrian Barath.xlsx", "aftab ahmed.xlsx", "Ajay Jadeja.xlsx", "Alaister Cook.xlsx", "Alexander Bell.xlsx", "Ali Bacher.xlsx", "Allan Donald.xlsx", "Allan R Border.xlsx", "alok kapali.xlsx", "Amit Mishra.xlsx", "Andrew Flintoff.xlsx", "Anil Kumble.xlsx", "aravinda de silva.xlsx", "Ashish Nehra.xlsx", "avishka gunawardene.xlsx", "Basil Butcher.xlsx", "Boeta Dippenaar.xlsx", "Bradley James Haddin.xlsx", "Carlton Baugh.xlsx", "Charles Athey.xlsx", "Claude Carter.xlsx", "Courtney Browne.xlsx", "CRD fernando.xlsx", "Curtly Ambrose.xlsx", "Daryll Cullinan.xlsx", "David C Boon.xlsx", "Devendra Bishoo.xlsx", "Eddie Barlow.xlsx", "Eldine Baptiste.xlsx", "Eoin Morgan.xlsx", "Geoff Boycott.xlsx", "George Camacho.xlsx", "Gerry Alexander.xlsx", "Gregory Stephen Chappell.xlsx", "habibul bashar.xlsx", "Hansie Cronje.xlsx", "Hashim Amla.xlsx", "Horace Cameron.xlsx", "Ian Bell.xlsx", "Ian Bishop.xlsx", "Ian Botham.xlsx", "Ian Michael Chappell.xlsx", "Ijaz Ahmed.xlsx", "Imran Khan.xlsx", "imrul kayes.xlsx", "Inshan ALi.xlsx", "Inzamam-ul-Haq.xlsx", "Irfan Pathan.xlsx", "Ivan Barrow.xlsx", "James Blanckenberg.xlsx", "James Christy.xlsx", "Javed Miandad.xlsx", "Jean Paul Duminy.xlsx", "Jimmy Adams.xlsx", "John Cheetham.xlsx", "John Commaille.xlsx", "Justin L Langer.xlsx", "Kapil Dev.xlsx", "Keith Arthurton.xlsx", "Keith Boyce.xlsx", "Ken Barrington.xlsx", "Kenneth Benjamin.xlsx", "Kenneth Bland.xlsx", "khaled mashud.xlsx", "khaled mehmud.xlsx",
         "Kimberley John Hughes.xlsx", "kumar dharmasena.xlsx", "Kyle Abbott.xlsx", "mahela jayawardene.xlsx", "Mark A Taylor.xlsx", "Mark Boucher.xlsx", "mashrafe mortaza.xlsx", "Matthew Lawrence Hayden.xlsx", "Michael Atherton.xlsx", "Michael Carew.xlsx", "Michael J Slater.xlsx", "Michael John Clarke.xlsx", "mohammad ashraful.xlsx", "Mohammad Kaif.xlsx", "mohammad rafique.xlsx", "Mohsin Khan.xlsx", "MS attapatu.xlsx", "Murli Karthik.xlsx", "Mushtaq Ahmed.xlsx", "nassir hossain.xlsx", "Neil Adcock.xlsx", "Nico Boje.xlsx", "Norman Cowans.xlsx", "nuwan kulasekara.xlsx", "Omari Banks.xlsx", "Paul Adams.xlsx", "Paul Collingwood.xlsx", "Pedro Collins.xlsx", "Praveen Kumar.xlsx", "Ramiz Raja.xlsx", "rangana herath.xlsx", "Rashid Latif.xlsx", "Ravi Bopara.xlsx", "Richard Ellison.xlsx", "Ricky Thomas Ponting.xlsx", "Robert Catteral.xlsx", "Robert Croft.xlsx", "romesh kaluwitharana.xlsx", "russel arnold.xlsx", "ruwan kalpage.xlsx", "Saeed Ajmal.xlsx", "Saleem Malik.xlsx", "sanath jayasuriya.xlsx", "sangarangen anurag.xlsx", "Sanjay Manjrekar.xlsx", "Shahid Afridi.xlsx", "Sheik Bacchus.xlsx", "Sherwin Campbell.xlsx", "Shivnarine Chanderpaul.xlsx", "Shoaib Akhtar.xlsx", "Simon Mathew Katich.xlsx", "Stephen Cook.xlsx", "Stephen Rodger Waugh.xlsx", "Steven Finn.xlsx", "Sulieman Benn.xlsx", "Suresh Raina.xlsx", "tillakaratne dilshan.xlsx", "Tino Best.xlsx", "Umar Gul.xlsx", "upul chandana.xlsx", "Virendra Sehwag.xlsx", "VVS Laxman.xlsx", "Wasim Akram.xlsx", "Winston Benjamin.xlsx", "Younis Khan.xlsx", "Yuvraj Singh.xlsx", "Zaheer Khan.xlsx"]
id = 1
for i in files:
    top20 = [0 for j in range(20)]
    name = i[:-5]
    ret_age = 0
    deb_age = 0
    lon_gap = 0
    tim_best_mov_avg = 0
    innings = 0
    tim_worst_mov_avg = 0
    tim_better_20 = 0
    try:
        main = Main(i)
    except:
        continue
    ag, sc, ini = main.file_open()
    innings = len(ini)
    if (innings <= 20):
        continue

    scores = []
    fiftees = 0
    for k in sc:
        if (k >= 50):
            fiftees += 1
    for i in sc:
        scores.append(i)
    fin_ag = main.age_list(ag)
    ma, xa = main.cal_mov_avg(sc, 10)
    ret_age = fin_ag[-1]
    deb_age = fin_ag[0]
    for k in range(20):
        top20.append(max(sc))
        sc.remove(max(sc))
    avg_top_score = sum(top20)/20
    for j in range(0, len(scores)):
        if (scores[j] >= avg_top_score):
            tim_better_20 = (j+1)/innings
    if(sum(sc) > 400):
        add_data("data_age.csv", [ret_age, deb_age, innings, sum(sc), fiftees])
    id += 1
