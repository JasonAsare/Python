students = ["Sam", "Lauren"]
name = input("Enter name: ")
for names in students:
    if name == names:
        print(names)
        break

# for numbers in range(101):
#     if numbers %2 == 0:
#         print(numbers)


# for numbers in range(101):
#     if numbers %2 == 0:
#         print(numbers)

# from math import pi, sqrt

# lenght = float(input("Enter lenght: "))
# GRAVITY = 9.81
# tension = 2 * pi * sqrt(lenght/GRAVITY)
# print(f"{tension:.2f}")