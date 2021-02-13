---
id: "course_style"

export_on_save:
  prince: true
---

@import "../../../my_style.less"

# PYTHON / ETL {.text_center}
## DEVOIR MAISON {.text_center}
##### Distribué le 26 Janvier 2021 {.text_center}
##### À rendre le 01 Fevrier 2021 {.text_center}


---
## Préambule
1. Créez un dossier `dm_etl_1_prenom` (en remplaçant `prenom` par votre prénom). Créez un fichier `.py` par exercice, les noms de fichier sont donnés dans les intitulés de chaque exercice. Enregistrez les fichiers dans le dossier que vous avez créez
1. Architecture du dossier une fois DM terminé:
| dm_etl_1_prenom
| __ alphavantage.py
| __ covid_france.py
| __ covid_summary.py
| __ endpoints.py
| __ fligh.txt
1. Quand vous avez terminé, compressez votre dossier et envoyez moi le fichier compressé sur Slack en DM
1. Commentez votre code, décrivez ce que vous faites: **pas de commentaire = -2 point**
1. Les questions sont indépendantes les unes des autres, ne bloquez pas sur un bug ou une question. Si vous n'y arrivez pas ou que votre bug vous résiste, commentez ce qui crée le bug et passez à la question suivante
1. Ne copiez pas les uns sur les autres, sinon ce sera 0 pour l'exercice complet. Vous avez accès aux cours et à Internet, mais interdiction d'échanger les uns avec les autres sur le DM
1. Ne faites pas le DM au dernier moment, certaines API peuvent mettre plusieurs heures avant de vous fournir une clef API. Les retards ne seront pas excusés


---
## Endpoints (3 points - `endpoints.py`)
L'objectif de cet excercice est de chercher (et trouver) les endpoints (url) demandés.

Je souhaite uniquement les endpoints, je ne vous demande pas le code requêtant les API. Vous pouvez simplement coller les endpoints sous forme de commentaires dans `endpoints.py`.

