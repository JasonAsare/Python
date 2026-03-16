import customtkinter
from customtkinter import *

def destroy():
    window.destroy()

window = customtkinter.CTk()
window.geometry("400x400+500+100")
window.title("My First App")
window.resizable(0,0)

customtkinter.set_appearance_mode('dark')

# frame
navigationFrame = customtkinter.CTkFrame(window, width=400, height=60, fg_color='blue', corner_radius=0)
navigationFrame.pack()

button = customtkinter.CTkButton(window, text="close x", text_color='white', fg_color='red', command=destroy)
# button.place(x=10, y=0)
button.place(relx = 0.4, rely = 0.5)


window.mainloop()