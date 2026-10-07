# Python Data Structures and Pandas Basics
# This file covers basic Python data types, collections, and DataFrame operations.
# Created By Jitendra Singh.

# 1. Numbers

age = 22
price = 499.50
complex_number = 3 + 4j

print(age)
print(price)
print(complex_number)

# Output:
# 22
# 499.5
# (3+4j)


# 2. Boolean Values

is_student = True
is_working = False

print(is_student)
print(is_working)

# Output:
# True
# False


# 3. None Value

result = None

print(result)

# Output:
# None


# 4. Checking Data Types

print(type(age))
print(type(price))
print(type(complex_number))
print(type(is_student))
print(type(result))

# Output:
# <class 'int'>
# <class 'float'>
# <class 'complex'>
# <class 'bool'>
# <class 'NoneType'>


# 5. Strings

name = "Jitendra"
course = "Data Science"

print(name)
print(course)

# Output:
# Jitendra
# Data Science


# 6. String Indexing

word = "Python"

print(word[0])
print(word[1])
print(word[-1])

# Output:
# P
# y
# n


# 7. String Slicing

word = "Python"

print(word[0:3])
print(word[2:6])
print(word[:4])
print(word[2:])
print(word[::-1])

# Output:
# Pyt
# thon
# Pyth
# thon
# nohtyP


# 8. String Methods

text = "data science"

print(text.upper())
print(text.lower())
print(text.title())
print(text.replace("data", "python"))
print(text.count("a"))

# Output:
# DATA SCIENCE
# data science
# Data Science
# python science
# 2


# 9. String Concatenation

first_name = "Jitendra"
last_name = "Singh"

full_name = first_name + " " + last_name

print(full_name)

# Output:
# Jitendra Singh


# 10. String Formatting

name = "Jitendra"
skill = "Python"

message = f"My name is {name} and I am learning {skill}."

print(message)

# Output:
# My name is Jitendra and I am learning Python.


# 11. Lists

marks = [78, 85, 91, 67, 88]

print(marks)

# Output:
# [78, 85, 91, 67, 88]


# 12. List Indexing

marks = [78, 85, 91, 67, 88]

print(marks[0])
print(marks[2])
print(marks[-1])

# Output:
# 78
# 91
# 88


# 13. List Slicing

marks = [78, 85, 91, 67, 88]

print(marks[1:4])
print(marks[:3])
print(marks[2:])
print(marks[::-1])

# Output:
# [85, 91, 67]
# [78, 85, 91]
# [91, 67, 88]
# [88, 67, 91, 85, 78]


# 14. Adding Items to a List

skills = ["Python", "SQL"]

skills.append("Power BI")

print(skills)

# Output:
# ['Python', 'SQL', 'Power BI']


# 15. Sorting a List

marks = [78, 45, 92, 67, 85]

marks.sort()

print(marks)

# Output:
# [45, 67, 78, 85, 92]


# 16. Finding an Item Position

skills = ["Python", "SQL", "Excel", "Power BI"]

print(skills.index("Excel"))

# Output:
# 2


# 17. Selecting Multiple List Items

skills = ["Python", "SQL", "Excel", "Power BI"]

print(skills[1:3])

# Output:
# ['SQL', 'Excel']


# 18. Deleting an Item from a List

skills = ["Python", "SQL", "Excel", "Power BI"]

del skills[2]

print(skills)

# Output:
# ['Python', 'SQL', 'Power BI']


# 19. Updating a List Item

skills = ["Python", "SQL", "Excel"]

skills[1] = "PostgreSQL"

print(skills)

# Output:
# ['Python', 'PostgreSQL', 'Excel']


# 20. List Operations

numbers = [1, 2, 3]

print(numbers + [4, 5])
print(numbers * 2)

# Output:
# [1, 2, 3, 4, 5]
# [1, 2, 3, 1, 2, 3]


# 21. Nested Lists

student_data = [
    ["Amit", 85],
    ["Rahul", 90],
    ["Neha", 88]
]

print(student_data[0])
print(student_data[1][1])

# Output:
# ['Amit', 85]
# 90


# 22. List Unpacking

student = ["Jitendra", 22, "BCA"]

name, age, degree = student

print(name)
print(age)
print(degree)

# Output:
# Jitendra
# 22
# BCA


# 23. Tuples

languages = ("Python", "SQL", "Excel")

print(languages)

# Output:
# ('Python', 'SQL', 'Excel')


