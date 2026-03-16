# def welcome():
#     print("Hello World")

# welcome()

import os
import datetime

def OpenNotepad():
    os.system('notepad')

def GetDate():
    time = datetime.datetime.now()
    print(time)

def main():
    print("Welcome to my system")
    print("Select te following options to continue...")
    print("1. Notepad")
    print("2. Current Date/Time")
    choice = input("Enter choice 1/2: ")
    if choice == str(1):
        OpenNotepad()

    if choice == str(2):
        GetDate()

main()


