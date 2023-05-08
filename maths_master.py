# Classess Importing
from tkinter import *
'''GUI Python Module'''

from customtkinter import *
'''GUI Module With Extensive Features'''


# Creates Window
root = CTk()
root.title("Maths Master")
appWidth, appHeight = 500, 500
set_appearance_mode("dark")
set_default_color_theme("green")

# Main & Subheading (Row 0-1)
main_heading = Label(text="Maths Master: Basic Facts Quiz",
                     font=("Raleway", "20", "bold"), bg="#242526", fg="white",
                     width="30")
main_heading.grid(row=0, column=0, pady=(10, 0))

subheading = Label(text="Test your maths knowledge through choosing a basic facts challenge!",
                   font=("Raleway", "10"), bg="#242526", fg="white",
                   width="80")
subheading.grid(row=1, column=0, pady=(10, 0))

# Quiz Choice (Row 2-3)


button1 = CTkButton(root, text="Gaming")
button1.grid()

# Displays GUI
root.mainloop()
