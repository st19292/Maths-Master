# Classess Importing
from tkinter import *
'''GUI Python Module'''

from PIL import Image, ImageTk
'''GUI Images Added'''


# Creates Window
root = Tk()
root.title("Maths Master")
appWidth, appHeight = 500, 500
root.configure(bg='#242424',)


# Sets Top Proximity, Primary Headers
menu_top_frame = Frame(master=root, width=500, height=120, bg="#2B2B2B")
menu_top_frame.grid(row=0, column=0)

# Main & Subheading Labels
menu_heading_text = "Math's Master: Basic Facts Quiz"
main_heading = Label(master=menu_top_frame, text=menu_heading_text,
                        font=("Raleway", "20", "bold"), bg="#2B2B2B", fg="white",
                        width=30)
main_heading.pack(pady=(10, 0))

menu_subheading_text = "Test your maths knowledge by choosing a basic facts challenge!"
subheading = Label(master=menu_top_frame, text=menu_subheading_text,
                      font=("Raleway", "10"), bg="#2B2B2B", fg="white",
                      width=80)
subheading.pack(pady=(10, 0))


# Quiz Choice (Row 2-3)

# Sets Middle Proximity, Operator Buttons
button_frame = Frame(root, bg='#242424', padx=10, pady=40)
button_frame.grid(row=1, column=0, rowspan=4)

# ++++++++++ Addition Button ++++++++++

# Addition Button Link
def addition_button_clicked(event):
    '''Testing Button'''
    print("Addition Button clicked!")

# Creates Canvas Widget
canvas_addition = Canvas(master=button_frame, width=80, height=80, bg='#242424', highlightthickness=0)
canvas_addition.grid(row=1, column=0)

# Adds/Resize Operator Image
addition_image = Image.open("C:/Users/Marc/Downloads/Maths Master/images/addition.png")
addition_image = addition_image.resize((70, 70))
add_addition_image = ImageTk.PhotoImage(addition_image)

# Addition Text
addition_text = Label(master=button_frame, text="Addition",
                      font=("Raleway", "10"), bg="#242424", fg="white",
                      width=10)
addition_text.grid(row=2, column=0)

# Places & Sets Command
addition_button = canvas_addition.create_image(40, 40, image=add_addition_image)
canvas_addition.tag_bind(addition_button, "<Button>", addition_button_clicked)


# ---------- Subtraction Button ----------

# Subtraction Button Link
def subtraction_button_clicked(event):
    '''Testing Button'''
    print("Subtraction Button clicked!")

# Creates Canvas Widget
canvas_subtraction = Canvas(master=button_frame, width=80, height=80, bg='#242424', highlightthickness=0)
canvas_subtraction.grid(row=1, column=1)

# Adds/Resize Operator Image
subtract_image = Image.open("C:/Users/Marc/Downloads/Maths Master/images/subtraction.png")
subtract_image = subtract_image.resize((70, 70))
add_subtraction_image = ImageTk.PhotoImage(subtract_image)

# Subtraction Text
subtraction_text = Label(master=button_frame, text="Subtraction",
                      font=("Raleway", "10"), bg="#242424", fg="white",
                      width=10)
subtraction_text.grid(row=2, column=1)

# Places & Sets Command
subtraction_button = canvas_subtraction.create_image(40, 40, image=add_subtraction_image)
canvas_subtraction.tag_bind(subtraction_button, "<Button>", subtraction_button_clicked)


# xxxxxxxxxx Multiplication Button xxxxxxxxxx

# Multiplication Button Link
def multiplication_button_clicked(event):
    '''Testing Button'''
    print("Multiplication Button clicked!")

# Creates Canvas Widget
canvas_multiplication = Canvas(master=button_frame, width=80, height=80, bg='#242424', highlightthickness=0)
canvas_multiplication.grid(row=1, column=2)

# Adds/Resize Operator Image
multiplication_image = Image.open("C:/Users/Marc/Downloads/Maths Master/images/multiplication.png")
multiplication_image = multiplication_image.resize((70, 70))
add_multiplication_image = ImageTk.PhotoImage(multiplication_image)

# Multiplication Text
multiplication_text = Label(master=button_frame, text="Multiplication",
                      font=("Raleway", "10"), bg="#242424", fg="white",
                      width=10)
multiplication_text.grid(row=2, column=2)

# Places & Sets Command
multiplication_button = canvas_multiplication.create_image(40, 40, image=add_multiplication_image)
canvas_multiplication.tag_bind(multiplication_button, "<Button>", multiplication_button_clicked)


# ÷÷÷÷÷÷÷÷÷÷ Division Button ÷÷÷÷÷÷÷÷÷÷

# Division Button Link
def division_button_clicked(event):
    '''Testing Button'''
    print("Division Button clicked!")

# Creates Canvas Widget
canvas_division = Canvas(master=button_frame, width=80, height=80, bg='#242424', highlightthickness=0)
canvas_division.grid(row=1, column=3)

# Adds/Resize Operator Image
division_image = Image.open("C:/Users/Marc/Downloads/Maths Master/images/division.png")
division_image = division_image.resize((70, 70))
add_division_image = ImageTk.PhotoImage(division_image)

# Division Text
division_text = Label(master=button_frame, text="Division",
                      font=("Raleway", "10"), bg="#242424", fg="white",
                      width=10)
division_text.grid(row=2, column=3)

# Places & Sets Command
division_button = canvas_division.create_image(40, 40, image=add_division_image)
canvas_division.tag_bind(division_button, "<Button>", division_button_clicked)


# Displays GUI
root.mainloop()
