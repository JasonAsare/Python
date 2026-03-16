student = {
    'name': 'Jason Asare',
    'age': '13',
    'dob': '6th March, 2012'
}

# name = student['name']
# print(name)

# age = student.get('age')
# print(age)

# print(student.keys())
# print(student.values())

# student['Marital_status'] = 'Married'
# student['name']= 'Ekow Tamaklow'
# student.pop('age')
# print(student)
# # student.popitem()
# # print(student)

# del student['dob']
# print(student)

# for i in student:
#     print(i)

# for i in student.values():
#     print(i)

for x,y in student.items():
    print(f"{x}:{y}")