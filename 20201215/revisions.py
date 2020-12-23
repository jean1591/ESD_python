from random import randint

# Template String
first_name = "Jean"

print("Je m'appelle " + first_name.upper() + " Bonjour")


print(f"Je m'appelle {first_name} Bonjour")
print(f"Je m'appelle {first_name.upper()} Bonjour")


age = 29
city = "Bordeaux"
# Je m'appelle Jean, j'ai 29 ans, j'habite à Bordeaux. True si city == "Bordeaux"
print(f"Je m'appelle {first_name}, j'ai {age} ans, j'habite à {city}. {city == 'Bordeaux'}")
print(f"Je m'appelle {first_name}, j'ai {age} ans, j'habite à {city}. {city == 'Talence'}")
print(f"Je m'appelle {first_name}, j'ai {age} ans, j'habite à {city}. {'> 30' if age > 30 else '< 30'}")
print(f"Je m'appelle {first_name}, j'ai {randint(20, 100)} ans, j'habite à {city}. {'> 30' if randint(20, 100) > 30 else '< 30'}")


for i in range(10):
  # print("J'ai " + str(i) + " ans")
  print(f"J'ai {i} ans")