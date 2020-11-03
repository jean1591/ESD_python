from random import choice, randint
import os

os.system("clear")

# print(choice([True, False]))
# print(randint(0, 100))

cat_list = ["household", "groceries", "travels", "extra", "rent"]

db = [
  {"value": 123,
  "executed": True,
  "cat": "household"}
]

# En partant de db = []
### Savoir faire une enregistrement à la fois
### Savoir ajouter l'enregistrement créée dans db
### Boucler n fois en créant et ajoutant des enregistrement


db = []

# Création d'un dict
tmp = {
  "value": randint(1, 1000),
  "executed": choice([True, False]),
  "cat": choice(cat_list)
}

# print(tmp)

db.append(tmp)

print(db)


# Faire boucle for
# Dans boucle => Générer dict tmp
# Dans boucle + Dict généré => Ajouter dict à db via .append()
# Fin boucle
# Afficher db via print()