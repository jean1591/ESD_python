# Clear terminal
import os
os.system("clear")

# Files
from finder import student_finder
print(student_finder())


# ===== ===== ===== =====
# Créez 2 variables int_1 et int_2 initialisées à 123 et 456 respectivement
int_1 = 123
int_2 = 123

# À l'aide d'une structure conditionnelle if, vérifiez si int_1 et inférieur à int_2. Si c'est le cas, affichez int_1 < int_2
if int_1 > int_2:
  print("int_1 > int_2")
elif int_1 < int_2:
  print("int_1 < int_2")
elif int_1 == int_2:
  print("int_1 égal int_2")

# Dans tous les cas, affichez la somme de int_1 + int_2
print(int_1 + int_2)


# ===== ===== ===== =====
# Créez 2 variables str_1 et str_2 initialisées à "jean" et "ESD" respectivement
str_1 = "jean"
str_2 = "ESD"





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



age = 50

if age > 40 and age < 45:
    print("40/44 ans")
elif age > 40 and age <= 50:
    print("45+ ans")
elif age > 30:
  print("30 ans")
elif age > 20:
  print("20 ans")


# Une seule condition True nécessaire pour passer
if True or False:
  print("passed")

# Toutes les conditions doivent être True pour passer
if True and False:
  print("passed")



