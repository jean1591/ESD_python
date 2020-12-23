import requests
from pprint import pprint


def fetch_data(url):
  res = requests.get(url)

  if res.status_code == 200:
    return res.json()
  return {}

data = fetch_data("http://newsapi.org/v2/top-headlines?country=fr&category=business&apiKey=80414d29bc9a4204abd1ec3673968341")

articles = data["articles"]


pprint(articles)