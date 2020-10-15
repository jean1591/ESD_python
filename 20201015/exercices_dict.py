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