from pprint import pprint
import random

students_list = ["Lucas", "Raphael", "Lucie", "Arena", "Alexandre", "Marie", "Simon", "Mirana", "Lilou", "Yann", "Lyvahne"]

options = ["python", "web", "SEO", "UX", "data"]

students_list_complex = [
  {"name": name.lower(),
  "email": f"{name.lower()}@example.com",
  "marks": [random.randint(12, 20) for i in range(3)],
  "option": {"name": random.choice(options), "duration": random.randint(3, 10)} if random.choice([True, False]) else None
} for name in students_list]



"""
# A EXPLIQUER EN COURS

students_list_complex = []

for student in students_list:
  # Liste de notes - Initialisée vide
  marks = []
  for i in range(3): # Ajoute 3 notes dans marks
    marks.append(random.randint(10, 20))
  # Ajoute un dict par student dans students_list_complex
  students_list_complex.append({"name": student.lower(), "email": f"{student.lower()}@example.com", "marks": marks})
 """


pprint(students_list_complex)