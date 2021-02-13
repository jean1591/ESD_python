---
id: "course_style"

export_on_save:
  prince: true
---

@import "../../../my_style.less"

# PYTHON {.text_center}
## DEVOIR MAISON (DM ETL 1) {.text_center}
##### Notes et Commentaires {.text_center}

---
## Notes
Nom | Note
--- | ---
Alexandre | 14.50
Aréna | 16.00
Lilou | 18.00
Lucas | 18.75
Lucie | 16.75
Lyvahne | 14.00
Marie | 16.75
Mirana | 14.50
Raphaël | 18.00
Simon | 18.00
Yann | 19.50

> Quand des erreurs sont répétés sur plusieurs exercices, je n'ai décompté les points que la premières fois


---
## Alexandre
**21.00/29 => 14.50/20**

#### Endpoints (3 / 3)


#### Alpha-Vantage (4 / 5)
Tu stockes `url1`, `url2` et `url3` en dehors de la fonction `fetch_crypto`, ça fonctionne mais c'est considéré comme une mauvaise pratique que d'utiliser des variables en dehors du scope de la fonction.


#### COVID-19 - Summary (6 / 7)

##### Pays avec le plus de nouveaux cas
Le `None` est du au fait que tu `print` le retour de ta fonction `top_new` mais que cette dernière n'a pas de `return`, donc la fonction retourne par défaut `none`.

C'est d'ailleurs une erreur, l'exercice demandait que l'on retourne les éléments et non qu'on les affiche.

Concernant tes questions:
- `for product in covid_summary["Countries"]: KeyError: 'Countries'`: c'est étonnant, il devait y avoit autre choses
- `SyntaxError: 'return' outside function`: le return de ta fonction n'était probablement pas indendé correctement, donc Python le considéré en dehors de la fonction.


#### COVID-19 - France (1 / 7)
`covidfrance` est une liste, tu peux parcourir les éléments d'une liste via `for element in my_list:`. Si une erreur t'échappe essaye de faire `print(type(covidfrance))`, ça te donnera le type de l'objet et te débloquera peut-être.


#### Flight App (7 / 7)


---
## Arena
**23.00/29 => 16.00/20**

#### Endpoints (2 / 3)
`/api/timezone/Europe`, `/api/timezone/America/Argentina/Salta` et `/api/timezone/Europe/London.txt` ne sont pas des endpoints.


#### Alpha-Vantage (2 / 5)
Pourquoi faire `return r.text` ? Nous n'avons jamais utilisé cette méthode, en faisant ça tu retournes une string au lieu de retourner un dict comme cela est demandé dans le DM.

De plus tu ne testes pas le `status.code` de `r`.

Aussi, tu utilises `api_key` qui est stocké en dehors du scope de ta fonction `fetch_crypto`, il faut éviter de faire cela ça peut te créer des problèmes de nommage ou d'accès aux variables.


#### COVID-19 - Summary (7 / 7)


#### COVID-19 - France (5 / 7)

##### Pic épidémique
Tu as mal lu la doc, `record["Cases"]` ne correspond pas au nopbre de nouveaux cas mais au nombre de cas cumulés depuis le début de l'épidémie. le script ne fait pas le bon traitement.


#### Flight App (7 / 7)


---
## Lilou
**26.00/29 => 18.00/20**

#### Endpoints (3 / 3)


#### Alpha-Vantage (5 / 5)


#### COVID-19 - Summary (5 / 7)

##### Nouveaux cas confirmés sur la planète
```python
for key in covid_summary:
    for country_data in covid_summary[key]:
        for k in country_data:
```
À chaque boucle imbriquée tu augmentes la complexité du traitement et l'espace mémoire. Ton algo tourne en `Cubic Time O(n^3)` (je te laisse aller voir si ça t'intéresse) mais c'est très gourmand et peu recommandé d'utiliser des algo de ce niveau là.

Surtout que tu pouvais faire bien plus simplement:
```python
global_new_cases = 0

for d in data["Countries"]:
  global_new_cases += d["NewConfirmed"]
```

##### Pays avec le plus de nouveaux cas
Mêmes commentaires que ci-dessus.

Il y a une erreur dans ton script mais je n'arrive pas à la trouver.

##### Bonus (1 / 1)


#### COVID-19 - France (5 / 7)

