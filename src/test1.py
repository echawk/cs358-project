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
<<<<<<< Updated upstream
      if INnode["status"] == "dead":
          scoreval = scoreval - 100

    #check status if alive give x if dead give -1000000
=======
      if INnode["status"] == "dead": #if station is dead give -100 score
        scoreval = scoreval - 100
      if INnode["country"] == "Russia": #if station is dead give -100 score
        scoreval = scoreval - 100


>>>>>>> Stashed changes
    #check countries
    #check pass

  elif nodetype == 2: #Station Scoring
    print("This is a station")
<<<<<<< Updated upstream
    #check status if alive give x if dead give -1000000


  print("The score of this node is ",scoreval)

=======
    if INnode["status"] == "dead": #if station is dead give -100 score
      scoreval = scoreval - 100



  print("The score of this node is ",scoreval)
  return scoreval
>>>>>>> Stashed changes

#NOI = 1#command to take an individual node (sattelite or station) from the list and turn it into Node of interest
satellite = satellitelist.json()
station = stationlist.json()
NOI = satellite[35] #accesses the first object in the json use sat[0]["name"] for more specific
PrefList = 0 #object containing the preferenced used in the scoring function
score(NOI,PrefList)