# 24. Tuple Indexing

languages = ("Python", "SQL", "Excel")

print(languages[0])
print(languages[-1])

# Output:
# Python
# Excel


# 25. Tuple Slicing

languages = ("Python", "SQL", "Excel", "Power BI")

print(languages[1:3])

# Output:
# ('SQL', 'Excel')


# 26. Tuple Length

languages = ("Python", "SQL", "Excel", "Power BI")

print(len(languages))

# Output:
# 4


# 27. Tuple Packing

skills = "Python", "SQL", "Power BI"

print(skills)
print(type(skills))

# Output:
# ('Python', 'SQL', 'Power BI')
# <class 'tuple'>


# 28. Tuple Unpacking

skills = ("Python", "SQL", "Power BI")

skill1, skill2, skill3 = skills

print(skill1)
print(skill2)
print(skill3)

# Output:
# Python
# SQL
# Power BI


# 29. Tuple Immutability

languages = ("Python", "SQL", "Excel")

try:
    languages[1] = "Pandas"
except TypeError as error:
    print(error)

# Output:
# 'tuple' object does not support item assignment


# 30. Dictionaries

student = {
    "name": "Jitendra",
    "age": 22,
    "degree": "BCA",
    "skill": "Python"
}

print(student)

# Output:
# {'name': 'Jitendra', 'age': 22, 'degree': 'BCA', 'skill': 'Python'}


# 31. Dictionary Access

student = {
    "name": "Jitendra",
    "age": 22,
    "degree": "BCA"
}

print(student["name"])
print(student["degree"])

# Output:
# Jitendra
# BCA


# 32. Dictionary Keys

student = {
    "name": "Jitendra",
    "age": 22,
    "degree": "BCA"
}

print(student.keys())

# Output:
# dict_keys(['name', 'age', 'degree'])


# 33. Dictionary Values

student = {
    "name": "Jitendra",
    "age": 22,
    "degree": "BCA"
}

print(student.values())

# Output:
# dict_values(['Jitendra', 22, 'BCA'])


# 34. Dictionary Length

student = {
    "name": "Jitendra",
    "age": 22,
    "degree": "BCA"
}

print(len(student))

# Output:
# 3


# 35. Updating a Dictionary Value

student = {
    "name": "Jitendra",
    "age": 22
}

student["age"] = 23

print(student)

# Output:
# {'name': 'Jitendra', 'age': 23}


# 36. Adding a New Dictionary Item

student = {
    "name": "Jitendra",
    "age": 22
}

student["skill"] = "Python"

print(student)

# Output:
# {'name': 'Jitendra', 'age': 22, 'skill': 'Python'}


# 37. Deleting a Dictionary Item

student = {
    "name": "Jitendra",
    "age": 22,
    "skill": "Python"
}

del student["age"]

print(student)

# Output:
# {'name': 'Jitendra', 'skill': 'Python'}


# 38. Dictionary Items

student = {
    "name": "Jitendra",
    "age": 22,
    "skill": "Python"
}

print(student.items())

# Output:
# dict_items([('name', 'Jitendra'), ('age', 22), ('skill', 'Python')])


# 39. Loop Through a Dictionary

student = {
    "name": "Jitendra",
    "age": 22,
    "skill": "Python"
}

for key, value in student.items():
    print(key, ":", value)

# Output:
# name : Jitendra
# age : 22
# skill : Python


# 40. Nested Dictionary

students = {
    "student_1": {
        "name": "Amit",
        "marks": 85
    },
    "student_2": {
        "name": "Neha",
        "marks": 92
    }
}

print(students["student_1"]["name"])
print(students["student_2"]["marks"])

# Output:
# Amit
# 92


# 41. List of Dictionaries

students = [
    {"name": "Amit", "marks": 85},
    {"name": "Neha", "marks": 92},
    {"name": "Rahul", "marks": 78}
]

print(students[0])
print(students[1]["name"])

# Output:
# {'name': 'Amit', 'marks': 85}
# Neha


# 42. Sets

skills = {"Python", "SQL", "Excel"}

print(skills)

# Output:
# {'Python', 'SQL', 'Excel'}

# Note:
# Set order can be different because sets are unordered.


# 43. Creating an Empty Set

empty_set = set()

print(empty_set)
print(type(empty_set))

# Output:
# set()
# <class 'set'>


# 44. Set Membership

skills = {"Python", "SQL", "Excel"}

