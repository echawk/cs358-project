import requests as req

r = req.get('https://db.satnogs.org/api/')

print(r.text)

