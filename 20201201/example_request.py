import requests
from pprint import pprint


# RANDOMUSER.API
res = requests.get("https://randomuser.me/api/?results=5&inc=name,email,phone&nat=fr&seed=esd")


data = None
if res.status_code == 200: # 200 = la requête s'est bien passée
  data = res.json() # Récupère les données au format JSON
  # pprint(data)

mailing = []
for user in data["results"]:
  mailing.append(user["email"])
print(mailing)



# THESPORTSDB API
res = requests.get("https://www.thesportsdb.com/api/v1/json/1/all_sports.php")


data = None
if res.status_code == 200: # 200 = la requête s'est bien passée
  data = res.json() # Récupère les données au format JSON
  # pprint(data)

for sport in data["sports"]:
  print(sport["strSport"])



# LASTFM API
res = requests.get("https://ws.audioscrobbler.com/2.0/?method=artist.getinfo&artist=Queen&api_key=2357e0e1756b0a1bf1db18ff322787a8&format=json")


data = None
if res.status_code == 200: # 200 = la requête s'est bien passée
  data = res.json() # Récupère les données au format JSON
  # pprint(data)

for artist in data["artist"]["similar"]["artist"]:
  print(artist["name"])


# COVID
res = requests.get("https://raw.githubusercontent.com/opencovid19-fr/data/master/dist/chiffres-cles.json")


data = None
if res.status_code == 200: # 200 = la requête s'est bien passée
  data = res.json() # Récupère les données au format JSON
  pprint(data)


# FINANCE
money_one = "EUR"
money_two = "USD"
url = "https://query1.finance.yahoo.com/v8/finance/chart/" + money_one + money_two + "=X?region=FR&lang=fr-FR&includePrePost=false&interval=1d&range=1mo&corsDomain=fr.finance.yahoo.com&.tsrc=finance"

print(url)
res = requests.get(url)

data = None
if res.status_code == 200: # 200 = la requête s'est bien passée
  data = res.json() # Récupère les données au format JSON
  # pprint(data)


volume = data["chart"]["result"][0]["indicators"]["quote"][0]["volume"]
print(volume)
print(len(volume))