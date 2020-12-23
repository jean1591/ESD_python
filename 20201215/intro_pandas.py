import requests
from pprint import pprint
import pandas as pd

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


def fetch_sublevel(dct, first_level, second_level):
  return dct[first_level][second_level]

def main(url):
  """Fetch & Transform data 

  Args:
      url (string): URL from which to fetch data

  Returns:
      list: List of dict containing users
  """
  data = fetch_data(url)
  users = data["results"]

  for user in users:
    # Extract city from user["location"]
    user["city"] = fetch_sublevel(user, "location", "city")
    del user["location"]["city"]

    # Extract data from user["name"]
    user["first"] = user["name"]["first"]
    user["last"] = user["name"]["last"]
    del user["name"]

    # Extract street name from location/street/name
    user["street_name"] = user["location"]["street"]["name"]
    del user["location"]

    # Use keys first & last
    user["email"] = f"{user['first'].lower()}.{user['last'].lower()}@esd.com"

    # Add initials to first if first[0] == last[0]
    if user["first"].startswith(user["last"][0]):
      user["first"] = f"{user['first']} {user['first'][0]}{user['first'][0]}"

  return users

users = main("https://randomuser.me/api/?results=50&inc=name,email,location&nat=fr&seed=esd")


df = pd.DataFrame(users)
print(df)
print(df.info())
print(df.shape)

pprint(users)