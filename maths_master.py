# Classess Importing
from customtkinter import *
from PIL import Image, ImageTk

# Creates Window
root = CTk()
root.title("Maths Master")
appWidth, appHeight = 500, 500
set_appearance_mode("dark")
set_default_color_theme("blue")

# Sets Menu's Top Frame
menu_top_frame = CTkFrame(master=root, width=500, height=120)
menu_top_frame.grid(row=0, column=0)

# Main & Subheading Labels
menu_heading_text = "Math's Master: Basic Facts Quiz"
main_heading = CTkLabel(master=menu_top_frame, text=menu_heading_text,
                        font=("Raleway", "20", "bold"), fg="white",
                        width=30)
main_heading.pack(pady=(10, 0))

menu_subheading_text = "Test your maths knowledge by choosing a basic facts challenge!"
subheading = CTkLabel(master=menu_top_frame, text=menu_subheading_text,
                      font=("Raleway", "10"), fg="white",
                      width=80)
subheading.pack(pady=(10, 0))

# Quiz Choice (Row 2-3)

# ++++++++++ Addition Button ++++++++++

# Addition Button Link
def addition_button_clicked(event):
    '''Testing Button'''
    print("Addition Button clicked!")

# Creates Canvas Widget
canvas_addition = CTkCanvas(root, width=80, height=80, bg='#242424', highlightthickness=0)
canvas_addition.grid(row=1, column=0)

# Adds/Resize Operator Image
add_image = Image.open("C:/Users/Marc/Downloads/Maths Master/images/addition.png")
add_image = add_image.resize((70, 70))
add_addition_image = ImageTk.PhotoImage(add_image)

# Places & Sets Command
addition_button = canvas_addition.create_image(40, 40, image=add_addition_image)
canvas_addition.tag_bind(addition_button, "<Button>", addition_button_clicked)


# ---------- Subtraction Button ----------

# Subtraction Button Link
def subtraction_button_clicked(event):
    '''Testing Button'''
    print("Subtraction Button clicked!")

# Creates Canvas Widget
canvas_subtraction = CTkCanvas(root, width=80, height=80, bg='#242424', highlightthickness=0)
canvas_subtraction.grid(row=2, column=0)

# Adds/Resize Operator Image
subtract_image = Image.open("C:/Users/Marc/Downloads/Maths Master/images/subtraction.png")
subtract_image = subtract_image.resize((70, 70))
add_subtraction_image = ImageTk.PhotoImage(subtract_image)

# Places & Sets Command
subtraction_button = canvas_subtraction.create_image(40, 40, image=add_subtraction_image)
canvas_subtraction.tag_bind(subtraction_button, "<Button>", subtraction_button_clicked)


# xxxxxxxxxx mult Button xxxxxxxxxx

# mult Button Link
def mult_button_clicked(event):
    '''Testing Button'''
    print("mult Button clicked!")

# Creates Canvas Widget
canvas_mult = CTkCanvas(root, width=80, height=80, bg='#242424', highlightthickness=0)
canvas_mult.grid(row=3, column=0)

# Adds/Resize Operator Image
mult_image = Image.open("C:/Users/Marc/Downloads/Maths Master/images/mult.png")
mult_image = mult_image.resize((70, 70))
add_mult_image = ImageTk.PhotoImage(mult_image)

# Places & Sets Command
mult_button = canvas_mult.create_image(40, 40, image=add_mult_image)
canvas_mult.tag_bind(mult_button, "<Button>", mult_button_clicked)


# Displays GUI
root.mainloop()
