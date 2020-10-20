# Clear terminal
import os
os.system("clear")

# Files
from finder import student_finder
print(student_finder())


# Une table
p1 = 5
for i in range(11):
  print(p1, "x", i, "=", p1 * i)

print("===== " * 10)
# Table de 0 à 2
for p1 in range(3):
  print("Table", p1)
  for p2 in range(11):
    print(p1, "x", p2, "=", p1 * p2)

print("===== " * 10)
str_lst_1 = [0, 1, 2, 3, 4, 5] # == range(6)
str_lst_2 = ["a", "z", "e", "r", "t", "y"]

# Affichez pour chaque élément de str_lst_1 tous les éléments de str_lst_2
for i in str_lst_1:
  print(i)
  for j in str_lst_2:
    print(j)

print("===== " * 10)
# Affichez les éléments au même index dans les liste str_lst_1 & str_lst_2
# (0, "a")
# (1, "z")
# (2, "e")
for i in str_lst_1:
  print(i, str_lst_2[i])