##### Pic épidémique
Tu as mal lu la doc, `k['Cases']` ne correspond pas au nopbre de nouveaux cas mais au nombre de cas cumulés depuis le début de l'épidémie. le script ne fait pas le bon traitement.


#### Flight App (7 / 7)


---
## Lucas
**27.00/29 => 18.75/20**

#### Endpoints (3 / 3)


#### Alpha-Vantage (5 / 5)


#### COVID-19 - Summary (5 / 7)

##### Nouveaux cas confirmés sur la planète
Tu utilises `i["TotalConfirmed"]` quand il fallait utiliser `i["NewConfirmed"]`, je t'invite à lire la doc pour voir la différence.


#### COVID-19 - France (7 / 7)
Tu t'es un peu complexifié la tache mais ça fonctionne.

#### Flight App (7 / 7)


---
## Lucie
**24.00/29 => 16.75/20**

#### Endpoints (3 / 3)


#### Alpha-Vantage (5 / 5)


#### COVID-19 - Summary (7 / 7)

##### Bonus (1 / 1)


#### COVID-19 - France (1 / 7)

##### Données de France Métropolitaine
`covid_france` est une liste, tu peux parcourir les éléments d'une liste via `for element in my_list:`. Si une erreur t'échappe essaye de faire `print(type(covid_france))`, ça te donnera le type de l'objet et te débloquera peut-être.

#### Flight App (5 / 7)
En attente d'endpoint complet


---
## Lyvahne
**20.00/29 => 14.00/20**

#### Endpoints (3 / 3)


#### Alpha-Vantage (4 / 5)
Reprends le DM et regarde bien le retour attendu: je n'attend pas uniquement la valeur d'une crypto dans une devise, mais aussi le données annexes.

#### COVID-19 - Summary (5 / 7)
L'ordonnancement de ton script n'est pas bon:
- ligne 7 tu utilises la fonction `make_requests`
- ligne 15: tu déclares la fonction `make_requests`

Tel que tu me l'as envoyé, ton script ne fonctionne pas.

##### Bonus (1 / 1)


#### COVID-19 - France (4 / 7)

##### Données de France Métropolitaine
C'est presque ça, il fallait juste faire `for case in summary:` au lieu de `for case in list(summary):`.

##### Pic épidémique
Tu as mal lu la doc, `day['Cases']` ne correspond pas au nopbre de nouveaux cas mais au nombre de cas cumulés depuis le début de l'épidémie. le script ne fait pas le bon traitement.


#### Flight App (3 / 7)
`https://USERNAME:PASSWORD@opensky-network.org/api/tracks/all` retourne tous les vols en cours, et non un vol en particuliers.


---
## Marie
**24.00/29 => 16.75/20**

#### Endpoints (3 / 3)


#### Alpha-Vantage (4 / 5)
Ta fonction ne retourne pas de résultat, elle l'affiche dans le terminal.


#### COVID-19 - Summary (6 / 7)

##### Pays avec le plus de nouveaux cas
Tu initialises `Max` en dehors de ta condition, mais tu initialises `Pays` dans la condition.
Il existe un cas ou `if countries["NewConfirmed"] > Max:` est toujours évalué à `false` (si `countries["NewConfirmed"]` est toujours négatif par exemple) et donc `Pays` n'est jamais instancié. Dans cette éventualité, ton `return` ferait crash ton script car tu ne peux pas retourner une variable non instanciée.

Aussi, il ne faut pas mettre de majuscules dans tes noms de variables, `Max` => `max`.

##### Bonus (1 / 1)
Mêmes commentaires que ci-dessus


#### COVID-19 - France (3 / 7)

##### Données de France Métropolitaine
Il aurait fallu prendre le problème dans l'autre sens: tu as créé une liste des dom-tom pour les purger, alors qu'il était plus simple de ne garder que les données de France Métropolitaine en filtrant par `""`.
Le probème que pose ta solution est le suivant: que se passe-t'il si il faut filtrer des milliers de territoires différents ?

##### Pic épidémique
De nouveau tu instancies des variables dans une condition, mêmes commentaires que `COVID-19 - Summary`.

Selon ton script, il y a eut 3 166 040 nouveaux cas le 31/01/2021, je pense que ton erreur vient du fait que associes la même valeur à `Max_cas` et à `Cas`.


#### Flight App (7 / 7)


---
## Mirana
**21.00/29 => 14.50/20**

