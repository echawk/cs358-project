import requests
import json
import ephem # USE THIS in terminal TO IMPORT EPHEM python -m pip install ephem

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

Station =create_observer(0, 0, 200, min_riseset=0.0)
FindPasses(sattelite, Station, tmin, tmax, minimum_altitude, min_pass_duration)

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
