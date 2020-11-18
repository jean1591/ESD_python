from pprint import pprint

students = [
	{
		"email": "lucas@example.com",
		"marks": [ 18, 19, 15 ],
		"name": "lucas",
		"option": None
	},
	{
		"email": "raphael@example.com",
		"marks": [ 19, 20, 16 ],
		"name": "raphael",
		"option": None
	},
	{
		"email": "lucie@example.com",
		"marks": [ 18, 18, 16 ],
		"name": "lucie",
		"option": { "duration": 3, "name": "web" }
	},
	{
		"email": "arena@example.com",
		"marks": [ 15, 17, 18 ],
		"name": "arena",
		"option": None
	},
	{
		"email": "alexandre@example.com",
		"marks": [ 20, 20, 15 ],
		"name": "alexandre",
		"option": { "duration": 9, "name": "python" }
	},
	{
		"email": "marie@example.com",
		"marks": [ 18, 12, 17 ],
		"name": "marie",
		"option": { "duration": 10, "name": "data" }
	},
	{
		"email": "simon@example.com",
		"marks": [ 17, 18, 20 ],
		"name": "simon",
		"option": { "duration": 7, "name": "SEO" }
	},
	{
		"email": "mirana@example.com",
		"marks": [ 17, 17, 16 ],
		"name": "mirana",
		"option": None
	},
	{
		"email": "lilou@example.com",
		"marks": [ 19, 20, 20 ],
		"name": "lilou",
		"option": { "duration": 10, "name": "SEO" }
	},
	{
		"email": "yann@example.com",
		"marks": [ 14, 13, 14 ],
		"name": "yann",
		"option": { "duration": 10, "name": "UX" }
	},
	{
		"email": "lyvahne@example.com",
		"marks": [ 18, 20, 15 ],
		"name": "lyvahne",
		"option": { "duration": 9, "name": "UX" }
	}
]

""" # Affichez la liste des emails de tous les étudiants
for i in students:
  print(i["email"])

mailing = []
for i in students:
  mailing.append(i["email"])
print(mailing) """


# Pour chaque élève, calculez puis affichez sa moyenne
""" for student in students:
  total = 0
  # nb = 0
  for mark in student["marks"]:
    total += mark
    # nb += 1
  # print(student["name"], round(total / nb, 2))
  print(student["name"], round(total / len(student["marks"]), 2)) """

""" for student in students:
  print(student["name"], round(sum(student["marks"]) / len(student["marks"]), 2)) """

# Pour chaque élève, ajoutez la clef "avg_mean" qui prend pour valeur la moyenne de l'étudiant
""" for student in students:
  student["avg_mean"] = round(sum(student["marks"]) / len(student["marks"]), 2) """

# pprint(students)


# Pour les étudiants qui ont une option et uniquement pour ceux-la, affichez le nom du étudiant, le nom de l'option et sa durée  => `alexandre python 9`
""" for student in students:
  if student["option"]: # is not None:
    print(student["name"], student["option"]["name"], student["option"]["duration"]) """

  
# Pour les étudiants qui ont une option **et** qui ont au moins un 20 dans leur notes et uniquement pour ceux-la, affichez le nom du étudiant avec la string "is taking the hard way"  => `alexandre is taking the hard way`
""" for student in students:
  if student["option"] and 20 in student["marks"]:
    print(student["name"], "is taking the hard way") """