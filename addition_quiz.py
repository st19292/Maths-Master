# Project: Maths Master - Quiz Interface
# Component 2.2: Finished Visual Interface
# 14052023: Finalized Layout


# Classes Importing
from tkinter import *
'''GUI Python Module'''


# Maths Master Quiz Interface
class QuizInterface:
    def __init__(self):
        """Initializes Math Master Instance"""

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
        menu_heading_text = "Addition Quiz"
        main_heading = Label(master=self.top_headings_frame, text=menu_heading_text,
                             font=("Raleway", "20", "bold"), bg="#2B2B2B", fg="white",
                             width=30)
        main_heading.pack(pady=(10, 0))

        menu_subheading_text = "Question 2 of 10"
        subheading = Label(master=self.top_headings_frame, text=menu_subheading_text,
                           font=("Raleway", "10"), bg="#2B2B2B", fg="white",
                           width=80)
        subheading.pack(pady=(10, 0))

    def menu_middle_frame(self):
        """Middle Proximity: Quiz Interface Frame Function"""

        # Middle Proximity, Quiz Choice (Row 1-2)
        self.middle_quiz_frame.grid(row=1, column=0, rowspan=2)

        # Quiz Questions Heading
        addition_text = Label(master=self.middle_quiz_frame, text="77 + 33",
                              font=("Raleway", "35", "bold"), bg="#242424", fg="white",
                              width=10)
        addition_text.grid(row=2, column=0)

        # Entry Feedback
        feedback_text = Label(master=self.middle_quiz_frame, text="Correct!",
                              font=("Raleway", "8"), bg="#242424", fg="#99FF99",
                              width=10)
        feedback_text.grid(row=3, column=0)

        # Entry Feedback
        name_entry = Entry(master=self.middle_quiz_frame, font=("Raleway", "12"), width=18, justify=CENTER)
        name_entry.grid(row=4, column=0)

    def menu_bottom_frame(self):
        """Bottom Proximity: Button Navigation Frame Function"""

        # Bottom Proximity, Footer Navigation (Row 3)
        self.bottom_buttons_frame.grid(row=3, column=0, rowspan=4)

        # Help & Info Button Link
        def return_to_menu_button_clicked():
            """Testing Button"""
            print("Help & Info Button clicked!")

        # History & Export Link
        def next_question_button_clicked():
            """Testing Button"""
            print("History & Export Button clicked!")

        # Help & Info Button
        return_to_menu_button = Button(master=self.bottom_buttons_frame, text="Return To Menu",
                                       font=("Raleway", "11", "bold"), fg="black", bg="white",
                                       height=1, width=16, relief="flat", command=return_to_menu_button_clicked)
        return_to_menu_button.grid(row=3, column=0, padx=8, pady=10)

        # History & Export Button
        next_question_button = Button(master=self.bottom_buttons_frame, text="Next Question",
                                      font=("Raleway", "11", "bold"), fg="black", bg="white",
                                      height=1, width=16, relief="flat", command=next_question_button_clicked)
        next_question_button.grid(row=3, column=1, padx=8, pady=10)


QuizInterface()
