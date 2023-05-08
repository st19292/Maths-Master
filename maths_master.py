# Classess Importing
from tkinter import *
'''GUI Python Module'''

from customtkinter import *
'''GUI Module With Extensive Features'''

from PIL import Image, ImageTk
'''GUI Images Added'''


# Creates Window
root = CTk()
root.title("Maths Master")
appWidth, appHeight = 500, 500
set_appearance_mode("dark")
set_default_color_theme("green")

frame = CTkFrame(master=root, width=500, height=80)
frame.grid()

# Main & Subheading (Row 0-1)
main_heading = Label(frame, text="Maths Master: Basic Facts Quiz",
                     font=("Raleway", "20", "bold"), bg="#2B2B2B", fg="white",
                     width="30")
main_heading.grid(row=0, column=0, pady=(10, 0))

subheading = Label(frame, text="Test your maths knowledge through choosing a basic facts challenge!",
                   font=("Raleway", "10"), bg="#2B2B2B", fg="white",
                   width="80")
subheading.grid(row=1, column=0, pady=(10, 0))


# Quiz Choice (Row 2-3)
add_addition_image = ImageTk.PhotoImage(Image.open("images/addition.png"), Image.ANTIALIAS)
add_button = CTkButton(master=root, image=add_addition_image, compound="left")
add_button.grid()

# Displays GUI
root.mainloop()
