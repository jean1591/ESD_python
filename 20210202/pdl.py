import requests
from pprint import pprint
import pandas as pd

profiles = ["robertoujean", "jeremydimeglio"]
# profiles = ["robertoujean", "jeremydimeglio", "elisaetcheverry", "stephanielaporte", "alexandre-bonhomme-7095a4100"]

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

# pprint(user_data)


# Init empty experience list
xp = []

for user in user_data:
  # Loop user's experiences
  for experience in user_data[user]["experience"]:
    # Fetch value if exists
    company_name = "n/a"
    if experience["company"] and experience["company"]["name"]:
      company_name = experience["company"]["name"]

    location = None
    if experience["company"] and experience["company"]["location"] and experience["company"]["location"]["locality"]:
      location = experience["company"]["location"]["locality"]

    position = "n/a"
    if experience["title"] and experience["title"]["name"]:
      position = experience["title"]["name"]

    # Equivalent in ternary conditions
    # company_name = experience["company"]["name"] if experience["company"] and experience["company"]["name"] else "n/a"
    # location = experience["company"]["location"]["locality"] if experience["company"] and experience["company"]["location"] and experience["company"]["location"]["locality"] else "n/a"
    # position = experience["title"]["name"] if experience["title"] and experience["title"]["name"] else "n/a"

    # Push to xp list
    xp.append({
      "user_id": user,
      "company_name": company_name,
      "location": location,
      "position": position
    })
    """ xp.append([
      user,
      company_name,
      location,
      position
    ]) """

# pprint(xp)

















# Create DataFrame from list of dict (or list of lists)
df = pd.DataFrame(xp)

# Rename columns
df.columns = ["id", "company", "location", "position"]

print(df)

# Select single column
print("Select single column")
print(df["location"])
# Select single row
print("Select single row")
print(df.iloc[7])
# Select single cell
print("Select single cell")
print(df.loc[7, "location"])


