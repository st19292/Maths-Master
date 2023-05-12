# Classes Importing
from tkinter import *
'''GUI Python Module'''

from PIL import Image, ImageTk
'''GUI Images Added'''


# Creates Window
root = Tk()
root.title("Maths Master")
root.resizable(False, False)
root.configure(bg="#242424")


# Top Proximity, Header (Row 0)

# Primary Headers Frame
headings_frame = Frame(master=root, padx=10, pady=10, bg="#2B2B2B")
headings_frame.grid(row=0, column=0)

# Main & Subheading Labels
menu_heading_text = "Maths Master: Basic Facts Quiz"
main_heading = Label(master=headings_frame, text=menu_heading_text,
                     font=("Raleway", "20", "bold"), bg="#2B2B2B", fg="white",
                     width=30)
main_heading.pack(pady=(10, 0))

menu_subheading_text = "Test your maths knowledge by choosing a basic facts challenge!"
subheading = Label(master=headings_frame, text=menu_subheading_text,
                   font=("Raleway", "10"), bg="#2B2B2B", fg="white",
                   width=80)
subheading.pack(pady=(10, 0))


# Middle Proximity, Quiz Choice (Row 1-2)

# Operator Buttons Frame 
operators_frame = Frame(root, bg="#242424", padx=10, pady=40)
operators_frame.grid(row=1, column=0, rowspan=2)


# Addition Button Link
def addition_button_clicked(click):
    """Testing Button"""
    print("Addition Button clicked!")


# Subtraction Button Link
def subtraction_button_clicked(click):
    """Testing Button"""
    print("Subtraction Button clicked!")


# Multiplication Button Link
def multiplication_button_clicked(click):
    """Testing Button"""
    print("Multiplication Button clicked!")


# Division Button Link
def division_button_clicked(click):
    """Testing Button"""
    print("Division Button clicked!")


# Creates Addition Widget
canvas_addition = Canvas(master=operators_frame, width=82, height=82, bg="#242424", highlightthickness=0)
canvas_addition.grid(row=1, column=0)

# Adds/Resize Addition Image
addition_image = Image.open("images/addition.png")
addition_image = addition_image.resize((70, 70))
add_addition_image = ImageTk.PhotoImage(addition_image)

# Addition Text
addition_text = Label(master=operators_frame, text="Addition",
                      font=("Raleway", "8", "bold"), bg="#242424", fg="white",
                      width=10)
addition_text.grid(row=2, column=0)

# Sets Addition Command
addition_button = canvas_addition.create_image(40, 40, image=add_addition_image)
canvas_addition.tag_bind(addition_button, "<Button>", addition_button_clicked)


# Creates Subtraction Widget
canvas_subtraction = Canvas(master=operators_frame, width=82, height=82, bg="#242424", highlightthickness=0)
canvas_subtraction.grid(row=1, column=1)

# Adds/Resize Subtraction Image
subtract_image = Image.open("images/subtraction.png")
subtract_image = subtract_image.resize((70, 70))
add_subtraction_image = ImageTk.PhotoImage(subtract_image)

# Subtraction Text
subtraction_text = Label(master=operators_frame, text="Subtraction",
                         font=("Raleway", "8", "bold"), bg="#242424", fg="white",
                         width=10)
subtraction_text.grid(row=2, column=1)

# Sets Subtraction Command
subtraction_button = canvas_subtraction.create_image(40, 40, image=add_subtraction_image)
canvas_subtraction.tag_bind(subtraction_button, "<Button>", subtraction_button_clicked)


# Creates Multiplication Widget
canvas_multiplication = Canvas(master=operators_frame, width=82, height=82, bg="#242424", highlightthickness=0)
canvas_multiplication.grid(row=1, column=2)

# Adds/Resize Multiplication Image
multiplication_image = Image.open("images/multiplication.png")
multiplication_image = multiplication_image.resize((70, 70))
add_multiplication_image = ImageTk.PhotoImage(multiplication_image)

# Multiplication Text
multiplication_text = Label(master=operators_frame, text="Multiplication",
                            font=("Raleway", "8", "bold"), bg="#242424", fg="white",
                            width=10)
multiplication_text.grid(row=2, column=2)

# Sets Multiplication Command
multiplication_button = canvas_multiplication.create_image(40, 40, image=add_multiplication_image)
canvas_multiplication.tag_bind(multiplication_button, "<Button>", multiplication_button_clicked)


# Creates Division Widget
canvas_division = Canvas(master=operators_frame, width=82, height=82, bg="#242424", highlightthickness=0)
canvas_division.grid(row=1, column=3)

# Adds/Resize Division Image
division_image = Image.open("images/division.png")
division_image = division_image.resize((70, 70))
add_division_image = ImageTk.PhotoImage(division_image)

# Division Text
division_text = Label(master=operators_frame, text="Division",
                      font=("Raleway", "8", "bold"), bg="#242424", fg="white",
                      width=10)
division_text.grid(row=2, column=3)

# Sets Division Command
division_button = canvas_division.create_image(40, 40, image=add_division_image)
canvas_division.tag_bind(division_button, "<Button>", division_button_clicked)


# Bottom Proximity, Footer Navigation (Row 3)

# Info/Export Buttons Frame
bottom_buttons_frame = Frame(root, bg="#242424", padx=10, pady=20)
bottom_buttons_frame.grid(row=3, column=0, rowspan=4)


# Help & Info Button Link
def help_and_info_button_clicked():
    """Testing Button"""
    print("Help & Info Button clicked!")


# History & Export Link
def history_and_export_button_clicked():
    """Testing Button"""
    print("History & Export Button clicked!")


# Help & Info Button
help_and_info_button = Button(master=bottom_buttons_frame, text="Help & Info", 
                              font=("Raleway", "11", "bold"), fg="black", bg="white", 
                              height=1, width=16, relief="flat", command=help_and_info_button_clicked)
help_and_info_button.grid(row=3, column=0, padx=8, pady=10)

# History & Export Button
history_and_export_button = Button(master=bottom_buttons_frame, text="History & Export", 
                                   font=("Raleway", "11", "bold"), fg="black", bg="white", 
                                   height=1, width=16, relief="flat", command=history_and_export_button_clicked)
history_and_export_button.grid(row=3, column=1, padx=8, pady=10)


# Displays GUI
root.mainloop()
