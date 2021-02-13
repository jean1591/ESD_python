# IMPORTS
import requests
from pprint import pprint as pp

URL = "https://api.covid19api.com/summary"


# Créez une fonction qui récupère les éléments
def fetch_data(url):
    """
    Fetch data from url

    Args:
        url (string): url from which to retrieve data

    Returns:
        dict: Data as dict object if successful, error otherwise
    """
    res = requests.get(url)

    if res.status_code == 200:
        return res.json()
    else:
        print(res)


# Stockez le retour de votre fonction
covid_summary = fetch_data(URL)


# Supprimez la paire clef/valeur
if "Global" in covid_summary:
  del covid_summary["Global"]


# Somme des nouveaux cas par pays
def global_new_confirmed(data):
  global_new_cases = 0

  for d in data["Countries"]:
    global_new_cases += d["NewConfirmed"]
  
  return global_new_cases


# Nom du pays et le nombre de nouveaux cas du pays avec le plus de nouveaux cas
def worst_country(data):
  max_new_confirmed = -1
  country = None

  for d in data["Countries"]:
    if d["NewConfirmed"] > max_new_confirmed:
      max_new_confirmed = d["NewConfirmed"]
      country = d["Country"]
  
  return {"country": country, "cases": max_new_confirmed}


# Bonus
def bonus(data):
  global_new_cases = 0
  max_new_confirmed = -1
  country = None

  for d in data["Countries"]:
    global_new_cases += d["NewConfirmed"]

    if d["NewConfirmed"] > max_new_confirmed:
      max_new_confirmed = d["NewConfirmed"]
      country = d["Country"]
  
  return {
    "global_new_cases": global_new_cases,
    "country": country,
    "cases": max_new_confirmed
  }



new_confirmed = global_new_confirmed(covid_summary)
country = worst_country(covid_summary)

# pp(covid_summary)
print(new_confirmed)
pp(country)

res = bonus(covid_summary)
pp(res)