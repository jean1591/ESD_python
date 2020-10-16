my_dict = {
  "name": "Bob",
  "age": 30,
  "lst": [1, 2, 3],
  "address": {
    "streetNb": 44,
    "streetName": "Lilas"
  },
  "email": {
    "provider": ["gmail", "outlook", "example"],
    "extension": ".com"
  },
  "mailing": [
    "r@example.com",
    "a@example.com",
    "m@example.com",
  ]
}

print(my_dict["name"])
print(my_dict["lst"])
print(my_dict["address"]["streetNb"])
print(my_dict["email"]["provider"][1])
print(my_dict["mailing"][1])


# Déclaration de dict
empty_dict = {}
dict_num = {"un": 1, "deux": 2, "trois": 3}

# Méthodes sur les dict
print(dict_num.keys())
print(dict_num.values())

# Accès aux éléments
print(dict_num["deux"])


my_dict = {
  "name": "Bob",
  "age": 30,
  "lst": [1, 2, 3],
  "address": {
    "streetNb": 44,
    "streetName": "Lilas"
  },
  "email": {
    "provider": ["gmail", "outlook", "example"],
    "extension": ".com"
  },
  "mailing": [
    "r@example.com",
    "a@example.com",
    "m@example.com",
  ]
}

# Accédez au dernier élément de "mailing"
print(my_dict["mailing"][2]) # Via index positif
print(my_dict["mailing"][-1]) # Via index négatif

# Ajoutez un "l@example.com" à mailing
my_dict["mailing"].append("l@example.com")
print(my_dict["mailing"])
# Ajoutez un "4" à lst
my_dict["lst"].append(4)
print(my_dict["lst"])

# Changez "name" pour "Alice"
my_dict["name"] = "Alice"
print(my_dict["name"])

# Type de "address"
print(type(my_dict["address"]))

# Ajouter la clef "is_log" à my_dict avec pour valeur True
# my_dict["is_log"] = True
# my_dict.update({"is_log": True, "name": "Jean"}) # Update and add new key
my_dict.update({"is_log": True})
print(my_dict["is_log"])

# Ajoutez la clef "city" à "address" avec pour valeur "Bordeaux"
# my_dict["address"]["city"] = "Bordeaux"
my_dict["address"].update({"city": "Bordeaux"})
print(my_dict["address"])

# Supprimez tous les "provider" puis ajoutez "mailo"
my_dict["email"]["provider"].clear()
my_dict["email"]["provider"].append("mailo")
print(my_dict["email"]["provider"])

# Incrémetez "age" de 30
my_dict["age"] += 30
print(my_dict["age"])