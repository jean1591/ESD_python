# Clear terminal
import os
os.system("clear")

# Files
from finder import student_finder
print(student_finder())


# ===== ===== ===== =====
# ===== ===== ===== =====
str_1 = "a"
str_2 = "b"
# Si str_1 est égal "a" ET str_2 est égal à "b", affichez True
# Sinon affichez False
# Dans tous les cas, affichez "Done..."
if str_1 == "a" and str_2 == "b":
  print(True)
else:
  print(False)

print("Done...")


# ===== ===== ===== =====
# ===== ===== ===== =====
str_1 = "a"
str_2 = "b"
# Si str_1 est égal "a" OU str_2 est égal à "c", affichez True
# Sinon affichez False
if str_1 == "a" or str_2 == "c":
  print(True)
else:
  print(False)


# ===== ===== ===== =====
# ===== ===== ===== =====
age = 50
if age > 40 and age < 45:
    print("40/44 ans")
elif age > 40 and age <= 50:
    print("45+ ans")
elif age > 30:
  print("30 ans")
elif age > 20:
  print("20 ans")
