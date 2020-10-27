#
lst_easy = []

#
lst_easy.append(1)

#
add_to_lst = [2, 3]
lst_easy.extend(add_to_lst)

#
print(len(lst_easy))

#
list_to_lst = [4, 5]
lst_easy.append(list_to_lst)

#
# [4, 5] est une variable de type list et ne compte par conséquent que pour une seul élément

print(lst_easy)