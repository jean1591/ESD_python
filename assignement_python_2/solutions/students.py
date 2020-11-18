from random import choice, randint


# Email Generator
def create_email_address(name):
  """Create email address from name

  Args:
      name (string): Name to generate an email address from

  Returns:
      string: Full email address
  """
  return name + "@example.com"

""" print(create_email_address("jean"))
print(create_email_address("alexandre"))
print(create_email_address("marie")) """


# Option Generator
def create_option(options, durations):
  """Create option from options list and durations list

  Args:
      options (list): Options list
      durations (list): Durations list

  Returns:
      dict: Option generated randomly
  """
  return {"name": choice(options), "duration": choice(durations)}

""" option_dm = ["python", "web", "UX", "data"]
option_ds = ["python", "regression", "ml", "dl"]
duration_list = [1, 2, 3, 4]
print(create_option(option_dm, duration_list))
print(create_option(option_ds, duration_list))
print(create_option(option_dm, duration_list)) """


# Marks Generator
def create_marks(n):
  """Generate n marks

  Args:
      n (int): Number of marks to be generated

  Returns:
      list: List of n marks
  """
  marks = []
  for i in range(n):
    marks.append(randint(0, 20))

  return marks

def create_marks_bis(n):
  return [randint(0, 20) for i in range(n)]

""" print(create_marks_bis(2))
print(create_marks_bis(3))
print(create_marks_bis(6)) """


# Student Generator
def generate_student(name, options, durations, marks_nb):
  """Generate a student given its name, some options and durations list and a number of marks

  Args:
      name (string): Student name
      options (list): Options list
      durations (list): Durations list
      marks_nb (int): Number of marks to be generated

  Returns:
      dict: Student with specified keys: values
  """

  return {
    "name": name,
    "email": create_email_address(name),
    "marks": create_marks(marks_nb),
    "option": create_option(options, durations)
  }


""" option_dm = ["python", "web", "UX", "data"]
option_ds = ["python", "regression", "ml", "dl"]
duration_list = [1, 2, 3, 4]
print(generate_student("hubert_1", option_dm, duration_list, 3))
print(generate_student("hubert_2", option_ds, duration_list, 10))
print(generate_student("hubert_3", option_dm, duration_list, 7)) """