#### Endpoints (3 / 3)


#### Alpha-Vantage (5 / 5)


#### COVID-19 - Summary (5 / 7)

##### Nouveaux cas confirmés sur la planète
`total_world = []` n'est pas instancié dans la fonction `NewCasesWorld`, cela fonctionne mais c'est vraiment une mauvaise pratique. Imagine par exemple que ta fonction soit stockée sur un autre fichier, tu n'aurais plus accès à `total_world` et cela ferait crasher ton script.


```python
for i in range(len(covid_summary["Countries"])):
    total_world.append(covid_summary["Countries"][i]["NewConfirmed"])
```
peut être écrit plus simplement:
```python
  for country in covid_summary["Countries"]:
    total_world.append(country["NewConfirmed"])
```

`return sum(total_world)` fonctionne mais une façon plus simple et moins gourmande en mémoire est de stocker la somme dans une variable que tu incrémentes à chaque tour de boucle.

##### Pays avec le plus de nouveaux cas
`details_country_cases = {}` et `for i in range(len(covid_summary["Countries"])):` => mêmes commentaires que ci-dessus.


#### COVID-19 - France (3 / 7)

##### Données de France Métropolitaine
`covid_france_only = []` et `for i in range(len(covid_france)):` => mêmes commentaires que ci-dessus.

##### Pic épidémique
`date_pic_covid = {}` et `for i in range(len(covid_france)):` => mêmes commentaires que ci-dessus.

`covid_france[i]["Cases"]` n'est pas le nombre de cas du jours mais le nombre de cas cumulés depuis le début de l'épidémie. Ton script ne fit pas le cachier des charges


#### Flight App (5 / 7)
`http://api.aviationstack.com/v1/flights?access_key=d27f799bb5beb495480e69d78df3f62f` ne permet pas de suivre un vol, quel est l'endpoint ?


---
## Raphaël
**26.00/29 => 18.00/20**

#### Endpoints (3 / 3)


#### Alpha-Vantage (4 / 5)
Reprends le DM et regarde bien le retour attendu: je n'attend pas uniquement la valeur d'une crypto dans une devise, mais aussi le données annexes.


#### COVID-19 - Summary (7 / 7)


#### COVID-19 - France (5 / 7)

##### Pic épidémique
Tu as mal lu la doc, `country['Cases']` ne correspond pas au nopbre de nouveaux cas mais au nombre de cas cumulés depuis le début de l'épidémie. le script ne fait pas le bon traitement.


#### Flight App (7 / 7)


---
## Simon
**26.00/29 => 18.00/20**

#### Endpoints (3 / 3)


#### Alpha-Vantage (5 / 5)


#### COVID-19 - Summary (5 / 7)

##### Pays avec le plus de nouveaux cas
Tu n'initialises pas `pays_nom` en dehors de la boucle, cela peut poser problème dans le cas ou `if country["NewConfirmed"] >= pire_pays:` est toujours évaluer à `false`.

##### Bonus (1 / 1)


#### COVID-19 - France (5 / 7)

##### Pic épidémique
Tu as mal lu la doc, `y['Cases']` ne correspond pas au nopbre de nouveaux cas mais au nombre de cas cumulés depuis le début de l'épidémie. le script ne fait pas le bon traitement.


#### Flight App (7 / 7)


---
## Yann
**28.00/29 => 19.50/20**

#### Endpoints (3 / 3)


#### Alpha-Vantage (5 / 5)


#### COVID-19 - Summary (7 / 7)

##### Bonus (1 / 1)


#### COVID-19 - France (5 / 7)

##### Données de France Métropolitaine
```python
if key["Province"] != "":
    del key
    #print(key)
else:
    ok.append(key)
```
C'est correct, mais il n'y a pas d'intéret à `del key` si au final tu retournes un autre objet.

##### Pic épidémique
```python
for key in summary:
    del key["City"], key["CityCode"], key["Country"], key["CountryCode"], key["Lat"], key["Lon"], key["Province"], key["Status"]
    key["delta"] = 0
```
Pourquoi faire ce traitement ?

Ça ne fonctionne pas car tu as mal lu la doc, `key['Cases']` ne correspond pas au nopbre de nouveaux cas mais au nombre de cas cumulés depuis le début de l'épidémie. le script ne fait pas le bon traitement.


#### Flight App (7 / 7)