# LIST
lst = [
  ["a", "r"],
  [23, 22]
]

# print(lst[0][0])
# print(lst[1][0])


# Concaténation
lst_one = [1, 2]
lst_two = ["a", "b"]
# print(lst_two + lst_one)

# Methodes
my_list = [1, 2]

# Ajouter à la fin de la liste
my_list.append(123456789)

# Ajoute le contenu d'une autre liste
other_list = [1, 3]
my_list.extend(other_list)

# Afficher le nombre d'occurrences d'un élément
print(my_list.count(1))

print(my_list)

unsorted_lst = [4, 3, 2, 1]
unsorted_lst.sort()
print("unsorted_lst", unsorted_lst)

unsorted_lst_a = [4, 3, 2, 1]
print("sorted(unsorted_lst_a)", sorted(unsorted_lst_a))
print("unsorted_lst_a", unsorted_lst_a)

# Tri sur int représentés sous forme de str
n_list = ["10", "1", "2"]
n_list.sort()
print(n_list)

# Inverse l'ordre d'une liste
n_list.reverse()
print(n_list)

# Supprime un élément par son index
n_list.pop(1)
print(n_list)

# Taille d'une liste
print("len(n_list)", len(n_list))

# Clear => vide la liste
n_list.clear()
print(n_list)

dct = {"one": 1, "two": 2, "three": 3}

# Récupère les clefs sous forme de liste
print(list(dct.keys()))

# Récupère les valeurs sous forme de liste
print(list(dct.values()))

# Récupère tous les éléments (clefs : valeurs)
print(list(dct.items()))

# Clear => vide le dict
dct.clear()
print(dct)