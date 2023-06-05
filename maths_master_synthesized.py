# Project: Maths Master - AS91906 (Marc Mojica).
# Improve your Maths skills through various quizzes and export your answers for reviewing.
# Component X.12: Final Refined Finished Program.
# 04062023: Added Window Focussing and Accessibility Button Binds.


# Classes Importing
from tkinter import *
"""GUI Python Module"""

from PIL import Image, ImageTk
"""Allows Images To Be Added"""

import random
"""Randomizing Module"""

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
        self.root.geometry("+0+10")
        self.root.focus_force()

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

        self.top_headings_frame.grid(row=0, column=0)

        # Main & Subheading Labels
        menu_heading_text = "Maths Master: Basic Facts Quiz"
        main_heading = Label(master=self.top_headings_frame, text=menu_heading_text,
                             font=("Raleway", "20", "bold"), bg="#2B2B2B", fg="white", width=30)
        main_heading.pack(pady=(10, 0))

        menu_subheading_text = "Test your maths knowledge by choosing a basic facts challenge!"
        subheading = Label(master=self.top_headings_frame, text=menu_subheading_text,
                           font=("Raleway", "10"), bg="#2B2B2B", fg="white", width=80)
        subheading.pack(pady=(10, 0))

    def menu_middle_frame(self):
        """Middle Proximity: Button Operators Frame Function (Row 1-2)"""

        self.middle_operators_frame.grid(row=1, column=0, rowspan=2)

        # Addition Button Link
        def addition_button_clicked(click):
            """Runs Addition Quiz"""

            self.root.destroy()
            QuizInterface("+")

        # Subtraction Button Link
        def subtraction_button_clicked(click):
            """Runs Subtraction Quiz"""

            self.root.destroy()
            QuizInterface("-")

        # Multiplication Button Link
        def multiplication_button_clicked(click):
            """Runs Multiplication Quiz"""

            self.root.destroy()
            QuizInterface("*")

        # Division Button Link
        def division_button_clicked(click):
            """Runs Division Quiz"""

            self.root.destroy()
            QuizInterface("/")

        # Creates Addition Widget
        canvas_addition = Canvas(master=self.middle_operators_frame, width=82, height=82, bg="#242424",
                                 highlightthickness=0)
        canvas_addition.grid(row=1, column=0)

        # Addition Text
        addition_text = Label(master=self.middle_operators_frame, text="(1) Addition",
                              font=("Raleway", "7", "bold"), bg="#242424", fg="white", width=12)
        addition_text.grid(row=2, column=0)

        # Sets Addition Command
        addition_button = canvas_addition.create_image(40, 40, image=self.add_addition_image)
        canvas_addition.tag_bind(addition_button, "<Button>", addition_button_clicked)
        self.root.bind('1', addition_button_clicked)

        # Creates Subtraction Widget
        canvas_subtraction = Canvas(master=self.middle_operators_frame, width=82, height=82, bg="#242424",
                                    highlightthickness=0)
        canvas_subtraction.grid(row=1, column=1)

        # Subtraction Text
        subtraction_text = Label(master=self.middle_operators_frame, text="(2) Subtraction",
                                 font=("Raleway", "7", "bold"), bg="#242424", fg="white", width=12)
        subtraction_text.grid(row=2, column=1)

        # Sets Subtraction Command
        subtraction_button = canvas_subtraction.create_image(40, 40, image=self.add_subtraction_image)
        canvas_subtraction.tag_bind(subtraction_button, "<Button>", subtraction_button_clicked)
        self.root.bind('2', subtraction_button_clicked)

        # Creates Multiplication Widget
        canvas_multiplication = Canvas(master=self.middle_operators_frame, width=82, height=82, bg="#242424",
                                       highlightthickness=0)
        canvas_multiplication.grid(row=1, column=2)

        # Multiplication Text
        multiplication_text = Label(master=self.middle_operators_frame, text="(3) Multiplication",
                                    font=("Raleway", "7", "bold"), bg="#242424", fg="white", width=12)
        multiplication_text.grid(row=2, column=2)

        # Sets Multiplication Command
        multiplication_button = canvas_multiplication.create_image(40, 40, image=self.add_multiplication_image)
        canvas_multiplication.tag_bind(multiplication_button, "<Button>", multiplication_button_clicked)
        self.root.bind('3', multiplication_button_clicked)

        # Creates Division Widget
        canvas_division = Canvas(master=self.middle_operators_frame, width=82, height=82, bg="#242424",
                                 highlightthickness=0)
        canvas_division.grid(row=1, column=3)

        # Division Text
        division_text = Label(master=self.middle_operators_frame, text="(4) Division",
                              font=("Raleway", "7", "bold"), bg="#242424", fg="white", width=12)
        division_text.grid(row=2, column=3)

        # Sets Division Command
        division_button = canvas_division.create_image(40, 40, image=self.add_division_image)
        canvas_division.tag_bind(division_button, "<Button>", division_button_clicked)
        self.root.bind('4', division_button_clicked)

    def menu_bottom_frame(self):
        """Bottom Proximity: Button Navigation Frame Function (Row 3)"""

        self.bottom_buttons_frame.grid(row=3, column=0, rowspan=4)

        # Exit Program Link
        def exit_program_button_clicked():
            self.root.destroy()

        # Help & Info Button Link
        def help_and_info_button_clicked():
            self.root.destroy()
            HelpAndInfo()

        # Exit Program Button
        exit_program_button = Button(master=self.bottom_buttons_frame, text="(ESC) Quit",
                                     font=("Raleway", "11", "bold"), fg="black", bg="white",
                                     height=1, width=16, relief="flat", command=exit_program_button_clicked)
        exit_program_button.grid(row=3, column=0, padx=8, pady=0)

        # Binds Escape Key with Quit Program Button
        self.root.bind('<Escape>', lambda event: exit_program_button_clicked())

        # Help & Info Button
        help_and_info_button = Button(master=self.bottom_buttons_frame, text="(I) Help & Info",
                                      font=("Raleway", "11", "bold"), fg="black", bg="white",
                                      height=1, width=16, relief="flat", command=help_and_info_button_clicked)
        help_and_info_button.grid(row=3, column=1, padx=8, pady=0)

        # Binds I Key with Help and Info Button
        self.root.bind('<i>', lambda event: help_and_info_button_clicked())


