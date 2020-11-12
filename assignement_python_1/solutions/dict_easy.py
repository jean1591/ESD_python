products_easy = {
   "smartphone": 1000,
   "laptop": 300
}

#
print(products_easy["smartphone"])

#
products_easy.update({"watch": 2000})
# OU
# products_easy["watch"] = 2000

#
products_easy.update({"laptop": 4000})
# OU
# products_easy["laptop"] = 4000

print(products_easy)