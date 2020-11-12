products_medium = {
  "smartphone": [1000, 16],
  "laptop": [4000, 0],
  "watch": [2000, 54]
}


#
print(products_medium["smartphone"][0])
print(products_medium["laptop"][1])

#
products_medium.update({"keyboard": [500, 72]})
# OU
# products_medium["keyboard"] = [500, 72]

#
products_medium["smartphone"][0] = 1500

#
if products_medium["laptop"][1] == 0:
  print("Out of Stock")
else:
  print(products_medium["laptop"][1])


print(products_medium)