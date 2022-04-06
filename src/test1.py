import requests
import json

defaultPref = 0
null = 0


stationlist = requests.get("https://db.satnogs.org/api/transmitters/")
satellitelist = requests.get("https://db.satnogs.org/api/satellites/")
print(stationlist.status_code)
print(satellitelist.status_code)
#print(stationlist.json())
#print(satellitelist.json())

def score(INnode, Preferences):
  scoreval = 0 #value of the node
  nodetype = 0 # 0 - no input 1 - satellite 2 - ground station
  if 'mode' in INnode: #if it is a station
    nodetype = 2
  else: #if it is a satellite
    nodetype = 1
  if Preferences == 0: #if the preferences given is empty
      Preferences = defaultPref #set to the default preferences


  if nodetype == 1: #Sattelite Scoring
      print("This is a satellite")

      if INnode["status"] == "dead":

          scoreval = scoreval - 100

    #check status if alive give x if dead give -1000000

    #check countries
    #check pass

  elif nodetype == 2: #Station Scoring
    print("This is a station")

    if INnode["status"] == "dead": #if station is dead give -100 score
      scoreval = scoreval - 100



  print("The score of this node is ",scoreval)
  return scoreval

#NOI = 1#command to take an individual node (sattelite or station) from the list and turn it into Node of interest
satellite = satellitelist.json()
station = stationlist.json()
NOI = satellite[35] #accesses the first object in the json use sat[0]["name"] for more specific
PrefList = 0 #object containing the preferenced used in the scoring function
score(NOI,PrefList)


# FROM OLD SATPASS.py
# var names
downlink_low = 0 #low end of the transmitter freq range
downlink_high = 0 #high end of the transmitter freq range
station_low = 0 #low end of the station freq range
station_high = 0 #high end of the station freq range
sLat = 0 #station Latitude
sLong = 0 #station Longitude

# Functions

def TrashSatellite():
    print("satellite is invalid")

def create_observer(lat, lon, alt, min_riseset=0.0):
    '''
    Create an observer instance.
    '''
    # pylint: disable=assigning-non-slot
    observer = ephem.Observer()
    observer.lat = str(lat)
    observer.lon = str(lon)
    observer.elevation = alt
    observer.horizon = str(min_riseset)

    return observer


def FindPasses(satellite, observer, tmin, tmax, minimum_altitude, min_pass_duration):
    passes = []

    sat_ephem = ephem.readtle(str(satellite.tle0))

    #set start time
    # observer.date = ephem.date(tmin)


# Find passes
#print('Finding all passes for %s satellites:' % len(satellites))



#loop over all passes
# is the satellite above the horizon (aka during a pass) at this time?
# is the transmitter frequency (`downlink_*`) within the frequency range of the antenna(s)?

#LOOP though all of the passes found using the following criteria
SatTLE = 0 #satellite position prediction
if downlink_low < station_low:
    TrashSatellite()
if downlink_high > station_high:
    TrashSatellite()
#check if the sattelite pass is ABOVE the horizon


    #TEST FROM SCHEDULING FUNCTION
    for j in range(0, len(List)):
        CompSat = List[j]
        if CompSat.Sperc > 70.0:
            if SchedNum > 1: #if this is NOT the first sat being scheduled
                if SchedList[SchedNum-1].LOSt > CompSat.AOSt : #if the previously scheduled sat's end time is greater than the curr sats start time
                    SchedList.append(CompSat)
                    SchedNum = SchedNum+1
            else: #if this is the first sat being scheduled
                SchedList.append(CompSat)
                SchedNum = SchedNum+1

    print(SchedList[1].ID)
