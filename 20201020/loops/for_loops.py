# Clear terminal
import os
os.system("clear")

# Files
from finder import student_finder
print(student_finder())


# ===== ===== ===== =====
# ===== ===== ===== =====
# Parcours des éléments de lst (type list d'int)
lst = [1, 2, 3, 4]
for item in lst:
  print("element " + str(item)) # Identique à ci-dessous
  print("element", item) # Identique à ci-dessus
  # print(f"element {item} square {item ** 2}") # Identique à ci-dessus


# ===== ===== ===== =====
# ===== ===== ===== =====
# Parcours des éléments de names (type list de string)
names = ["simon", "arena"]
for name in names:
  print(name, "is first row")


# ===== ===== ===== =====
# ===== ===== ===== =====
# Parcours des éléments d'une string (type string)
for letter in "ESD":
  print(letter)