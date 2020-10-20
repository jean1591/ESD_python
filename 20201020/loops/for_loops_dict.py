# Clear terminal
import os
os.system("clear")

# Files
from finder import student_finder
print(student_finder())

my_dict = {"name": "Bob", "age": 30, "email": "b@example.com", "logged": True}

for key in my_dict: # Parcours des clefs
# for key in my_dict.keys(): # Identique ligne dessus
  print(key, my_dict[key])


print("===== " * 10)
for value in my_dict.values(): # Parcours des valeurs
  print(value)


print("===== " * 10)
# Afficher la valeur si celle-ci est égale à Bob

# 1. Parcours des valeurs
for value in my_dict.values():
  # 2. Test sur valeur => my_dict[key] == "Bob"
  if value == "Bob":
    # 3. Affichage si vrai
    print(value)

# 1. Parcours des clefs
for key in my_dict.keys():
  # 2. Test sur valeur => my_dict[key] == "Bob"
  if my_dict[key] == "Bob":
    # 3. Affichage si vrai
    print(my_dict[key])

print("===== " * 10)
# 1. Parcours des clefs
for key in my_dict: # ["name", "age", "email", "logged"]
  # 2. Test sur nom de la clef
  if key == "email":
    # 3. Affichage si vrai
    print(key, my_dict[key])


print("===== " * 10)
# Affichez si clef == "age" ET valeur == 30
# 1. Parcours des clefs
for key in my_dict:
  # 2. Test sur nom de la clef et valeur de clef
  if key == "age" and my_dict[key] == 30:
    # 3. Affichage
    print(key, my_dict[key])

print("===== " * 10)
# Afficher si valeur == 30 OU si clef == "email"
for key in my_dict:
  if my_dict[key] == 30 or key == "email":
    print(my_dict[key])