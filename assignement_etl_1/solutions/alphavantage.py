import requests
from pprint import pprint as pp

# doc = "http://worldtimeapi.org/"

# ALPHAVANTAGE
api_key="H304HZH7RV40569G"


def fetch_crypto(crypto, currency, api_key):
    URL = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={crypto}&to_currency={currency}&apikey={api_key}"
    res = requests.get(URL)
    if res.status_code == 200:
        return res.json()
    else:
        print(res)


pp(fetch_crypto("ETH", "USD", api_key))