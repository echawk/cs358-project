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
    SchedNum = 1
    numconsidered = 0
    CurrSat = List[0]
    LST = '0' #Last Scheduled Time


    for x in range(1,len(List)): #Goes through every pass in List
        CompSat = List[x] #CompSat = relevent pass
        if StartT <= CompSat[0]: #only enters if start of pass is after the specified start time frame
            if EndT >= CompSat[1]: #only enters if the end of pass is before the specified end time frame
                numconsidered = numconsidered+1 #this code runs whenever a sat is being considered
                if LST < CompSat[0]: #if the last considered time is before the start time
                    SchedList.append(CompSat)
                    SchedNum = SchedNum+1
                    LST = CompSat[1]




    print('After considering', numconsidered, 'sattelites, scheduling pass readings of', len(SchedList), 'sattelites in the allocated time period')
    #print('After considering', len(List), 'sattelites, scheduling pass of sattelite ID(s): ', CurrSat.ID)
    #print('After considering', len(List), 'sattelites, scheduling pass of sattelite ID(s): ', len(SchedList))
    return SchedList

def GetPasses(Station, StartT, EndT, minimum_altitude, min_pass_duration):
    a = 0
    return

def string_time_to_unix_time(input_str):
    ymd_s, hms_s = tuple(input_str.split(" "))
    year, month, day = tuple(ymd_s.split('-'))
    hms_s = hms_s.split(".")[0]
    hour, minute, second = tuple(hms_s.split(':'))
    date_time = datetime.datetime(int(year), int(month), int(day), int(hour), int(minute), int(second))
    return ("unix_timestamp => ",(time.mktime(date_time.timetuple())))


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

InStartTime = '2018-09-12 07:22:40.080409'
InEndTime = '2018-09-13 21:51:21.865953'
FinSc = Schedule(PassList, InStartTime, InEndTime)
for y in range(len(FinSc)):
    print(FinSc[y])
