# money = input("Enter Amount: ")
# money = float(money)
# print(type(money))


# username = input("Enter Username: ")
# password = input("Enter Password: ")

# if(username and password):
#     print("Welcome")

# elif(username and not password):
#     print("No password")

# elif(password and not username):
#     print("No username")

# elif not(username and password):
#     print("No username and password")


database = ["Lauren", "1234"]

email = input("Email: ")
password = input("Password: ")

#authentication

email = email.lower()
if email == database[0] and password == database[1]:
    print("Welcome")

else:
    print("Email or Password are incorrect")