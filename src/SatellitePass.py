import requests
import json
import sqlite3;
import pandas as pd
import ephem # USE THIS in terminal TO IMPORT EPHEM python -m pip install ephem

class Station (object):

    def __init__(self, sLat, sLong, sAlt, station_id):
        self.sAlt = sAlt
        self.sLat = sLat
        self.sLong = sLong
        self.station_id = station_id
        self.SNCbal = 100

class Pass (object):

    def __init__(self, ID, AOSt, LOSt, AOSd, TCAd, LOSd, Sperc):
       self.ID = ID
       self.AOSt = AOSt
       self.AOSd = AOSd
       self.TCAd = TCAd
       self.LOSt = LOSt
       self.LOSd = LOSd
       self.Sperc = Sperc

# Functions
def Schedule(List, StartT, EndT): #function to schedule the given Pass List in the allowed time period
    SchedList = []
    SchedNum = 0
    CurrSat = List[0]

    #THIS IS WHERE THE PRIORITIES OF THE STATION OWNER IS INPUTTED
    #(this example is only prioritizing success rate)

    for x in range(1,len(List)):
        CompSat = List[x]
        if CompSat.Sperc > CurrSat.Sperc:
            CurrSat = CompSat

    print('After considering', len(List), 'sattelites, scheduling pass of sattelite ID(s): ', CurrSat.ID)
    #print('After considering', len(List), 'sattelites, scheduling pass of sattelite ID(s): ', len(SchedList))
    return

def GetPasses(Station, StartT, EndT, minimum_altitude, min_pass_duration):
    a = 0
    return


################
## MAIN
################

#Set up Stations and Passes


sats = sqlite3.connect("C:\\Users\\Yogif\\OneDrive\\Desktop\\Homework\\CS 358\\satdata\\passes.sqlite\\passes.sqlite")

sc = sats.cursor()
#print(sc.execute('SELECT name FROM sqlite_schema WHERE type=\'table\' AND name NOT LIKE \'sqlite_%\';'))

for row in sc.execute('SELECT * FROM passes;'):
    print(row)

#print(df.head())

S1 = Station(41.462,-87.038,240,834) #VALPO STATION INFO EXAMPLE
P1 = Pass(99477, 414, 425, 203, 17, 331, 56.48) #example pass from online pass predictor
P2 = Pass(39430, 415, 428, 31, 14, 145, 63.31) #example pass from online pass predictor
P3 = Pass(47963, 418, 430, 25, 24, 165, 45.33) #example pass from online pass predictor
P4 = Pass(28654, 419, 434, 196, 26, 335, 97.77)
P5 = Pass(47945, 422, 433, 22, 29, 170, 79.06)
P6 = Pass(43792, 426, 437, 207, 15, 329, 52.11)
P7 = Pass(43793, 435, 442, 208, 15, 329, 78.49)

PassList = [P1, P2, P3, P4, P5, P6, P7]
Schedule(PassList, 414, 443)
