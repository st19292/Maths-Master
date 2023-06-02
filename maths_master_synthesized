# Project: Maths Master
# Component X: Synthesizing Draft
# 30052023: Compiled Three Windows


# Classes Importing
from tkinter import *
'''GUI Python Module'''

from PIL import Image, ImageTk
'''GUI Images Added'''

import random
'''Randomizing Module'''

import datetime
"""Module Allows Date Retrieval"""


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
            AdditionQuiz()

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
            HistoryAndExport()

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


# Maths Master Quiz Interface
class AdditionQuiz:
    """Creates Class for Quiz Interface Window"""

    def __init__(self):
        """Initializes Math Master Instance"""

        # Sets Tkinter Window Settings
        self.root = Tk()
        self.root.title("Maths Master: Addition Quiz")
        self.root.resizable(False, False)
        self.root.configure(bg="#242424")

        # Creates Top Proximity Frame
        self.top_headings_frame = Frame(self.root, padx=10, pady=10, bg="#2B2B2B")

        # Creates Middle Proximity Frame
        self.middle_quiz_frame = Frame(self.root, bg="#242424", padx=10, pady=40)

        # Creates Bottom Proximity Frame
        self.bottom_buttons_frame = Frame(self.root, bg="#242424", padx=10, pady=20)

        # Initialize Question, Answer & Update Variables
        self.question = ""
        self.answer = 0
        self.question_number = 0
        self.subheading = ""
        self.addition_text = None
        self.user_entry = None
        self.number_one = None
        self.number_two = None
        self.feedback_text = None
        self.incorrect_list = []
        self.next_question_button = None

        # Calls Frames Methods & Elements
        self.menu_top_frame()
        self.menu_middle_frame()
        self.menu_bottom_frame()

        # Creates First Question
        self.generate_new_question()

        # Displays GUI
        self.root.mainloop()

    def menu_top_frame(self):
        """Top Proximity: Headings Frame Function"""

        # Top Proximity, Header (Row 0)
        self.top_headings_frame.grid(row=0, column=0)

        # Main & Subheading Labels
        menu_heading_text = "Addition Quiz"
        main_heading = Label(master=self.top_headings_frame, text=menu_heading_text,
                             font=("Raleway", "20", "bold"), bg="#2B2B2B", fg="white",
                             width=30)
        main_heading.pack(pady=(10, 0))

        # Sets Question Number
        menu_subheading_text = f"Question {self.question_number} of 10"
        self.subheading = Label(master=self.top_headings_frame, text=menu_subheading_text,
                                font=("Raleway", "10"), bg="#2B2B2B", fg="white",
                                width=80)
        self.subheading.pack(pady=(10, 0))

    def menu_middle_frame(self):
        """Middle Proximity: Quiz Interface Frame Function"""

        # Middle Proximity, Quiz Choice (Row 1-4)
        self.middle_quiz_frame.grid(row=1, column=0, rowspan=2)

        # Quiz Questions Heading
        self.addition_text = Label(master=self.middle_quiz_frame, text=self.question, font=("Raleway", "35", "bold"),
                                   bg="#242424", fg="white", width=10)
        self.addition_text.grid(row=2, column=0)

        # Entry Feedback
        self.feedback_text = Label(master=self.middle_quiz_frame, text="Please type an answer",
                                   font=("Raleway", "9"), bg="#242424", fg="white",
                                   width=35)
        self.feedback_text.grid(row=3, column=0)

        # Entry Feedback
        self.user_entry = Entry(master=self.middle_quiz_frame, font=("Raleway", "12"), width=18, justify=CENTER)
        self.user_entry.grid(row=4, column=0)

        # Runs Function for Question
        self.generate_new_question()

    def menu_bottom_frame(self):
        """Bottom Proximity: Button Navigation Frame Function"""

        # Bottom Proximity, Footer Navigation (Row 5)
        self.bottom_buttons_frame.grid(row=5, column=0, rowspan=4)

        # Help & Info Button Link
        def return_to_menu_button_clicked():
            """Testing Button"""
            self.root.destroy()

        # Return To Menu Button
        return_to_menu_button = Button(master=self.bottom_buttons_frame, text="Return To Menu",
                                       font=("Raleway", "11", "bold"), fg="black", bg="white",
                                       height=1, width=16, relief="flat", command=return_to_menu_button_clicked)
        return_to_menu_button.grid(row=5, column=0, padx=8, pady=10)

        # Submit Answer Button
        self.next_question_button = Button(master=self.bottom_buttons_frame, text="Submit Answer",
                                           font=("Raleway", "11", "bold"), fg="black", bg="white",
                                           height=1, width=16, relief="flat", command=self.answer_check)
        self.next_question_button.grid(row=5, column=1, padx=8, pady=10)

    def random_numbers(self):
        """Generates & Displays Two Random Numbers"""

        # Randomizes Two Number from 1 to 25
        self.number_one = random.randint(1, 25)
        self.number_two = random.randint(1, 25)

        # Sets Heading Question & Correct Answer
        self.question = f"{self.number_one} + {self.number_two}"
        self.answer = self.number_one + self.number_two

    def generate_new_question(self):
        """Generates New Numbers & Updates as New Question"""

        # Calls New Numbers & Updates Question Heading
        self.random_numbers()
        self.addition_text.config(text=self.question)

        # Clears Entry Box
        self.user_entry.delete(0, END)

        # Updates Question Number
        menu_subheading_text = f"Question {self.question_number} of 10"
        self.subheading.config(text=menu_subheading_text)
        self.question_number += 1

        # Disables Button if 10 Question Iterated
        if self.question_number > 10:
            self.next_question_button.config(state="disabled")
            self.subheading.config(text="Quiz Finished!")

    def answer_check(self):
        """Checks User Input as Correct, Incorrect, or Invalid"""

        # Checks if Input is Integer
        try:
            # Sets Variable from Called Entry
            user_answer = int(self.user_entry.get())

            # Compares Correct Answer & User Input to Mark; Changes Color to Green or Red
            if user_answer == self.answer:
                self.feedback_text.config(text=f"Correct: {self.number_one} + {self.number_two} is {self.answer}")
                self.feedback_text.config(fg="#99FF99")
            else:
                self.feedback_text.config(text=f"Incorrect: {self.number_one} + {self.number_two} is {self.answer}")
                self.incorrect_list.append(f"{self.number_one} + {self.number_two} = {self.answer}")
                self.feedback_text.config(fg="#FF9999")

            # If Integers Valid, Generates New Question
            self.generate_new_question()

        # Addresses Invalid Input
        except ValueError:
            self.feedback_text.config(text="Invalid input. Please enter a valid number.")
            self.feedback_text.config(fg="#FF9999")
            self.user_entry.delete(0, END)

        # Given Unknown Error, Addresses
        except Exception as e:
            self.feedback_text.config(text=f"An error occurred: {str(e)}")
            self.feedback_text.config(fg="#FF9999")
            self.user_entry.delete(0, END)


