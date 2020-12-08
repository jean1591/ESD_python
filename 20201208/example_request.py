import requests
from pprint import pprint


# res = requests.get(url)

# data = None
# if res.status_code == 200:
#   data = res.json()

# pprint(data)

sport = "Soccer"
country = "France"
url = f"https://www.thesportsdb.com/api/v1/json/1/search_all_teams.php?s={sport}&c={country}"
# url = "https://www.thesportsdb.com/api/v1/json/1/search_all_teams.php?s=" + sport + "&c=" + country // Équivalent ligne ci-dessus

def fetch_data(url):
  res = requests.get(url)

  data = None
  if res.status_code == 200:
    data = res.json()

  return data

data = fetch_data(url)

teams = data["teams"]
for team in teams:
  print(team["strTeam"])