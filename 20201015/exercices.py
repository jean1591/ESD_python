# STRING
# Screen Display
print("ESD")

# COMMENTS
# Ceci est un commentaire

# THIS YEAR
year = 1991
age = 29
this_year = year + age
print(this_year)

# SCORE
score = 17.5
max_score = 20
diff_to_max = max_score - score
print(diff_to_max)

# CHECKED / UNCHECKED
checked = True
print(checked)
pas_checked = not checked
print(pas_checked)

# MULTIPLY TWO INT
n1 = 89
n2 = 34
print("Le produit de n1 par n2:", n1 * n2)

# MULTIPLY TWO FLOAT
n1 = 33.3
n2 = 11.1
produit = n1 * n2
print(produit)

# HELLO WORLD!
hello = "Hello World!"
print(hello)

# STRING WITH '
here = 'I\'m here'
print(here)

# STRING WITH "
she = "She said: \"OK\""
print(she)

# STRING WITH """
long_string = """Hello, this is a
multiline string with "double quotes" and 'single quotes'"""
print(long_string)

print(here, "\n", she, "\n", long_string)


# STRING TO INT & SUM
s1 = "89"
s2 = "34"
s1 = int(s1)
s2 = int(s2)
print(s1 + s2)

# METHODS
var = "Am I in lowercase ?" # Commentaire
var.islower()

var = "Ends with i"
var.endswith("i")

var = "I Should be uppercase"
var.upper()

var = "Oh wow"
var.count("w")

var = "Oh wow"
var.replace("w", "t")


var = "Hello World"

print(var[2:4])

var = "Bienvenue à l'ESD"
# Afficher "Bienvenue"
print(var[0:9], var[:9])
print(var[14:17], var[14:])
print(var[4])
# Afficher "ESD"