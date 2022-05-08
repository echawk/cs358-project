import requests
import json
import datetime
import time
import sqlite3;
import csv
import math

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
    print('Creating Schedule From ', StartT, 'to ', EndT)
    SchedList = []
    SchedNum = 0
    numconsidered = 0
    StartT = string_time_to_unix_time(StartT)
    EndT = string_time_to_unix_time(EndT)
    LST = StartT #Last Scheduled Time
    PrevSatID = []
    PrevSatDesc = []
    List.sort()

    for x in range(1,len(List)): #Goes through every pass in List
        MatchID = 0
        CompSat = List[x] #CompSat = relevent pass
        compsat_0_unix_time = string_time_to_unix_time(CompSat[0])
        if StartT <= compsat_0_unix_time: #only enters if start of pass is after the specified start time frame
            if EndT >= string_time_to_unix_time(CompSat[1]): #only enters if the end of pass is before the specified end time frame
                if CompSat[2] > 600: #only enters if the time of a pass is more than 15 sec
                    for y in range(0,len(PrevSatID)):
                        if CompSat[8] == PrevSatID[y]:
                            MatchID = 1
                    if MatchID == 0: #disqualifies same sat ID from being scheduled twice
                        if PrevSatDesc != CompSat[7]:
                            numconsidered = numconsidered+1 #this code runs whenever a sat is being considered
                            Score = SigScore(CompSat,LST)
                            if Score > 0.5: #if the sigmoid score of the sattelite is greater than 0.5 (CHANGE THIS currently x > 0 in the sig function to be scheduled)

                                #this scedules the currently considered sattelite (currently sceduling if it fits within schedule)
                                print('Scheduling Sattelite with starting time ',CompSat[0], 'New Last Scheduled Time is ',CompSat[1])
                                SchedList.append(CompSat)
                                SchedNum = SchedNum+1
                                LST = string_time_to_unix_time(CompSat[1])
                                PrevSatID.append(CompSat[8])
                                PrevSatDesc = CompSat[7]




    print('After considering', numconsidered, 'sattelites, scheduling pass readings of', len(SchedList), 'sattelites in the allocated time period')
    return SchedList

def SigScore(Pass,LST):
    x = -10
    ###########################################################################
    ##THIS IS WHERE THE SPECIFIC STATION PREFERENCES ARE ADDED
    ##there have been a few provided examples of what priorities can be added
    ###########################################################################
    # this example checks if the sattelite is to the WEST of the ground station
    # (can be used if there is a physical restriction making sats to the east unreadable)
    #  if Pass[3] < 180:
    #       if Pass[4] < 180:
    #
    # this example checks if the duration of the pass is over 600 seconds long
    # (can be used if short passes do not want to be considered)
    #  if Pass[2] > 600:
    #
    # this example only considers sattelites that are below limit_elevation height
    # (can be used if the ground station can not accurately read sats above a certain elevation)
    #  if Pass[6] < limit_elevation:
    #
    # The X value directly changes what the score will be, negasive values will always be below a 0.5
    # while pos values increase the score exponentially, You should add to x based on how important the
    # preference is, and then increase the value that the score must be over in the schedule function to
    # prioritise based on those scores
    ###########################################################################
    satstart = string_time_to_unix_time(Pass[0])
    #print(LST)
    if LST < satstart: #if the last scheduled time is before the start time
        x = x+11
    score = 1/(1 + math.exp(-x))
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


sats = sqlite3.connect("C:\\Users\\Yogif\\OneDrive\\Desktop\\Homework\\CS 358\\satdata\\passes.sqlite\\passes.sqlite") #input file path to SAT PASS LIST sqlite file

sc = sats.cursor()
PassList = []
for row in sc.execute('SELECT * FROM passes;'): #fills in the PassList array with all of the 4.8M individual passes
    PassList.append(row)

#INFO READ IN IS FORMATTED AS: start, end, duration, riseaz, setaz, tca, max el, gs, norad (TCA IRRELEVENT)

InStartTime = '2018-08-01 00:00:00.000000'
InEndTime = '2018-08-01 20:00:00.000000' #currently makes schedule over 20 hour time period on August 1st 2018
FinSc = Schedule(PassList, InStartTime, InEndTime)

#Write Schedule to CSV
file = open('schedule.csv', 'w') #Opens file in write mode
writer = csv.writer(file)
for y in range(len(FinSc)):
    writer.writerow(FinSc[y])
file.close()
