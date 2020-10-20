# Clear terminal
import os
os.system("clear")

""" var = 10
if var == 10:
  print("var égal 10") """




var_one = 10
var_two = 50
lst = []

if var_one < var_two:
  print("var_one < var_two")
  lst.append(1)
  lst.append(2)
  lst.append(3)
else:
  print("var_one >= var_two")

print("lst", lst)




count = 10
if count >= 5:
  if count <= 15:
    print("Count se situe entre 5 et 15")
  else:
    print("Count est supérieur à 15")
else:
  print("Count est inférieur à 5")

if count >= 5 and count <= 15:
  print("Count se situe entre 5 et 15")
else:
  print("Count pas dans l'interval")


majeur = True
if majeur is not True: # Si majeur n'est pas vrai
  print("Vous n'êtes pas majeur") # Affiche ceci
else: # Sinon
  print("Vous êtes majeur") # Affiche cela