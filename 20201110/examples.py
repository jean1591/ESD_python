from os import system

try:
  system("clear") # => MAC / LINUX
except:
  system("cls") # => WINDOWS



# Fonction gen_user qui prend en parametre un nom (string) et un age (int) et qui retourne un dict
""" 
Retour de la fonction:
{
  "name": "jean",
  "age": 29
}
"""
def gen_user(name, age):
  return {"name": name, "age": age}

print(gen_user("jean", 29))



my_list = [1, 2, -3, 4, 5, 22, -8, 10, 11, 16]
my_list_neg = [-22, -8, -10]
# Fonction get_max qui prend en paramètre une liste d'int et qui retourne le plus grand élément de la liste
def get_max(lst):
  # 1. Créez var tmp qui stock le plus grand élément actuel
  tmp = lst[0]

  # 2. Parcours de la liste
  for element in lst:
    # 3. Vérifiez si l'élément parcouru est plus grand que tmp
    if element >= tmp:
      # 4. Si plus grand => Mettre tmp avec l'élément actuel
      tmp = element

  # 5. Retourne tmp
  return tmp

print(get_max(my_list))
print(get_max(my_list_neg))



# Expliquez le traitement du script suivant:
def some_function(string):
    """
    Order unique letters from string

    Args:
        string (string): String to analyse

    Returns:
        list: Letters ordered alphabetically
    """
  
    # Init empty list
    letters = []

    # Loop string using lowercase letters
    for l in string.lower():
        # Test if l is in letters
        if l not in letters:
            # If not, add l to letters
            letters.append(l)
    
    # Return sorted letters
    return sorted(letters)


print(some_function("string"))
print(some_function("jean"))
print(some_function("aabbccddee"))


# Fonction is_pal qui prend en paramètre une string et qui retourne True si la string est un palindrome, False sinon
def is_pal(string):
  # Tester si string est égale à string lue de droite à gauche
  """ if string == string[::-1]:
    return True
  else:
    return False """

  return string == string[::-1]

print(is_pal("radar"))
print(is_pal("wow"))
print(is_pal("hello"))


my_list = [1, 2, -3, 4, 5, 22, -8, 10, 11, 16]
my_list_neg = [-22, -8, -10]
# Fonction sum_of_list qui prend en paramètre une liste d'int et qui retourne la somme de cette liste
def sum_of_list(lst):
  # Initialisation à 0 de la variable de total
  total_sum = 0

  # Parcours des éléments de my_list
  for b in lst:
    # B => Ajout de l'élément parcouru à total
    # print(">>", total)
    total_sum += b

  # Retourne total
  return total_sum

print(sum_of_list(my_list))
print(sum_of_list(my_list_neg))


# Fonction apply_coupon qui prend en paramètre une liste d'int et qui retourne 0 si la somme des éléments de la liste est supérieur à 100, sinon retourne 30
def apply_coupon(lst):
  res = sum_of_list(lst)

  if res > 100:
    return 0
  else:
    return 30

print(apply_coupon([100, 1, 200, 400]))
print(apply_coupon(my_list))
print(apply_coupon(my_list_neg))