# Clear terminal
import os
os.system("clear")

# Files
from finder import student_finder
print(student_finder())


# ===== ===== ===== =====
# Affichez tous les nombres entre 50, 87 inclus avec range()
for item in range(50, 88):
  print(item)


# ===== ===== ===== =====
# Affichez tous les nombres entre 50, 87 inclus avec un pas de 3 avec range()
exos = range(50, 88, 3)
print(list(exos))
for item in range(50, 88, 3):
  print(item)



# Tous les nombres pairs via modulo (%)
for item in range(10):
  if item % 2 == 0:
    print(item)

names = ["simon", "arena", "lilou", "lucie"]

# Affichez tous les prénoms qui commencent par "l"

# 1. Parcourir names
for i in names:

  # 2. Tester
  # print(i if i.startswith("l") else None)
  # if i[0] == "l":
  if i.startswith("l"):

    # 3. Affichez
    print(i)