print("Python" in skills)
print("Java" in skills)

# Output:
# True
# False


# 45. Adding an Item to a Set

skills = {"Python", "SQL"}

skills.add("Power BI")

print(skills)

# Output:
# {'Python', 'SQL', 'Power BI'}


# 46. Duplicate Values in a Set

numbers = {10, 20, 20, 30, 30}

print(numbers)

# Output:
# {10, 20, 30}


# 47. Removing an Item from a Set

skills = {"Python", "SQL", "Excel"}

skills.remove("SQL")

print(skills)

# Output:
# {'Python', 'Excel'}


# 48. Set Union

python_skills = {"Python", "Pandas"}
sql_skills = {"SQL", "PostgreSQL"}

print(python_skills | sql_skills)

# Output:
# {'Python', 'Pandas', 'SQL', 'PostgreSQL'}


# 49. Set Intersection

required_skills = {"Python", "SQL", "Excel"}
known_skills = {"Python", "SQL", "Power BI"}

print(required_skills & known_skills)

# Output:
# {'Python', 'SQL'}


# 50. Set Difference

required_skills = {"Python", "SQL", "Excel"}
known_skills = {"Python", "SQL", "Power BI"}

print(required_skills - known_skills)

# Output:
# {'Excel'}


# 51. Range

numbers = range(1, 6)

print(list(numbers))

# Output:
# [1, 2, 3, 4, 5]


# 52. Bytes

data = b"Python"

print(data)
print(type(data))

# Output:
# b'Python'
# <class 'bytes'>


# 53. Type Conversion

number = "100"

integer_number = int(number)
decimal_number = float(number)

print(integer_number)
print(decimal_number)

# Output:
# 100
# 100.0


# 54. List Comprehension

numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers]

print(squares)

# Output:
# [1, 4, 9, 16, 25]


# 55. Set Comprehension

numbers = [1, 2, 2, 3, 3, 4]

squares = {number ** 2 for number in numbers}

print(squares)

# Output:
# {1, 4, 9, 16}


# 56. Dictionary Comprehension

numbers = [1, 2, 3, 4]

squares = {number: number ** 2 for number in numbers}

print(squares)

# Output:
# {1: 1, 2: 4, 3: 9, 4: 16}


# 57. Mutable List

sales = [100, 200, 300]

sales[0] = 500

print(sales)

# Output:
# [500, 200, 300]


# 58. Immutable Tuple

sales = (100, 200, 300)

try:
    sales[0] = 500
except TypeError as error:
    print(error)

# Output:
# 'tuple' object does not support item assignment


# 59. Practical Data Science List

product_names = [
    "Laptop",
    "Mouse",
    "Keyboard",
    "Monitor"
]

prices = [
    55000,
    800,
    1500,
    12000
]

print(product_names)
print(prices)

# Output:
# ['Laptop', 'Mouse', 'Keyboard', 'Monitor']
# [55000, 800, 1500, 12000]


# 60. Pandas Introduction

import pandas as pd

print(pd.__version__)

# Output:
# Your installed Pandas version will be displayed.


# 61. Creating DataFrame from a Dictionary

data = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor"],
    "Price": [55000, 800, 1500, 12000],
    "Quantity": [5, 20, 15, 8]
}

df = pd.DataFrame(data)

print(df)

# Output:
#     Product  Price  Quantity
# 0    Laptop  55000         5
# 1     Mouse    800        20
# 2  Keyboard   1500        15
# 3   Monitor  12000         8


# 62. Selecting One DataFrame Column

print(df["Product"])

# Output:
# 0      Laptop
# 1       Mouse
# 2    Keyboard
# 3     Monitor
# Name: Product, dtype: object


# 63. Selecting Multiple DataFrame Columns

print(df[["Product", "Price"]])

# Output:
#     Product  Price
# 0    Laptop  55000
# 1     Mouse    800
# 2  Keyboard   1500
# 3   Monitor  12000


# 64. Selecting the First Rows

print(df.head(2))

# Output:
#   Product  Price  Quantity
# 0  Laptop  55000         5
# 1   Mouse    800        20


# 65. Selecting DataFrame Rows by Position

print(df.iloc[0])
print(df.iloc[1])

# Output:
# Product     Laptop
# Price        55000
# Quantity         5
# Name: 0, dtype: object
#
# Product     Mouse
# Price         800
# Quantity       20
# Name: 1, dtype: object
