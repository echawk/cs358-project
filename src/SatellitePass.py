import requests
import json

# var names
downlink_low = 0 #low end of the transmitter freq range
downlink_high = 0 #low end of the transmitter freq range
station_low = 0 #high end of the transmitter freq range
station_high = 0 #high end of the transmitter freq range

# Find passes
satellites = []
passesAbove = []
print('Finding all passes for %s satellites:' % len(satellites))

# is the satellite above the horizon (aka during a pass) at this time?
# is the transmitter frequency (`downlink_*`) within the frequency range of the antenna(s)?

#LOOP though all of the passes found using the following criteria

if downlink_low < station_low:
    TrashSatellite()


def TrashSatellite():
    print("satellite is invalid")
