# This file save the data of active players which will be used to predict the total innings of the active players by test_innings.

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
            "to_predict/"+player_name, sheet_name="Test")
        self.scores = []
        self.innings = []
        self.ages = []
        self.count = 1
        self.age_num = []
        self.moving_avg = []
        self.year = []

    # this function opens the player excel file while and returns the following data in the form of list - 1. Age of Player at every inning, 2. Runs scored in every inning, 3. Number of Inning
    def file_open(self):
        try:
            while (True):
                self.yr = 0
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
                self.innings.append(int(self.dataframe1['Column2'][self.count]))
                if (str(self.dataframe1['Column3'][self.count]) not in ["nan","NaN","NAN","Nan"]):
                    self.year.append(int(str(self.dataframe1['Column3'][self.count])[-4:]))
                else:
                    self.year.append(self.year[-1])
        except:
            return (self.ages, self.scores, self.innings, self.year)
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

files = ["babar.xlsx", "bairstow.xlsx", "kane.xlsx", "karunaratne.xlsx", "markaram.xlsx", "mayers.xlsx", "rohit.xlsx", "root.xlsx", "smith.xlsx", "tamim.xlsx", "virat.xlsx", "warner.xlsx"]

id = 1
for i in files:
    yearly_average = []
    ret_age = 0
    deb_age = 0
    lon_gap = 0
    fiftees = 0
    in3 = 0
    tim_best_mov_avg = 0
    innings = 0
    tim_worst_mov_avg = 0
    tim_better_20 = 0
    try:
        main = Main(i)
    except:
        continue
    ag, sc, ini, years = main.file_open()
    innings = len(ini)
    if(innings < 20):
        continue
    year_counter = 0
    unique_years = np.unique(np.array(years))
    try:
        last_year = [unique_years[-1],unique_years[-2],unique_years[-3]]
        for j in range(len(ini)):
            if(years[j] in last_year):
                in3 += 1
    except:
        pass
    scores = []
    for k in sc:
        if(k>=50):
            fiftees += 1
    for i in sc:
        scores.append(i)
    fin_ag = main.age_list(ag)
    ma, xa = main.cal_mov_avg(sc, 10)
    ret_age = fin_ag[-1]
    deb_age = fin_ag[0]

    # predicted_innings will have the data of the active players which will we used to predict their final innings. This data will be copied to data_innings.
    
    add_data("predicted_innings.csv", [ret_age, deb_age, innings, sum(sc), fiftees, in3])
    #print([ret_age, deb_age, innings, sum(yearly_average)/len(yearly_average), sum(sc), fiftees])
    id += 1
