USER_DATABASE = {
    'username' : 'admin',
    'password' : '3'
}

def login(username, password):
    if username == USER_DATABASE['username'] and password == USER_DATABASE['username']:
        return "login succesful"
    
    else:
        return "Wrong emial or password"


def main():
    username = input("Username: ")
    password = input("Password: ")
    email = input("Email: ")
    confirm_password = input("Confirm Password: ")
    master = login(username, password)
    print(master)

def register(email, password, username, confirm_password):
    if username and password and email and confirm_password:
        return "Enter all details"
    


main()