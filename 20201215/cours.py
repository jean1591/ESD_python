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
  # Aplanissage - simple I
  # Extract city from user["location"]
  user["city"] = user["location"]["city"]

  del user["location"]["city"]

  # Aplanissage - simple II
  # Extract data from user["name"]
  user["first"] = user["name"]["first"]
  user["last"] = user["name"]["last"]

  del user["name"]

  # Aplanissage - avancé
  user["street_name"] = user["location"]["street"]["name"]
  del user["location"]

  # Formatage - simple
  # Use keys first & last
  # user["email"] = user["first"].lower() + "." + user["last"].lower() + "@esd.com"
  user["email"] = f"{user['first'].lower()}.{user['last'].lower()}@esd.com"
  # Replace domain
  # user["email"] = user["email"].replace("@example.com", "@esd.com")
  # Split on @ and append "@esd.com"
  # user["email"] = user["email"].split("@")[0] + "@esd.com"

  # Formatage - avancé
  """if user["first"][0] == user["last"][0]:
    user["first"] = user["first"] + " " + user["first"][0] + user["first"][0]
    user["flag"] = "AZERTYUIOPMLKJHGFDSQWXCVBN?AZERTYUIOPMLKJHGFDSQWXCVBN?AZERTYUIOPMLKJHGFDSQWXCVBN?AZERTYUIOPMLKJHGFDSQWXCVBN?AZERTYUIOPMLKJHGFDSQWXCVBN?AZERTYUIOPMLKJHGFDSQWXCVBN?AZERTYUIOPMLKJHGFDSQWXCVBN?AZERTYUIOPMLKJHGFDSQWXCVBN?AZERTYUIOPMLKJHGFDSQWXCVBN?" """
  
  if user["first"].startswith(user["last"][0]):
    user["first"] = f"{user['first']} {user['first'][0]}{user['first'][0]}"

    user["flag"] = "AZERTYUIOPMLKJHGFDSQWXCVBN?AZERTYUIOPMLKJHGFDSQWXCVBN?AZERTYUIOPMLKJHGFDSQWXCVBN?AZERTYUIOPMLKJHGFDSQWXCVBN?AZERTYUIOPMLKJHGFDSQWXCVBN?AZERTYUIOPMLKJHGFDSQWXCVBN?AZERTYUIOPMLKJHGFDSQWXCVBN?AZERTYUIOPMLKJHGFDSQWXCVBN?AZERTYUIOPMLKJHGFDSQWXCVBN?"



""" # Template string example
age = 29
print(f"J'ai {age} ans") """



pprint(users)