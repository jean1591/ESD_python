# IMPORTS
import requests
from pprint import pprint as pp

URL = "https://api.covid19api.com/dayone/country/france/status/confirmed"


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
covid_france = fetch_data(URL)


# Nous nous intéresserons uniquement aux données de France Métropolitaine
def only_french_data(data):
    """
    Filter data based on predefine condition

    Args:
        data (dict): Data to filter

    Returns:
        dict: Filtered data
    """
    new_data = []

    for d in data:
        if d["Province"] == "":
            new_data.append(d)
    
    return new_data

# Écrasez covid_france par le retour de votre fonction
covid_france = only_french_data(covid_france)


# Date ou la France a connu son pic épidémique
def covid_peak(data):
    """
    Find epidemic peak in data using for loop

    Args:
        data (dict): Data to analyse

    Returns:
        dict: Peak date and value
    """
    max_confirmed_cases = data[0]["Cases"]
    date_max_confirmed_cases = None

    for i in range(1, len(data)):
        confirmed_cases = data[i]["Cases"] - data[i - 1]["Cases"]
        if confirmed_cases > max_confirmed_cases:
            max_confirmed_cases = confirmed_cases
            date_max_confirmed_cases = data[i]["Date"]
    
    return {"worst_date": date_max_confirmed_cases, "cases": max_confirmed_cases}

peak = covid_peak(covid_france)

# pp(covid_france)
# print(len(covid_france))
pp(peak)
