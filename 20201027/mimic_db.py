from random import choice, randint

print(choice([True, False]))
print(randint(0, 100))

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