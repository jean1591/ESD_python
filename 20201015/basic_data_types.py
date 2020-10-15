# INTEGER

my_int = 4
my_int_bis = 6
# total stock le résultat de my_int + my_int_bis soit 4 + 6
total = my_int + my_int_bis
print("total", total)



# Variante plus complexe
int_one = 4
int_one += 6
print("int_one:", int_one)
print(f"int_one: {int_one}")

# FLOAT
my_float = 123.456
my_float -= 100
print("my_float", my_float)
# Round my_float à 3 chiffres après la virgule
print("round(my_float, 3)", round(my_float, 3))

# TODO => Fiche round, square, sqrt, ...
print("56 ** 2", 56 ** 2)
print("56 ** 4", 56 ** 4)


# BOOLEAN
# [True, False]
my_boolean = True
not_my_boolean = not my_boolean
print("my_boolean", my_boolean)
print("not_my_boolean", not_my_boolean)

# Chainage de variables
print("my_boolean", my_boolean, "not_my_boolean", not_my_boolean)