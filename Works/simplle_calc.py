import customtkinter
from customtkinter import *



container = customtkinter.CTk()
container.geometry("400x400+500+100")
container.title("Calculator")

header = customtkinter.CTkFrame(container, width=400, height=60, fg_color="grey", corner_radius=0)
header.place(relx=0, rely=0 )

headingLabel = customtkinter.CTkFrame(header, text= "Simple Calculator", text_color="black", corner_radius=0)
headingLabel.place(relx=0.02, rely=0.5 )

# Entries`

SellingEntry = customtkinter.CTkFrame(container, color= "white", text_color= "black", width=300, placeholder_text="COST PRICE", corner_radius=10, fg_color= "white", border_color='white')
SellingEntry.place(relx=0.1, rely=0.25)

button = customtkinter.CTkButton(container, text= "CALCULATE" font = ("Montserrat", 16)
button.place(relx=0.1, rely=0.55)

costPEntry = customtkinter.CTkEntry(container, text= "COST PRICE" cv )



container.mainloop()