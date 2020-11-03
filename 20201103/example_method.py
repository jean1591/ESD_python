


def display_mult_table(n):
  for i in range(0, 11):
    print(i * n)

# display_mult_table(5)



""" for element in range(11):
  display_mult_table(element) """


def my_func():
   print("Fonction my_func appelée")
   print("AZERTYUIOP")
   print("SDLksfjs")


# my_func()
# my_func()




def multiply(num_one, num_two):
  print(num_one, "*", num_two, ":")
  print(num_one * num_two)
  return num_one * num_two

  print("Hello") # Ne s'affiche pas car après le return


m1 = multiply(45, 67)
print(m1)
# m2 = multiply(123, 456)
# m3 = multiply(987, 654)

def add_n(a, b, c, d):
  """
  Add 4 numbers together and return

  Args:
      a (int): Number to add
      b (int): Number to add
      c (int): Number to add
      d (int): Number to add

  Returns:
      int: Sum of 4 numbers
  """
  return a + b + c + d



n = add_n(1, 2, 3, 4)
print(n)



# Fonction is_pos qui prend en arg un nombre, la fonction True si arg est > 0, False si <= 0
def is_pos(n):
  """
  Return True if n > 0, return False otherwise

  Args:
      n (int): Number to test

  Returns:
      bool: True if n > 0, return False otherwise
  """
  if n > 0:
    return True
  else:
    return False


print(is_pos(6))
print(is_pos(-6))




my_list = [1, 2, 3, 4, 5, 8, 10, 11, 16]
# Fonction only_even qui prend en argument une liste et qui affiche les éléments pairs de la liste
# Tip: utilisez le modulo % pour tester la parité
def only_even(lst):
  for n in lst:
    if n % 2 == 0:
      print(n)

only_even(my_list)




# Fonction only_even_r qui prend en argument une liste et qui retourne une liste des éléments pairs de la liste passée en argument
def only_even_r(lst):
  final_list = []

  for n in lst:
    if n % 2 == 0:
      final_list.append(n)
  
  return final_list


even_n = only_even_r(my_list)
print(even_n)




# Fonction max_from_two qui prend en parametre deux int et retourne le plus grand
def max_from_two(a, b):
  if a > b:
    return a
  else:
    return b
  
  # return max(a, b) => Même traitement que ci-dessus

maxi = max_from_two(45, 789)
print(maxi)




# Fonction max_from_three qui prend en parametre trois int et retourne le plus grand
def max_from_three(a, b, c):
  if a > b and a > c:
    return a
  elif b > a and b > c:
    return b
  else:
    return c


print(max_from_three(1, 2, 3))
print(max_from_three(3, 4, 5))
print(max_from_three(4, 6, 5))


# Fonction gen_user qui prend en parametre un nom (string) et un age (int) et qui retourne un dict
""" 
Retour de la fonction:
{
  "name": "jean",
  "age": 29
}
"""




my_list = [1, 2, 3, 4, 5, 22, 8, 10, 11, 16]
# Fonction get_max qui prend en paramètre une liste d'int et qui retourne le plus grand élément de la liste