# Quiz Interface Class Window
class QuizInterface:
    """Creates Class for Quiz Interface Window"""

    def __init__(self, operator):
        """Initializes Math Master Instance"""

        # Sets Tkinter Window Settings
        self.root = Tk()
        self.root.title("Maths Master Quiz")
        self.root.resizable(False, False)
        self.root.configure(bg="#242424")
        self.root.geometry("+0+10")
        self.root.focus_force()

        # Creates Top Proximity Frame
        self.top_headings_frame = Frame(self.root, padx=10, pady=10, bg="#2B2B2B")

        # Creates Middle Proximity Frame
        self.middle_quiz_frame = Frame(self.root, bg="#242424", padx=10, pady=40)

        # Creates Bottom Proximity Frame
        self.bottom_buttons_frame = Frame(self.root, bg="#242424", padx=10, pady=20)

        # Initialize Question, Answer & Update Variables
        self.operator = operator
        self.question = ""
        self.answer = 0
        self.question_number = 0
        self.subheading = ""
        self.operator_text = None
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

        self.top_headings_frame.grid(row=0, column=0)

        # Main & Subheading Labels
        menu_heading_text = "Maths Master Quiz"
        main_heading = Label(master=self.top_headings_frame, text=menu_heading_text,
                             font=("Raleway", "20", "bold"), bg="#2B2B2B", fg="white", width=30)
        main_heading.pack(pady=(10, 0))

        # Sets Question Number
        menu_subheading_text = f"Question {self.question_number} of 10"
        self.subheading = Label(master=self.top_headings_frame, text=menu_subheading_text,
                                font=("Raleway", "10"), bg="#2B2B2B", fg="white", width=80)
        self.subheading.pack(pady=(10, 0))

    def menu_middle_frame(self):
        """Middle Proximity: Quiz Interface Frame Function (Row 1-4)"""

        self.middle_quiz_frame.grid(row=1, column=0, rowspan=2)

        # Quiz Questions Heading
        self.operator_text = Label(master=self.middle_quiz_frame, text=self.question, font=("Raleway", "35", "bold"),
                                   bg="#242424", fg="white", width=10)
        self.operator_text.grid(row=2, column=0)

        # Entry Feedback
        self.feedback_text = Label(master=self.middle_quiz_frame, text="Please type an answer",
                                   font=("Raleway", "9"), bg="#242424", fg="white", width=35)
        self.feedback_text.grid(row=3, column=0)

        # Entry Feedback
        self.user_entry = Entry(master=self.middle_quiz_frame, font=("Raleway", "12"), width=18, justify=CENTER)
        self.user_entry.grid(row=4, column=0)

        # Runs Function for Question
        self.generate_new_question()

    def menu_bottom_frame(self):
        """Bottom Proximity: Button Navigation Frame Function (Row 5)"""

        self.bottom_buttons_frame.grid(row=5, column=0, rowspan=4)

        # Help & Info Button Link
        def return_to_menu_button_clicked():
            """Closes Window"""

            self.root.destroy()
            MathsMasterApp()

        # Return To Menu Button
        return_to_menu_button = Button(master=self.bottom_buttons_frame, text="Return To Menu",
                                       font=("Raleway", "11", "bold"), fg="black", bg="white",
                                       height=1, width=16, relief="flat", command=return_to_menu_button_clicked)
        return_to_menu_button.grid(row=5, column=0, padx=8, pady=10)

        # Binds Escape Key with Submit Answer Button
        self.root.bind('<Escape>', lambda event: return_to_menu_button_clicked())

        # Submit Answer Button
        self.next_question_button = Button(master=self.bottom_buttons_frame, text="Submit Answer",
                                           font=("Raleway", "11", "bold"), fg="black", bg="white",
                                           height=1, width=16, relief="flat", command=self.answer_check)
        self.next_question_button.grid(row=5, column=1, padx=8, pady=10)

        # Binds Enter/Space Key with Submit Answer Button
        self.root.bind('<Return>', lambda event: self.answer_check())
        self.root.bind('<space>', lambda event: self.answer_check())

    def random_numbers(self):
        """Generates & Displays Two Random Numbers"""

        self.number_one = random.randint(0, 12)
        self.number_two = random.randint(0, 12)

        if self.operator == "+":
            """Sets Heading Question & Correct Answer"""

            self.question = f"{self.number_one} + {self.number_two}"
            self.answer = self.number_one + self.number_two

        elif self.operator == "-":
            self.question = f"{self.number_one} - {self.number_two}"
            self.answer = self.number_one - self.number_two

        elif self.operator == "*":
            self.question = f"{self.number_one} × {self.number_two}"
            self.answer = self.number_one * self.number_two

        else:
            number_one_divisor = [i for i in range(1, self.number_one + 1) if self.number_one % i == 0]
            """Sets Whole Numbers as Answers"""

            if number_one_divisor:
                self.number_two = random.choice(number_one_divisor)

            else:
                """Handles Empty Divisor"""
                self.number_two = 1

            self.question = f"{self.number_one} ÷ {self.number_two}"
            self.answer = self.number_one // self.number_two

    def generate_new_question(self):
        """Generates New Numbers & Updates as New Question"""

        # Calls New Numbers & Updates Question Heading
        self.random_numbers()
        self.operator_text.config(text=self.question)

        # Clears Entry Box
        self.user_entry.delete(0, END)

        # Updates Question Number
        menu_subheading_text = f"Question {self.question_number} of 10"
        self.subheading.config(text=menu_subheading_text)
        self.question_number += 1

        # Disables Button if 10 Question Iterated
        if self.question_number > 11:
            self.subheading.config(text="Quiz Finished")
            self.next_question_button.config(state="disabled")

            if len(self.incorrect_list) == 0:
                self.root.destroy()

            else:
                self.root.destroy()
                HistoryAndExport(self.incorrect_list)

    def answer_check(self):
        """Checks User Input as Correct, Incorrect, or Invalid"""

        try:

            # Sets Variable from Called Entry
            user_answer = int(self.user_entry.get())

            # Sets Correct Answer Relative to Operator
            if self.operator == "+":
                correct_answer = self.number_one + self.number_two
                operation_str = f"{self.number_one} + {self.number_two}"
            elif self.operator == "-":
                correct_answer = self.number_one - self.number_two
                operation_str = f"{self.number_one} - {self.number_two}"
            elif self.operator == "*":
                correct_answer = self.number_one * self.number_two
                operation_str = f"{self.number_one} × {self.number_two}"
            else:
                correct_answer = self.number_one // self.number_two
                operation_str = f"{self.number_one} ÷ {self.number_two}"

            # Compares Correct Answer & User Input to Mark; Changes Color to Green or Red
            if user_answer == correct_answer:
                self.feedback_text.config(text=f"Correct: {operation_str} is {correct_answer}")
                self.feedback_text.config(fg="#99FF99")

            else:
                self.feedback_text.config(text=f"Incorrect: {operation_str} is {correct_answer}")
                self.incorrect_list.append(f"{operation_str} = {correct_answer}")
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


