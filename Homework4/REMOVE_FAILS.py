students = {
    'Henry': 42,
    'Ani': 96,
    'Artur': 95,
    'Malena': 75,
    'Leo': 35
}
# without creating new dictionary

for key in list(students.keys()):
    if students[key] <= 60:
        del students[key]

print(students)

# by creating new dictionary
students = {key: value for key, value in students.items() if value >= 60}

print(students)