### Time API
Lien vers la [doc](http://worldtimeapi.org/) (la doc est down assez fréquement, dans ce cas utilisez: [backup doc](https://web.archive.org/web/20201124225307/https://worldtimeapi.org/))

1. Trouvez l'endpoint qui retourne les localisations d'une zones en particulier (par exemple toutes les localisations d'`Europe` ou d'`Asia`)
1. Trouvez l'endpoint qui retourne l'heure d'une ville (dans une timezone) en particulier
1. Trouvez l'endpoint qui retourne l'heure d'une ville (dans une timezone) en particulier au format text (`.txt`)

### NASA
Cette API nécessite une clef API au delà de 30 requêtes / heure, je vous conseille de vous créer une clef API, c'est bien entendu gratuit. Si vous ne souhaitez pas donner votre adresse email vous pouvez utilisez [temp-mail](https://temp-mail.org/en/)

À partir de la [doc](https://api.nasa.gov/), trouvez les endpoints suivants:

1. Météo Martienne: affiche les détails de la météo sur Mars
1. Near Earth Object Web Service: affiche les astéroides proches de notre planète
1. Astronomy Picture of the Day: affiche les détails et un lien vers la photo astronomique du jour


---
## Alpha-Vantage (5 points - `alphavantage.py`)

--- | ---
--- | ---
Clef API obligatoire | Oui
Page de génération de clef API | [Clef API](https://www.alphavantage.co/support/#api-key)
Limitation | Maximum 5 requêtes par minute et 500 requêtes par jour
Lien vers la doc | [Doc](https://www.alphavantage.co/documentation/)


Fonction qui requête l'API d'Alpha-Vantage et retourne la valeurs d'une cryptomonnaie dans une devise donnée. Nous souhaitons utiliser la valeur d'`Exchange Rates` sur les cryptocurrencies. La fonction prend en paramètres `crypto` correspondant à la cryptomonnaie que l'on souhaite requêter, et `currency` qui est la devise dans laquelle nous souhaitons avoir la valeur de la cryptomonnaie (par exemple des Bitcoins en Euros)

--- | ---
--- | ---
Nom | `fetch_crypto`
Arguments | crypto (type `string`)
| | currency (type `string`)
Exemple d'appel | `fetch_crypto("BTC", "EUR")`
Traitement | Effectue une requête sur l'API d'Alpha-Vantage et retourne la valeur d'`Exchange Rates` de `crypto` en `currency`
Exemple de retour | Voir ci-dessous
Type du retour | `dict`

Exemple de retour de l'API avec Bitcoin (`"BTC"`) et Euro (`"EUR"`):
```bash
{
  'Realtime Currency Exchange Rate': {
    '1. From_Currency Code': 'BTC',
    '2. From_Currency Name': 'Bitcoin',
    '3. To_Currency Code': 'EUR',
    '4. To_Currency Name': 'Euro',
    '5. Exchange Rate': '26127.88523200',
    '6. Last Refreshed': '2021-01-05 15:40:02',
    '7. Time Zone': 'UTC',
    '8. Bid Price': '26127.87708500',
    '9. Ask Price': '26127.88523200'
  }
}
```


---
## COVID-19 - Summary (7 points - `covid_summary.py`)

--- | ---
--- | ---
Clef API obligatoire | Non
Lien vers la doc | [Doc](https://documenter.getpostman.com/view/10808728/SzS8rjbc)

L'endpoint https://api.covid19api.com/summary affiche un résumé de la journée en cours.

1. Créez une fonction qui prend en paramètre une url et récupère les éléments de cette url
1. Appelez votre fonction avec comme paramètre https://api.covid19api.com/summary et stocker le retour dans une variable `covid_summary`
1. Supprimez la paire clef/valeur `Global` de `covid_summary`
1. Créez une fonction qui prend en paramètre `covid_summary` et calcule et retourne le nombre de nouveaux cas confirmés sur la planète (somme des nouveaux cas confirmés par pays)
1. Créez une fonction qui prend en paramètre `covid_summary`, retourne le nom du pays qui a le plus de nouveaux cas ainsi que le nombre de nouveaux cas de ce pays

### Bonus round (+ 1 point)
Créez une fonction qui prend en paramètre `covid_summary` et réalise **dans une seule boucle** les traitements suivants:
- Nombre de nouveaux cas confirmés sur la planète
- Nom du pays et le nombre de nouveaux cas du pays avec le plus de nouveaux cas


---
## COVID-19 - France (7 points - `covid_france.py`)

--- | ---
--- | ---
Clef API obligatoire | Non
Lien vers la doc | [Doc](https://documenter.getpostman.com/view/10808728/SzS8rjbc)

L'endpoint https://api.covid19api.com/dayone/country/france/status/confirmed affiche le cumul de cas confirmés depuis le début de la pandémie en France (inclus DOM-TOM et autres territoires). Il ne s'agit pas du nombre de nouveaux cas mais du nombre cumulé de cas COVID-19.

**Remarque:**   
Le délai de récupération des éléments peut-être plus ou moins long, c'est normal

1. Réutilisez la fonction de récupération de l'exercice précédent et appelez la avec https://api.covid19api.com/dayone/country/france/status/confirmed comme paramètre. Stockez le retour de votre fonction dans une variable `covid_france`
1. Nous nous intéresserons uniquement aux données de France Métropolitaine, créez une fonction qui prend en paramètre `covid_france` et retourne un dict ne comprenant que les données de France Métropolitaine. Écrasez `covid_france` par le retour de votre fonction
1. Maintenant que `covid_france` ne contient plus que des données de France Métropolitaine, créez une fonction qui prend en paramètre `covid_france` et retourne la date ou la France a connu son pic épidémique avec le nombre de cas associés à cette date


---
## Flight App (7 points - `fligh.txt`)
> La création de fichier `.txt` se fait de la même manière que la création d'un fichier Python sur VSCode, changez simplement `.py` par `.txt`

Un client vous consulte pour créer une application de suivi de vols (flight tracking). Il souhaite que vous lui recommandiez une API possédant à minima un endpoint permettant de suivre un vol via son numéro de vol (aussi appelé `flight ICAO`, voir [wiki](https://en.wikipedia.org/wiki/International_Civil_Aviation_Organization)).

Trouvez cette API et affichez l'endpoint dans `fligh.txt`. Décrivez aussi votre raisonnement, comment avez-vous trouvé cette API, à partir de quelle(s) recherche(s), à partir de quel(s) site(s), l'API de votre choix a t'elle d'autres endpoints intéressants à recommander à votre client, l'API de votre choix a-t'elle des wrappers pour Python ou node.js permettant une intégration simplifiée de l'API dans votre application, ...

**Remarque:**   
L'endpoint doit être accessible gratuitement, la création de compte pour accéder à l'endpoint est acceptée.