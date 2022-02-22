import requests
stationlist = requests.get("https://db.satnogs.org/api/transmitters/")
satellitelist = requests.get("https://db.satnogs.org/api/satellites/")
print(stationlist.status_code)
print(satellitelist.status_code)
#print(stationlist.json())
#print(satellitelist.json())