# Help And Info Class Window
class HelpAndInfo:
    def __init__(self):
        """Initializes Math Master Instance"""

        self.root = Tk()
        self.root.title("Maths Master: Help & Info")
        self.root.resizable(False, False)
        self.root.configure(bg="#242424")
        self.root.geometry("+0+10")
        self.root.focus_force()

        # Creates Top Proximity Frame
        self.top_headings_frame = Frame(self.root, padx=10, pady=10, bg="#2B2B2B")

        # Creates Middle Proximity Frame
        self.middle_operators_frame = Frame(self.root, bg="#242424", padx=10, pady=40)

        # Creates Bottom Proximity Frame
        self.bottom_buttons_frame = Frame(self.root, bg="#242424", padx=10, pady=20)

        # Calls Frames Methods & Elements
        self.menu_top_frame()
        self.menu_middle_frame()
        self.menu_bottom_frame()

        # Displays GUI
        self.root.mainloop()

    def menu_top_frame(self):
        """Top Proximity: Headings Frame Function"""

        self.top_headings_frame.grid(row=0, column=0)

        # Main & Subheading Labels
        menu_heading_text = "Help & Information"
        main_heading = Label(master=self.top_headings_frame, text=menu_heading_text,
                             font=("Raleway", "20", "bold"), bg="#2B2B2B", fg="white", width=30)
        main_heading.pack(pady=(10, 0))

        menu_subheading_text = "Need help? Have a read on how to use the Math Master GUI."
        subheading = Label(master=self.top_headings_frame, text=menu_subheading_text,
                           font=("Raleway", "10"), bg="#2B2B2B", fg="white", width=80)
        subheading.pack(pady=(10, 0))

    def menu_middle_frame(self):
        """Middle Proximity: Button Operators Frame Function (Row 1-2)"""

        self.middle_operators_frame.grid(row=1, column=0, rowspan=2)

        # Help/Information Text
        help_and_info_text = ("This program helps you improve your basic math skills. "
                              "Choose from addition, subtraction, multiplication, or "
                              "division to take a quiz. Each quiz has 10 random questions. \n\n"
                              "If you get a question wrong, you can view your history of " 
                              "incorrect answers and export them for future review.")
        help_and_info = Label(master=self.middle_operators_frame, text=help_and_info_text,
                              font=("Raleway", "10",), bg="#242424", fg="white", wraplength=420)
        help_and_info.grid(row=2, column=0, pady=10)

    def menu_bottom_frame(self):
        """Bottom Proximity: Button Navigation Frame Function (Row 3)"""

        self.bottom_buttons_frame.grid(row=3, column=0, rowspan=4)

        # Return To Menu Button Link
        def return_to_menu_button_clicked():
            self.root.destroy()
            MathsMasterApp()

        # Help & Info Button
        return_to_menu_button = Button(master=self.bottom_buttons_frame, text="Return To Menu",
                                       font=("Raleway", "11", "bold"), fg="black", bg="white",
                                       height=1, width=16, relief="flat", command=return_to_menu_button_clicked)
        return_to_menu_button.grid(row=3, column=0, padx=8, pady=10)

        # Binds Escape Key with Return To Menu Button
        self.root.bind('<Escape>', lambda event: return_to_menu_button_clicked())


