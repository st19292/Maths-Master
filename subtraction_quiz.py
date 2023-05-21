# Project: Maths Master - Quiz Interface
# Component 2.26: 10 Questions Limit
# 21052023: Final, Questions Limited


# Classes Importing
from tkinter import *
'''GUI Python Module'''

import random
'''Randomizing Module'''


# Maths Master Quiz Interface
class QuizInterface:
    """Creates Class for Quiz Interface Window"""

    def __init__(self):
        """Initializes Math Master Instance"""

        # Sets Tkinter Window Settings
        self.root = Tk()
        self.root.title("Maths Master: Subtraction Quiz")
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
        self.subtraction_text = None
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
        menu_heading_text = "Subtraction Quiz"
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
        self.subtraction_text = Label(master=self.middle_quiz_frame, text=self.question, font=("Raleway", "35", "bold"),
                                      bg="#242424", fg="white", width=10)
        self.subtraction_text.grid(row=2, column=0)

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

            print("Help & Info Button clicked!")

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
        self.question = f"{self.number_one} - {self.number_two}"
        self.answer = self.number_one - self.number_two

    def generate_new_question(self):
        """Generates New Numbers & Updates as New Question"""

        # Calls New Numbers & Updates Question Heading
        self.random_numbers()
        self.subtraction_text.config(text=self.question)

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
                self.feedback_text.config(text=f"Correct: {self.number_one} - {self.number_two} is {self.answer}")
                self.feedback_text.config(fg="#99FF99")
            else:
                self.feedback_text.config(text=f"Incorrect: {self.number_one} - {self.number_two} is {self.answer}")
                self.incorrect_list.append(f"{self.number_one} - {self.number_two} = {self.answer}")
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


# Runs Program
QuizInterface()
