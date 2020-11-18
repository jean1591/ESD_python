order = {
	"user": {
		"name": "Four Product Order",
		"email": "four@example.com",
		"address": {
			"street_name": "141, Blvd Mortier",
			"postal_code": "75020",
			"city": "Paris",
			"country": "France"
		}
	},
	"order_details": {
		"order_id": "kdu6g479kdf4e9",
		"created_at": "2020-01-01",
		"paid": True,
		"delivered": False,
		"source": "somewebsite.com"
	},
	"products": [
		{
			"product_name": "iPhone",
			"product_id": "38y5fz4456789e",
			"quantity": 1,
			"price": 999
		},
		{
			"product_name": "Smart TV",
			"product_id": "83y5fz44yel899",
			"quantity": 1,
			"price": 1999
		},
		{
			"product_name": "HDMI Cable",
			"product_id": "j67ffzk7sel8f3",
			"quantity": 5,
			"price": 12
		},
		{
			"product_name": "Smart Watch",
			"product_id": "k0l33y5fz44y99",
			"quantity": 1,
			"price": 699
		}
	]
}


# Si vous n'y arriverez pas, retournez quelque chose dans tous les cas pour utiliser votre fonction
def impossible():
  return 0


def get_articles_nb(order):
  """Calculates number of ordered products

  Args:
      order (dict): Order passed

  Returns:
      int: Quantity of products
  """
  # Init res à 0 pour stocker qté
  res = 0

  # Parcours des différents produits
  for product in order["products"]:
    # Quantité stockée dans "quantity"
    # J'ajoute "quantity" à var res
    res += product["quantity"]
  
  # Retourne res
  return res


def get_articles_price(order):
  """Calculates total price

  Args:
      order (dict): Order passed

  Returns:
      int: Total price
  """
  # Init var res à 0 pour stocker prix total
  res = 0

  # Parcours des différents produits
  for product in order["products"]:
    # Quantité stockée dans "quantity"
    # Prix stocké dans "price"
    # J'ajoute quantity * price à var res
    res += product["price"] * product["quantity"]
  
  # Retourne res
  return res


""" def total_eng(order):
  res = 0
  for product in order["products"]:
    res += sum(product["engagements"].values())
  
  return res

print(total_eng(order)) """

def get_shipping_costs(total_price):
  """Calculates if shipping costs applies

  Args:
      total_price (int): Total price

  Returns:
      int: Value of shiiping costs
  """
  if total_price < 1000:
    return 30
  return 0

""" print(get_shipping_costs(50))
print(get_shipping_costs(1000)) """


def order_summary(order):
  # User
  print("User:", order["user"]["name"], "(", order["user"]["email"], ")")

  # Order
  print("Order Date:", order["order_details"]["created_at"])
  print("Order Status:")
  
  # Paid
  if order["order_details"]["paid"]:
    print("\t>> Paid")
  else:
    print("\t>> Not Paid")

  # Delivered
  if order["order_details"]["delivered"]:
    print("\t>> Delivered")
  else:
    print("\t>> Not Delivered")
  
  # Products
  print("Products:")
  for product in order["products"]:
    print("\t>>", product["product_name"], product["quantity"], "units x $", product["price"], "= $", product["quantity"] * product["price"])

  # Total
  total_price = get_articles_price(order)
  shipping_costs = get_shipping_costs(total_price)
  print("Total:")
  print("\t>> Products Quantity:", get_articles_nb(order))
  print("\t>> Products Price: $", total_price)
  print("\t>> Shipping Costs: $", shipping_costs)
  print("\t>> ORDER TOTAL: $", total_price + shipping_costs)



order_summary(order)