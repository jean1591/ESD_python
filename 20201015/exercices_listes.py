n = list("ABC")
print(n)

# Alphabets
list_one = ["a", "b", "c"]

# Empty list to number list
empty_list = []
empty_list.append(0)
empty_list.append(1)
empty_list.append(2)
empty_list.append(3)
# empty_list.extend([0, 1, 2, 3])

# Reverse list
my_list = [1, 2, 3, 4, 5, 6]
my_list.reverse()
print(my_list)

# List length
my_list = [1, 2, 3, 4, 5, 6]
print(len(my_list))

# Item in list
my_list = [1, 2, 3, 4, 5, 6]
number_check = 3
print(my_list.count(number_check))
print(number_check in my_list)

# Déclaration de liste
empty_list = []
str_list = ["one", "two", "three"]
int_list = [1, 2, 3]

# Concaténation de listes
concat_list = str_list + int_list

# Méthodes sur les listes
concat_list.append("four")

# Accès aux éléments
print(concat_list[3:6])

# Découpage de liste
print(concat_list[:3])
print(concat_list[3:6])

print(concat_list)