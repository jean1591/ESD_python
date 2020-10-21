# Clear terminal
import os
os.system("clear")

# Files
from finder import student_finder
print(student_finder())


# ===== ===== ===== =====
# ===== ===== ===== =====
# Créez 2 variables int_1 et int_2 initialisées à 123 et 456 respectivement
int_1 = 123
int_2 = 123

# À l'aide d'une structure conditionnelle if/elif/else, vérifiez si int_1 est strictement supérieur à int_2, puis si int_1 est strictement inférieur à int_2 et enfin si int_1 est égal à int_2. Dans chaque condition, afficher du texte
if int_1 > int_2:
  print("int_1 > int_2")
elif int_1 < int_2:
  print("int_1 < int_2")
elif int_1 == int_2:
  print("int_1 égal int_2")

# Dans tous les cas, affichez la somme de int_1 + int_2
print(int_1 + int_2)


# ===== ===== ===== =====
# ===== ===== ===== =====
int_1 = 123
int_2 = 456

# int_1 et supérieur à int_2 : si c'est le cas, affichez int_1 > int_2
if int_1 > int_2:
  print("int_1 > int_2")

# Puis vérifiez si int_1 est égal à int_2 : si c'est le cas affichez int_1 == int_2
elif int_1 == int_2:
  print("int_1 égal int_2")

# Sinon affichez int_1 < int_2
else:
  print("int_1 < int_2")


# ===== ===== ===== =====
# ===== ===== ===== =====
# Une seule condition True nécessaire pour passer
if True or False:
  print("passed") # Affiche True

# Toutes les conditions doivent être True pour passer
if True and False: # N'affiche rien
  print("passed")



