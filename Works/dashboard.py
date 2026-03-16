import customtkinter
from customtkinter import *
import datetime
from datetime import *

# def time():
#     current_time = datetime.strftime("%H:%M")
#     timer.configure(text=current_time)


def logic():
    pass

def main():
    window = CTk()
    window.geometry("1200x760")
    set_appearance_mode('white')
    window.title("Quatum core")
    window.resizable(width=0, height=0)

    #horizontal nav
    navigation = CTkFrame(window, width=1200, height=60, fg_color='darkblue', corner_radius=0)
    navigation.place(relx=0, rely=0)
    textlogo = CTkLabel(navigation, text="Quatum", text_color='white', font=("Arial", 20, 'bold'))
    textlogo.place(relx=0.01, rely=0.3)
    textlogo2 = CTkLabel(navigation, text="Core", text_color='cyan', font=("Arial", 22, 'bold'))
    textlogo2.place(relx=0.091,rely=0.29)

    #time
    timer = CTkLabel(navigation, text=datetime.now(), text_color='white', font=("Arial", 20, 'bold'))
    timer.place(relx=0.7, rely=0.3)

    #Side Nav
    sidbar = CTkFrame(window, width=200, height=700, corner_radius=0)
    sidbar.place(relx=0, rely=0.0815)

    #cards
    card1 = CTkFrame(window, width=150, height=250, fg_color='darkblue')
    card1.place(rely=0.1, relx=2)

    # card2 = CTkFrame(window, width=150, height=250, fg_color='darkblue')
    # card2.place(rely=0.1, relx=2)
    #
    # card3 = CTkFrame(window, width=150, height=250, fg_color='darkblue')
    # card3.place(rely=0.1, relx=2)

    window.mainloop()

main()

