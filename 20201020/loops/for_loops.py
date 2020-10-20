# Clear terminal
import os
os.system("clear")

# Files
from finder import student_finder
print(student_finder())


# ===== ===== ===== =====
lst = [1, 2, 3, 4]
for item in lst:
  print("element " + str(item))
  print("element", item)
  # print(f"element {item} square {item ** 2}")


names = ["simon", "arena"]

for name in names:
  print(name, "is first row")


for letter in "ESD":
  print(letter)


# for item in range(0, 10, 1): 
for item in range(10):
  print("Hello", item)

for item in range(10, 21, 2): # Tous les nombres pairs entre 10 et 20
  print(item)

for item in range(11, 21, 2): # Tous les nombres impairs entre 11 et 20
  print(item)