class HistoryAndExport:
    def __init__(self):
        """Initializes Math Master Instance"""

        self.root = Tk()
        self.root.title("Maths Master: History & Export")
        self.root.resizable(False, False)
        self.root.configure(bg="#242424")

        # Creates Top Proximity Frame
        self.top_headings_frame = Frame(self.root, padx=10, pady=10, bg="#2B2B2B")

        # Creates Middle Proximity Frame
        self.middle_operators_frame = Frame(self.root, bg="#242424", padx=10, pady=40)

        # Creates Bottom Proximity Frame
        self.bottom_buttons_frame = Frame(self.root, bg="#242424", padx=10, pady=20)

        # Sets Filename and Answers List
        self.filename = ""
        self.answers_list = []
        self.file_naming = None
        self.user_entry = None

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
        menu_heading_text = "History & Export"
        main_heading = Label(master=self.top_headings_frame, text=menu_heading_text,
                             font=("Raleway", "20", "bold"), bg="#2B2B2B", fg="white",
                             width=30)
        main_heading.pack(pady=(10, 0))

        menu_subheading_text = "Revise your wrong answers. " \
                               "(When exporting, if file name already exists, it will be replaced.)"
        subheading = Label(master=self.top_headings_frame, text=menu_subheading_text,
                           font=("Raleway", "10"), bg="#2B2B2B", fg="white",
                           width=80)
        subheading.pack(pady=(10, 0))

    def menu_middle_frame(self):
        """Middle Proximity: Button Operators Frame Function"""
        # Middle Proximity, Quiz Choice (Row 1-2)
        self.middle_operators_frame.grid(row=1, column=0, rowspan=2, padx=10, pady=0)

        recent_label = Label(master=self.middle_operators_frame, text="Recent Incorrect Answers",
                             font=("Raleway", "10",), bg="#242424", fg="white",
                             wraplength=420)
        recent_label.grid(row=0, column=0, pady=0)

        # Correct Answers Frame
        corrected_answers_frame = Frame(self.root, padx=10, pady=10, bg="#242424")
        corrected_answers_frame.grid(row=2, column=0, rowspan=2, padx=10, pady=(60, 0))

        # Iterates First Five in List
        for i in range(5):
            answer_label = Label(master=corrected_answers_frame, text=self.answers_list[i],
                                 font=("Raleway", "8"), bg="#242424", fg="white",
                                 wraplength=70)
            answer_label.grid(row=i + 1, column=0, padx=5, pady=0)
            """Iterates Next Number as Next Row"""

        # Iterates Last Five in List
        for i in range(5, 10):
            answer_label = Label(master=corrected_answers_frame, text=self.answers_list[i],
                                 font=("Raleway", "8"), bg="#242424", fg="white",
                                 wraplength=70)
            answer_label.grid(row=i - 4, column=1, padx=5, pady=0)
            """When i = 5, 5 - 4 is 1 for Row & Column 1"""

        # Export Entry Frame
        export_entry_frame = Frame(self.root, padx=10, pady=10, bg="#242424")
        export_entry_frame.grid(row=4, column=0, rowspan=2, padx=10, pady=(0, 0))

        # Answers List Saving Heading
        self.file_naming = Label(master=export_entry_frame, text="Export Test",
                                 font=("Raleway", "10",), bg="#242424", fg="white")
        self.file_naming.grid(row=4, column=0, pady=0)

        # User Entry List
        self.user_entry = Entry(master=export_entry_frame, font=("Raleway", "12"), width=18, justify=CENTER)
        self.user_entry.grid(row=5, column=0)

    def menu_bottom_frame(self):
        """Bottom Proximity: Button Navigation Frame Function"""

        # Bottom Proximity, Footer Navigation (Row 3)
        self.bottom_buttons_frame.grid(row=6, column=0, rowspan=4)

        # Return To Menu Button Link
        def return_to_menu_button_clicked():
            """Testing Button"""
            self.root.destroy()

        # History & Export Link
        def export_answers_list():
            """Saves File's Name as .txt"""
            with open(self.filename, 'w') as file:
                for answer in self.answers_list:
                    file.write(answer + '\n')
                    self.file_naming.config(text=f"File Saved as '{self.filename}'")
                    self.file_naming.config(fg="#99FF99")

        # If Unnamed, Saves File as Date; Fails if Spaces/Special Characters
        def naming_check():
            """Validate Filename Input"""
            self.filename = self.user_entry.get()

            if not self.filename:
                """Saves File as Current Time"""
                current_date = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
                self.filename = current_date + "_answers_list.txt"
                export_answers_list()

            elif any(not c.isalnum() for c in self.filename):
                """Restricts Saving File with Special Characters"""
                self.file_naming.config(text=f"No Special Characters or Spaces!")
                self.file_naming.config(fg="#FF9999")

            else:
                self.filename = self.filename + ".txt"
                export_answers_list()

        # Return To Menu Button
        return_to_menu_button = Button(master=self.bottom_buttons_frame, text="Return To Menu",
                                       font=("Raleway", "11", "bold"), fg="black", bg="white",
                                       height=1, width=16, relief="flat", command=return_to_menu_button_clicked)
        return_to_menu_button.grid(row=6, column=0, padx=8, pady=0)

        # Export Button
        export_button = Button(master=self.bottom_buttons_frame, text="Export",
                               font=("Raleway", "11", "bold"), fg="black", bg="white",
                               height=1, width=16, relief="flat", command=naming_check)
        export_button.grid(row=6, column=1, padx=8, pady=10)


# Runs Math Master App
MathsMasterApp()
