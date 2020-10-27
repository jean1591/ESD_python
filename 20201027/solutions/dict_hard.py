from pprint import pprint
import os

os.system("clear")


products_hard = {
  "smartphone": {
    "price": 1500,
    "quantity": 16,
    "components": {
      "screen": "4K Gorilla Glass",
      "CPU": "High Efficiency CPU",
      "GPU": "High Efficiency GPU"
    },
    "tags": ["tech", "smartphone"],
    "in_stock": True
  },
  "laptop": {
    "price": 4000,
    "quantity": 0,
    "components": {
      "screen": "27in 8K",
      "CPU": "Best Tech CPU",
      "GPU": "Best Tech GPU"
    },
    "tags": ["tech", "computer"],
    "in_stock": True
  }, "watch": {
    "price": 2000,
    "quantity": 54,
    "components": {
      "screen": "Small Screen Inc.",
      "CPU": "Downsize CPU",
      "GPU": "Downsize GPU"
    },
    "in_stock": True
  }
}

#
print(products_hard["smartphone"]["price"])
print(products_hard["laptop"]["quantity"])
print(products_hard["watch"]["components"])
print(products_hard["laptop"]["tags"])

#
products_hard.update({"keyboard": {}})
# OU
# products_hard["keyboard"] = {}

products_hard["keyboard"].update({"price": 500})
products_hard["keyboard"].update({"quantity": 72})
# OU
# products_hard["keyboard"]["price"] = 500
# products_hard["keyboard"]["quantity"] = 72

products_hard["keyboard"].update({"components": {}})
# OU
# products_hard["keyboard"]["components"] = {}

products_hard["watch"].update({"tags": ["tech", "smartwatch", "iot"]})
# OU
# products_hard["watch"]["tags"] = ["tech", "smartwatch", "iot"]

products_hard["laptop"]["tags"].append("iot")

#
products_hard["watch"]["components"].update({"screen": "Little Screen Corp."})
# OU
# products_hard["watch"]["components"]["screen"] = "Little Screen Corp."
products_hard["laptop"].update({"in_stock": False})
# OU
# products_hard["laptop"]["in_stock"] = False

for p in products_hard:
  print(p, ": €", products_hard[p]["price"], ",", products_hard[p]["quantity"], "units")