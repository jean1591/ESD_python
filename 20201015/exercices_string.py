# STRING
string_with_quotes = 'string avec apostrophes'
string_with_double_quotes = "string avec guillements"
print(string_with_quotes)
print(string_with_double_quotes)

string_with_triples_quotes = """Bonjour
Premiere ligne
Deuxieme et dernière ligne"""
print("string_with_triples_quotes", string_with_triples_quotes)

string_with_double_quotes_bis = "Bonjour\nPremiere ligne\nDeuxieme et dernière ligne"
print("string_with_double_quotes_bis", string_with_double_quotes_bis)

print("\n" * 10)
int_not_string = 30
int_as_string = str(int_not_string)
print("type(int_not_string):", type(int_not_string), int_not_string)
print("type(int_as_string):", type(int_as_string), int_as_string)


new_float = 99.99
print("type(new_float):", type(new_float))

new_boolean = False
print(type(new_boolean))

# Concaténation de string
string_one = "J'ai lu"
string_two = "un livre"
string_three = string_one + " " + string_two
print(string_three)

# METHODES
print("\n" * 1)
var = "hello1 hello2 hello3"

# Première lettre en capital
print(var.capitalize())

# La 1ere lettre de chaque mot est en capital
print(var.title())

# Nombre de fois qu'apparait un terme (lettre ou mot)
print("'l' occurs:", var.count("l"), "times")

# String se terminant par o ou h
print("Ends with 'o':", var.endswith("o"))
print("Ends with 'h':", var.endswith("h"))

# String commençant par o ou h
print("Starts with 'o':", var.startswith("o"))
print("Starts with 'h':", var.startswith("h"))

# Test majuscules / minuscules
print("En minuscules:", var.islower())
print("En majuscules:", var.isupper())

# Transforme la string en majuscules / minuscules
print(var.upper())
print(var.lower())

# Change un charactère pour un autre
print(var.replace("o", "0"))
print(var.replace("l", "1"))

# Découpe une string en fonction d'un séparateur
print(var.split(" "))


new_string = "This is a new string"

# Mettre en maj
print(new_string.upper())
print(new_string)

# Nombre d'occurrences de "i"
print(new_string.count("i"))
# Nombre d'occurrences de "I"
print(new_string.count("I"))

# Majuscule sur les 1ères lettres de chaque mot
print(new_string.title())

# Remplacer les "s" par des $
print(new_string.replace("s", "$"))