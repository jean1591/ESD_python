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

# Formatage des données
def format_phone(n_phone):  
  """
  Format phone number
  Replace all "-" with empty char

  Args:
      n_phone (string): Phone number to be formated

  Returns:
      string: Formated phone number
  """
  return user["phone"].replace("-", "")




url = "https://randomuser.me/api/?results=50&inc=name,email,phone&nat=fr&seed=esd"

data = fetch_data(url)
# pprint(data)

# Extract users from data
users = data["results"]

# Aplanir
for user in users:
  # Extract data from user["name"]
  user["firstname"] = user["name"]["first"]
  user["lastname"] = user["name"]["last"]
  user["title"] = user["name"]["title"]

  # Delete key name from user
  del user["name"]

# Format phone number using format_phone
for user in users:
  user["phone"] = format_phone(user["phone"])



# Dans le cadre d'un Transform, il est plus performant de ne parcourir qu'une
# seule fois les données, le code ci-dessus est structuré de façon à être
# plus compréhensible mais n'est pas algo correct. Vous trouverez ci-dessous
# une version algo correct du même code:

""" for user in users:
  # Extract data from user["name"]
  user["firstname"] = user["name"]["first"]
  user["lastname"] = user["name"]["last"]
  user["title"] = user["name"]["title"]

  # Delete key name from user
  del user["name"]

  # Format phone number using format_phone
  user["phone"] = format_phone(user["phone"]) """



pprint(users)