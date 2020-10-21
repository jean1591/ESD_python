# Clear terminal
import os
os.system("clear")

# Files
from finder import student_finder
print(student_finder())


# ===== ===== ===== =====
# ===== ===== ===== =====
# Affichez tous les nombres entre 50, 87 inclus avec range()
for item in range(50, 88):
  print(item)


# ===== ===== ===== =====
# ===== ===== ===== =====
# Affichez tous les nombres entre 50, 87 inclus avec un pas de 3 avec range()
exos = range(50, 88, 3)
print(list(exos)) # range() retourne un objet de type range, il faut le cast en list pour pouvoir afficher ses éléments
# Parcours des éléments de range(50, 88, 3)
for item in range(50, 88, 3):
  print(item)


# ===== ===== ===== =====
# ===== ===== ===== =====
# Tous les nombres pairs via modulo (%)
for item in range(10): # Parcours des nombres de 0 à 9
  if item % 2 == 0: # item % 2 retourne le reste de la division de item par 2, si le nombre est pair ce reste est 0
    print(item)


# ===== ===== ===== =====
# ===== ===== ===== =====
# Affichez tous les prénoms qui commencent par "l"
names = ["simon", "arena", "lilou", "lucie"]
# 1. Parcourir names
for i in names:
  # 2. Tester
  # if i[0] == "l": # Correct, mais privilégier les méthodes quand elles existent
  if i.startswith("l"):
    # 3. Affichez
    print(i)


# ===== ===== ===== =====
# ===== ===== ===== =====
# Faire plusieurs fois le même traitement
for item in range(10): # Identique à for item in range(0, 10, 1): 
  print("Hello", item)


# ===== ===== ===== =====
# ===== ===== ===== =====
# Afficher les nombres pairs via range() dans un interval
for item in range(10, 21, 2): # Tous les nombres pairs entre 10 et 20
  print(item)

# Afficher les nombres impairs via range() dans un interval
for item in range(11, 21, 2): # Tous les nombres impairs entre 11 et 20
  print(item)