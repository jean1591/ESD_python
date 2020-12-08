import requests
from pprint import pprint

def fetch_data(url):
  """
  Fetch data from url

  Args:
      url (string): url from where to fetch data

  Returns:
      dict: JSON object containing data
  """
  res = requests.get(url)

  # Init data
  data = None

  # Check for correct status code
  if res.status_code == 200:
    # Parse data to JSON
    data = res.json()

  return data


url = "https://randomuser.me/api/?results=50&inc=name,email,location&nat=fr&seed=esd"

data = fetch_data(url)
# pprint(data)

# Extract users from data
users = data["results"]
# pprint(users)

for user in users:
  print(user.keys())
  break


for user in users:
  # Extract city from user["location"]
  user["city"] = user["location"]["city"]

  del user["location"]["city"]

  # Extract data from user["name"]
  user["first"] = user["name"]["first"]
  user["last"] = user["name"]["last"]

  del user["name"]

pprint(users)