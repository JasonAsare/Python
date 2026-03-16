import customtkinter
from customtkinter import *


def login(username,password):
    pass


root = CTk()
root.title("Login")
root.geometry("400x400")
root.resizable(width=0, height=0)

mainframe = CTkFrame(root, width=400, height=400, fg_color='white')
mainframe.place(relx=0, rely=0)

label = CTkLabel(mainframe, font=("Arial", 20), text='Welcome back')
label.place(relx=0.2, rely=0.1)
#login

usernameEntry = CTkEntry(mainframe, width=300, font=("Arial", 20), placeholder_text='Username')
usernameEntry.place(relx=0.12, rely=0.2)

passwordEntry = CTkEntry(mainframe, width=300, font=("Arial", 20), placeholder_text='Password', show='*')
passwordEntry.place(relx=0.12, rely=0.38)

submitButton = CTkButton(mainframe, width=300, font=("Arial", 20), text="Submit")
submitButton.place(relx= 0.12, rely=0.5)

root.mainloop()