# History And Export Class Window
class HistoryAndExport:
    def __init__(self, incorrect_list):
        """Initializes Math Master Instance"""

        self.root = Tk()
        self.root.title("Maths Master: History & Export")
        self.root.resizable(False, False)
        self.root.configure(bg="#242424")
        self.root.geometry("+0+10")
        self.root.focus_force()

        # Creates Top Proximity Frame
        self.top_headings_frame = Frame(self.root, padx=10, pady=10, bg="#2B2B2B")

        # Creates Middle Proximity Frame
        self.middle_operators_frame = Frame(self.root, bg="#242424", padx=10, pady=40)

        # Creates Bottom Proximity Frame
        self.bottom_buttons_frame = Frame(self.root, bg="#242424", padx=10, pady=20)

        # Sets Filename and Answers List
        self.filename = ""
        self.answers_list = incorrect_list
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

        self.top_headings_frame.grid(row=0, column=0)

        # Main & Subheading Labels
        menu_heading_text = "History & Export"
        main_heading = Label(master=self.top_headings_frame, text=menu_heading_text,
                             font=("Raleway", "20", "bold"), bg="#2B2B2B", fg="white",
                             width=30)
        main_heading.pack(pady=(10, 0))

        menu_subheading_text = "Revise your wrong answers. " \
                               "(When exporting, if file name already exists, it will be replaced)"
        subheading = Label(master=self.top_headings_frame, text=menu_subheading_text,
                           font=("Raleway", "10"), bg="#2B2B2B", fg="white",
                           width=80)
        subheading.pack(pady=(10, 0))

    def menu_middle_frame(self):
        """Middle Proximity: Button Operators Frame Function (Row 0-5)"""

        self.middle_operators_frame.grid(row=1, column=0, rowspan=2, padx=10, pady=0)

        recent_label = Label(master=self.middle_operators_frame, text="Recent Incorrect Answers",
                             font=("Raleway", "10",), bg="#242424", fg="white",
                             wraplength=420)
        recent_label.grid(row=0, column=0, pady=0)

        # Correct Answers Frame
        corrected_answers_frame = Frame(self.root, padx=10, pady=10, bg="#242424")
        corrected_answers_frame.grid(row=2, column=0, rowspan=2, padx=10, pady=(72, 0))

        # Iterates Over List
        for row_num, answer in enumerate(self.answers_list):
            answer_label = Label(master=corrected_answers_frame, text=answer,
                                 font=("Raleway", "8"), bg="#242424", fg="white",
                                 wraplength=80)
            answer_label.grid(row=row_num, column=0, padx=5, pady=0)

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
        """Bottom Proximity: Button Navigation Frame Function (Row 6)"""

        self.bottom_buttons_frame.grid(row=6, column=0, rowspan=4)

        # Return To Menu Button Link
        def return_to_menu_button_clicked():
            """Closes Exporting Menu and Opens Main Menu"""

            self.root.destroy()
            MathsMasterApp()

        # History & Export Link
        def export_answers_list():
            """Saves File's Name as .txt"""

            with open(self.filename, 'w') as file:
                for answer in self.answers_list:
                    file.write(answer + '\n')
                    self.file_naming.config(text=f"File Saved as '{self.filename}'")
                    self.file_naming.config(fg="#99FF99")

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
                """Given Validity, Saves File"""

                self.filename = self.filename + ".txt"
                export_answers_list()

        # Return To Menu Button
        return_to_menu_button = Button(master=self.bottom_buttons_frame, text="Return To Menu",
                                       font=("Raleway", "11", "bold"), fg="black", bg="white",
                                       height=1, width=16, relief="flat", command=return_to_menu_button_clicked)
        return_to_menu_button.grid(row=6, column=0, padx=8, pady=0)

        # Binds Escape Key with Return To Menu Button
        self.root.bind('<Escape>', lambda event: return_to_menu_button_clicked())

        # Export Button
        export_button = Button(master=self.bottom_buttons_frame, text="Export",
                               font=("Raleway", "11", "bold"), fg="black", bg="white",
                               height=1, width=16, relief="flat", command=naming_check)
        export_button.grid(row=6, column=1, padx=8, pady=10)

        # Binds Enter Key with Exporting Button
        self.root.bind('<Return>', lambda event: naming_check())


# Runs Math Master App
MathsMasterApp()
