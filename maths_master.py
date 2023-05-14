# Project: Maths Master
# Component 1.3: Final Draft
# 14052023: Added Classes Execution


# Classes Importing
from tkinter import *
'''GUI Python Module'''

from PIL import Image, ImageTk
'''GUI Images Added'''


# Maths Master Main Menu
class MathsMasterApp:
    def __init__(self):
        """Initializes Math Master Instance"""

        self.root = Tk()
        self.root.title("Maths Master")
        self.root.resizable(False, False)
        self.root.configure(bg="#242424")

        # Creates Top Proximity Frame
        self.top_headings_frame = Frame(self.root, padx=10, pady=10, bg="#2B2B2B")

        # Creates Middle Proximity Frame
        self.middle_operators_frame = Frame(self.root, bg="#242424", padx=10, pady=40)

        # Creates Bottom Proximity Frame
        self.bottom_buttons_frame = Frame(self.root, bg="#242424", padx=10, pady=20)

        # Creates Image Instances for Operator Buttons
        self.addition_image_path = "images/addition.png"
        addition_image = Image.open(self.addition_image_path)
        addition_image = addition_image.resize((70, 70))
        self.add_addition_image = ImageTk.PhotoImage(addition_image)

        self.subtraction_image_path = "images/subtraction.png"
        subtraction_image = Image.open(self.subtraction_image_path)
        subtraction_image = subtraction_image.resize((70, 70))
        self.add_subtraction_image = ImageTk.PhotoImage(subtraction_image)

        self.multiplication_image_path = "images/multiplication.png"
        multiplication_image = Image.open(self.multiplication_image_path)
        multiplication_image = multiplication_image.resize((70, 70))
        self.add_multiplication_image = ImageTk.PhotoImage(multiplication_image)

        self.division_image_path = "images/division.png"
        division_image = Image.open(self.division_image_path)
        division_image = division_image.resize((70, 70))
        self.add_division_image = ImageTk.PhotoImage(division_image)

        # Calls Frames Methods & Elements
        self.menu_top_frame()
        self.menu_middle_frame()
        self.menu_bottom_frame()

        # Displays GUI
        self.root.mainloop()

    def menu_top_frame(self):
        """Top Proximity: Headings Frame Function"""

        # Top Proximity, Header (Row 0)
        self.top_headings_frame.grid(row=0, column=0)

        # Main & Subheading Labels
        menu_heading_text = "Maths Master: Basic Facts Quiz"
        main_heading = Label(master=self.top_headings_frame, text=menu_heading_text,
                             font=("Raleway", "20", "bold"), bg="#2B2B2B", fg="white",
                             width=30)
        main_heading.pack(pady=(10, 0))

        menu_subheading_text = "Test your maths knowledge by choosing a basic facts challenge!"
        subheading = Label(master=self.top_headings_frame, text=menu_subheading_text,
                           font=("Raleway", "10"), bg="#2B2B2B", fg="white",
                           width=80)
        subheading.pack(pady=(10, 0))

    def menu_middle_frame(self):
        """Middle Proximity: Button Operators Frame Function"""

        # Middle Proximity, Quiz Choice (Row 1-2)
        self.middle_operators_frame.grid(row=1, column=0, rowspan=2)

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
        canvas_addition = Canvas(master=self.middle_operators_frame, width=82, height=82,
                                 bg="#242424", highlightthickness=0)
        canvas_addition.grid(row=1, column=0)

        # Addition Text
        addition_text = Label(master=self.middle_operators_frame, text="Addition",
                              font=("Raleway", "8", "bold"), bg="#242424", fg="white",
                              width=10)
        addition_text.grid(row=2, column=0)

        # Sets Addition Command
        addition_button = canvas_addition.create_image(40, 40, image=self.add_addition_image)
        canvas_addition.tag_bind(addition_button, "<Button>", addition_button_clicked)

        # Creates Subtraction Widget
        canvas_subtraction = Canvas(master=self.middle_operators_frame, width=82, height=82,
                                    bg="#242424", highlightthickness=0)
        canvas_subtraction.grid(row=1, column=1)

        # Subtraction Text
        subtraction_text = Label(master=self.middle_operators_frame, text="Subtraction",
                                 font=("Raleway", "8", "bold"), bg="#242424", fg="white",
                                 width=10)
        subtraction_text.grid(row=2, column=1)

        # Sets Subtraction Command
        subtraction_button = canvas_subtraction.create_image(40, 40, image=self.add_subtraction_image)
        canvas_subtraction.tag_bind(subtraction_button, "<Button>", subtraction_button_clicked)

        # Creates Multiplication Widget
        canvas_multiplication = Canvas(master=self.middle_operators_frame, width=82, height=82,
                                       bg="#242424", highlightthickness=0)
        canvas_multiplication.grid(row=1, column=2)

        # Multiplication Text
        multiplication_text = Label(master=self.middle_operators_frame, text="Multiplication",
                                    font=("Raleway", "8", "bold"), bg="#242424", fg="white",
                                    width=10)
        multiplication_text.grid(row=2, column=2)

        # Sets Multiplication Command
        multiplication_button = canvas_multiplication.create_image(40, 40, image=self.add_multiplication_image)
        canvas_multiplication.tag_bind(multiplication_button, "<Button>", multiplication_button_clicked)

        # Creates Division Widget
        canvas_division = Canvas(master=self.middle_operators_frame, width=82, height=82,
                                 bg="#242424", highlightthickness=0)
        canvas_division.grid(row=1, column=3)

        # Division Text
        division_text = Label(master=self.middle_operators_frame, text="Division",
                              font=("Raleway", "8", "bold"), bg="#242424", fg="white",
                              width=10)
        division_text.grid(row=2, column=3)

        # Sets Division Command
        division_button = canvas_division.create_image(40, 40, image=self.add_division_image)
        canvas_division.tag_bind(division_button, "<Button>", division_button_clicked)

    def menu_bottom_frame(self):
        """Bottom Proximity: Button Navigation Frame Function"""

        # Bottom Proximity, Footer Navigation (Row 3)
        self.bottom_buttons_frame.grid(row=3, column=0, rowspan=4)

        # Help & Info Button Link
        def help_and_info_button_clicked():
            """Testing Button"""
            print("Help & Info Button clicked!")

        # History & Export Link
        def history_and_export_button_clicked():
            """Testing Button"""
            print("History & Export Button clicked!")

        # Help & Info Button
        help_and_info_button = Button(master=self.bottom_buttons_frame, text="Help & Info",
                                      font=("Raleway", "11", "bold"), fg="black", bg="white",
                                      height=1, width=16, relief="flat", command=help_and_info_button_clicked)
        help_and_info_button.grid(row=3, column=0, padx=8, pady=10)

        # History & Export Button
        history_and_export_button = Button(master=self.bottom_buttons_frame, text="History & Export",
                                           font=("Raleway", "11", "bold"), fg="black", bg="white",
                                           height=1, width=16, relief="flat", command=history_and_export_button_clicked)
        history_and_export_button.grid(row=3, column=1, padx=8, pady=10)


MathsMasterApp()
