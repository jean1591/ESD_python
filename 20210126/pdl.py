import requests
from pprint import pprint

profiles = ["robertoujean", "raphaël-fuentes-354074155", "lilou-roger", "miranarakotoarivony", "alexandre-lafon-100797107", "arenaguiose", "lucaschevalier", "lucie-guillaume", "yangtinglyv", "simon-masanet"]

URL = "https://api.peopledatalabs.com/v5/person/enrich?pretty=true&api_key=d03f91ecf13f21698a97d4fdc9c34e2c14c0a96b2e77c03f71cd978503322b69&profile=www.linkedin.com/in"

# Créez fonction qui récupère des données à partir d'une URL
def fetch_data(url, user_id):
  """
  Fetch data from url parameter and return data as json

  Args:
      url (string): URL from which to fetch data

  Returns:
      dict: Data as dict (json) object
  """
  res = requests.get(f"{url}/{user_id}")
  # res = requests.get(url + "/" + user_id)

  if res.status_code == 200:
    return res.json()
  return {}

# robertoujean = fetch_data(URL, "robertoujean")

user_data = {}
# Créez boucle sur profiles
# Pour chaque profil, créez une clef dans user_data avec l'id et en valeur le retour de fetch_data(URL, id)
for user in profiles:
  print(f"{URL}/{user}")
  tpm_data = fetch_data(URL, user)
  user_data[user] = tpm_data["data"]


# Affichage des données

# Loop profiles in user_data
for user in user_data.keys():
  print(user)

  # Loop experiences in user_data[user]["experience"]
  for xp in user_data[user]["experience"]:
    if xp["title"] is not None:
      print(xp["title"]["name"])
    
    if xp["company"] is not None:
      print(xp["company"]["name"])

      if xp["company"]["location"] is not None and xp["company"]["location"]["locality"] is not None:
        print(xp["company"]["location"]["locality"])
      print(xp["company"]["industry"])
    
    print("===== " * 5)
  
  print("===== " * 10)
  print("===== " * 10)
  print("\n")





""" for user in user_data.keys():
  print(user.upper())
  # Loop experiences in user_data[user]["experience"]
  for xp in user_data[user]["experience"]:
    title = xp["title"]["name"] if xp["title"]["name"] is not None else None
    if title is not None:
      print(title.title())
    
    if xp["company"] is not None:
      location = xp["company"]["location"]["locality"] if xp["company"]["location"]["locality"] is not None else ""
      
      print(f"{xp['company']['name'].title()} ({location.title()})")
      print(f">> Industry: {xp['company']['industry']}")
      print(f">> Founded: {xp['company']['founded'] if xp['company']['founded'] is not None else 'n/a'}")
    
    print("===== " * 5)
  
  print("===== " * 10)
  print("===== " * 10)
  print("\n") """










# Utilisez cette fonction dans une boucle pour récupérer tous les profils de la classe => enregistrez les données dans un dict avec vos nom_prenom comme clef
# Créez un scrip de nettoyage des données (paramètres: dict ci-dessus)