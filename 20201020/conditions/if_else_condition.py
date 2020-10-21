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
int_2 = 456

# À l'aide d'une structure conditionnelle if, vérifiez si int_1 et inférieur à int_2. Si c'est le cas, affichez int_1 < int_2
if int_1 > int_2:
  print("int_1 > int_2")

# Sinon, ajoutez 1000 à int_2
else:
  int_2 += 1000

# Dans tous les cas, affichez la somme de int_1 + int_2
print(int_1 + int_2)


# ===== ===== ===== =====
# ===== ===== ===== =====
# Créez 2 variables str_1 et str_2 initialisées à "Hello" et "World!" respectivement
str_1 = "Hello "
str_2 = "World!"

# À l'aide d'une structure conditionnelle if, vérifiez si la 1ère lettre de str_1 est en capital. Si c'est le cas, affichez str_2
if str_1[0].isupper(): # str_1[0] récupère le 1er caractère de str_1, .isupper() véfifie si l'élément passé est en capital
  print(str_2)

# Sinon écrasez str_2 par "ESD"
else:
  str_2 = "ESD"

# Dans tous les cas, affichez concaténation str_1 + str_2
print(str_1 + str_2)


# ===== ===== ===== =====
# ===== ===== ===== =====
# Créez une variable boolean initialisée à False
boolean = False

# À l'aide d'une structure conditionnelle if, vérifiez si boolean est égal à True. Si c'est le cas, affichez "boolean is True"
if boolean:
  print("boolean is True")
# Sinon Affichez "boolean is False"
else:
  print("boolean is False")
