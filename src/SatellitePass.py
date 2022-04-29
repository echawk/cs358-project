import requests
import json
import datetime
import time
import sqlite3;
import pandas as pd
import ephem # USE THIS in terminal TO IMPORT EPHEM python -m pip install ephem
import csv

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
    SchedNum = 1
    numconsidered = 0
    CurrSat = List[0]
    LST = 0 #Last Scheduled Time
    StartT = string_time_to_unix_time(StartT)
    EndT = string_time_to_unix_time(EndT)

    for x in range(1,len(List)): #Goes through every pass in List
        CompSat = List[x] #CompSat = relevent pass
        compsat_0_unix_time = string_time_to_unix_time(CompSat[0])
        if StartT <= compsat_0_unix_time: #only enters if start of pass is after the specified start time frame
            if EndT >= string_time_to_unix_time(CompSat[1]): #only enters if the end of pass is before the specified end time frame
                if CompSat[2] > 1: #only enters if the time of a pass is more than 100 sec
                    numconsidered = numconsidered+1 #this code runs whenever a sat is being considered
                    if LST < compsat_0_unix_time: #if the last scheduled time is before the start time
                    ###########################################################################
                    ##THIS IS WHERE THE SPECIFIC STATION PREFERENCES ARE ADDED
                    ##there have been a few provided examples of what priorities can be added
                    ###########################################################################
                    # this example checks if the sattelite is to the WEST of the ground station
                    # (can be used if there is a physical restriction making sats to the east unreadable)
                    #  if CompSat[3] < 180:
                    #       if CompSat[4] < 180
                    #
                    # this example checks if the duration of the pass is over 600 seconds long
                    # (can be used if short passes do not want to be considered)
                    #  if CompSat[2] > 600:
                    #
                    # this example only considers sattelites that are below limit_elevation height
                    # (can be used if the ground station can not accurately read sats above a certain elevation)
                    #  if CompSat[6] < limit_elevation:
                    #
                    ###########################################################################

                        #this scedules the currently considered sattelite (currently sceduling if it fits within schedule)
                        SchedList.append(CompSat)
                        SchedNum = SchedNum+1
                        LST = string_time_to_unix_time(CompSat[1])




    print('After considering', numconsidered, 'sattelites, scheduling pass readings of', len(SchedList), 'sattelites in the allocated time period')
    return SchedList

def SigScore(Pass):

    score = 1/1 + e^-x
    return score



def string_time_to_unix_time(input_str):
    ymd_s, hms_s = tuple(input_str.split(" "))
    year, month, day = tuple(ymd_s.split('-'))
    hms_s = hms_s.split(".")[0]
    hour, minute, second = tuple(hms_s.split(':'))
    date_time = datetime.datetime(int(year), int(month), int(day), int(hour), int(minute), int(second))
    return (time.mktime(date_time.timetuple()))


################
## MAIN
################

#Set up Stations and Passes


sats = sqlite3.connect("C:\\Users\\Yogif\\OneDrive\\Desktop\\Homework\\CS 358\\satdata\\passes.sqlite\\passes.sqlite")

sc = sats.cursor()
#print(sc.execute('SELECT name FROM sqlite_schema WHERE type=\'table\' AND name NOT LIKE \'sqlite_%\';'))
PassList = []
for row in sc.execute('SELECT * FROM passes;'): #fills in the PassList array with all of the 4.8M individual passes
    PassList.append(row)

for pass_ in PassList:
    start, end, duration, rizeaz, setaz, tca, max_el, gs, norad = pass_

#INFO READ IN IS FORMATTED AS: start, end, duration, riseaz, setaz, tca, max el, gs, norad (TCA IRRELEVENT)

InStartTime = '2018-08-10 00:00:00.000000'
InEndTime = '2018-08-13 00:00:00.000000'
FinSc = Schedule(PassList, InStartTime, InEndTime)

#Testing
#for y in range(len(FinSc)):
#    print(FinSc[y])

#Write to CSV
file = open('schedule.csv', 'w') #Opens file in write mode
writer = csv.writer(file)
for y in range(len(FinSc)):
    writer.writerow(FinSc[y])
file.close()
