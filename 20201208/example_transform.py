import requests
from pprint import pprint

def fetch_data(url):
  res = requests.get(url)

  data = None
  if res.status_code == 200:
    data = res.json()

  return data

url = "https://randomuser.me/api/?results=50&inc=name,email,phone&nat=fr&seed=esd"

data = fetch_data(url)
# pprint(data)

users = data["results"]

# Aplanir
for user in users:
  # Extract data from user["name"]
  user["firstname"] = user["name"]["first"]
  user["lastname"] = user["name"]["last"]
  user["title"] = user["name"]["title"]

  # Delete key name from user
  del user["name"]


# Formatage des données
def format_phone(n_phone):
  return user["phone"].replace("-", "")

for user in users:
  user["phone"] = format_phone(user["phone"])

pprint(users)