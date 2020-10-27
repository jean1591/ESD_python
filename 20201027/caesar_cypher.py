# Module contenant des méhodes et attributs sur les string
import string
# Module pour clear (cls pour Windows) le terminal
import os
# Module pour afficher les dict de manière plus lisible
from pprint import pprint

# Clear terminal
os.system("clear")

# Récupère toutes les lettres de l'alphabet en minuscules
letters = string.ascii_lowercase
# print(letters)


codex = {}
ind = 15
# Pour chaque caractère de la var letters, crée un clef avec le caractère et une valeur avec letters[ind % 26]
for l in letters:
  codex.update({l: letters[ind % 26]})
  ind += 1

# Gestion des espaces
codex.update({" ": " "})

# String à chiffrer
text = "Bonjour bonjour"

# Init string chiffrée
text_crypted = ""

# pprint(codex)

# Pour chaque caractère de la var text, ajoute la valeur de la clef c à text_crypted
for c in text.lower():
  text_crypted += codex[c]

print(text, "=>", text_crypted)


# Pour aller plus loin
# À partir d'une string cryptée et d'un index, décryptez la string