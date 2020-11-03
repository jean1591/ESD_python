import datetime
from random import randint, choice
from os import system

system("clear")


""" {
  "name": "alfred",
  "email": "alfred@example.com",
  "last_payment": "2020-01-01",
  "program": "premium",
  "last_session": "2020-10-15",
  "sponsorship": False,
  "location": "sydney"
} """


names = ["Lucas", "Raphael", "Lucie", "Arena", "Alexandre", "Marie", "Simon", "Mirana", "Lilou", "Yann", "Lyvahne"]
domains = ["gmail.com", "example.com", "outlook.com", "mailo.com"]
programs = ["basic", "premium"]
locations = ["sydney", "camberra", "perth", "darwin"]

db = []

















# Random name
tmp_name = choice(names)

# Random email
tmp_email = tmp_name + "@example.com"

# Random last payment date
# Generate random date between two bounds
start_date = datetime.date(2020, 1, 1)
end_date = datetime.date(2020, 12, 31)

time_between_dates = end_date - start_date
days_between_dates = time_between_dates.days
random_number_of_days = randint(0, days_between_dates)
""" print("time_between_dates", time_between_dates)
print("days_between_dates", days_between_dates)
print("random_number_of_days", random_number_of_days) """

tmp_last_payment = start_date + datetime.timedelta(days=random_number_of_days)

random_number_of_days = randint(0, days_between_dates)
# print("random_number_of_days", random_number_of_days)
tmp_last_session = start_date + datetime.timedelta(days=random_number_of_days)


tmp_name = choice(names)
tmp = {
  "name": tmp_name.lower(),
  "email": tmp_name.lower() + "@" + choice(domains),
  "last_payment": tmp_last_payment.strftime("%Y-%m-%d"),
  "last_session": tmp_last_session.strftime("%Y-%m-%d"),
  "program": choice(programs),
  "sponsorship": choice([True, False]),
  "location": choice(locations)
}

print(tmp)