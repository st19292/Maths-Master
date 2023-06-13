"""
Project: Maths Master - (Marc Mojica).

Assessment: AS91906 - Use complex programming techniques to develop a program.
Info: Improve Maths skills through quizzes and export answers for reviewing.
13062023: Changed Quiz Input Subheading
"""

# Class Imports: Tkinter Elements, Pillow Images, Randomizing & Date Acquiring
from tkinter import Tk, Frame, Label, Button, Canvas, Entry
from tkinter.constants import CENTER, END
from PIL import Image, ImageTk
import random
import datetime

# Styling & Numerical Constants
QUESTIONS = 10
MIN_RANGE = 0
MAX_RANGE = 12
MIN_NUM = 0
MAX_NUM = MAX_RANGE * MAX_RANGE
POSITION = "+10+10"
MAIN_FONT = "Raleway"
WHITE = "#F2F9FF"
GREY = "#242424"
RED = "#FF9999"
ORANGE = "#FFCA99"
GREEN = "#99FF99"
LIGHT_BLUE = "#DDEFFF"
DARK_BLUE = "#00213F"
ADD_TEXT_COLOUR = "#B8FFF4"
SUBTRACT_TEXT_COLOUR = "#84E5D6"
MULTIPLY_TEXT_COLOUR = "#9EDCF6"
DIVIDE_TEXT_COLOUR = "#67BBEB"


class MathsMasterApp:
    """Maths Master Main Menu."""

    def __init__(self):
        """Initializes Frame & Image Instances."""
        self.root = Tk()
        self.root.title("Maths Master")
        self.root.resizable(False, False)
        self.root.configure(bg=GREY)
        self.root.geometry(POSITION)
        self.root.focus_force()

        # Creates Top, Middle & Bottom Proximity Frame
        self.top_heading_frame = Frame(self.root, padx=10, pady=10, bg=GREY)
        self.middle_buttons_frame = Frame(self.root, bg=GREY, padx=10, pady=40)
        self.bottom_buttons_frame = Frame(self.root, bg=GREY, padx=10, pady=20)

        # Creates Image Instances for Operator Buttons
        self.add_img_path = "images/addition.png"
        add_img = Image.open(self.add_img_path)
        add_img = add_img.resize((70, 70))
        self.add_add_img = ImageTk.PhotoImage(add_img)

        self.subtract_img_path = "images/subtraction.png"
        subtract_img = Image.open(self.subtract_img_path)
        subtract_img = subtract_img.resize((70, 70))
        self.add_subtract_img = ImageTk.PhotoImage(subtract_img)

        self.multiply_img_path = "images/multiplication.png"
        multiply_img = Image.open(self.multiply_img_path)
        multiply_img = multiply_img.resize((70, 70))
        self.add_multiply_img = ImageTk.PhotoImage(multiply_img)

        self.divide_img_path = "images/division.png"
        divide_img = Image.open(self.divide_img_path)
        divide_img = divide_img.resize((70, 70))
        self.add_divide_img = ImageTk.PhotoImage(divide_img)

        # Calls Frames Methods, Elements & Displays GUI
        self.window_top_frame()
        self.window_middle_frame()
        self.window_bottom_frame()
        self.root.mainloop()

    def window_top_frame(self):
        """Top Proximity: Headings Frame Function."""
        self.top_heading_frame.grid(row=0, column=0)

        # Main & Subheading Labels
        heading_text = "Maths Master: Basic Facts Quiz"
        main_heading = Label(master=self.top_heading_frame, text=heading_text,
                             font=(MAIN_FONT, "20", "bold"),
                             bg=GREY, fg=WHITE, width=30)
        main_heading.pack(pady=(10, 0))

        subheading_text = "Test your Maths Skills by choosing a challenge!"
        subheading = Label(master=self.top_heading_frame, text=subheading_text,
                           font=(MAIN_FONT, "10"), bg=GREY,
                           fg=LIGHT_BLUE, width=80)
        subheading.pack(pady=(10, 0))

    def window_middle_frame(self):
        """Middle Proximity: Button Operators Frame Function (Row 1-2)."""
        self.middle_buttons_frame.grid(row=1, column=0, rowspan=2)

        # Runs Operator Quizzes
        def clicked_add_button(click):
            self.root.destroy()
            QuizInterface("+")

        def clicked_subtract_button(click):
            self.root.destroy()
            QuizInterface("-")

        def clicked_multiply_button(click):
            self.root.destroy()
            QuizInterface("*")

        def clicked_divide_button(click):
            self.root.destroy()
            QuizInterface("/")

        # Creates Addition Widget
        canvas_add = Canvas(master=self.middle_buttons_frame,
                            width=82, height=82, bg=GREY,
                            highlightthickness=0)
        canvas_add.grid(row=1, column=0)

        # Addition Text
        add_text = Label(master=self.middle_buttons_frame,
                         text="(1) Addition",
                         font=(MAIN_FONT, "7", "bold"),
                         bg=GREY, fg=ADD_TEXT_COLOUR, width=12)
        add_text.grid(row=2, column=0)

        # Sets Addition Command
        add_button = canvas_add.create_image(40, 40, image=self.add_add_img)
        canvas_add.tag_bind(add_button, "<Button>", clicked_add_button)
        self.root.bind('1', clicked_add_button)

        # Creates Subtraction Widget
        canvas_subtract = Canvas(master=self.middle_buttons_frame,
                                 width=82, height=82, bg=GREY,
                                 highlightthickness=0)
        canvas_subtract.grid(row=1, column=1)

        # Subtraction Text
        subtract_text = Label(master=self.middle_buttons_frame,
                              text="(2) Subtraction",
                              font=(MAIN_FONT, "7", "bold"),
                              bg=GREY, fg=SUBTRACT_TEXT_COLOUR, width=12)
        subtract_text.grid(row=2, column=1)

        # Sets Subtraction Command
        subtract_button = \
            canvas_subtract.create_image(40, 40, image=self.add_subtract_img)
        canvas_subtract.tag_bind(subtract_button,
                                 "<Button>", clicked_subtract_button)
        self.root.bind('2', clicked_subtract_button)

        # Creates Multiplication Widget
        canvas_multiply = Canvas(master=self.middle_buttons_frame,
                                 width=82, height=82, bg=GREY,
                                 highlightthickness=0)
        canvas_multiply.grid(row=1, column=2)

        # Multiplication Text
        multiply_text = Label(master=self.middle_buttons_frame,
                              text="(3) Multiplication",
                              font=(MAIN_FONT, "7", "bold"),
                              bg=GREY, fg=MULTIPLY_TEXT_COLOUR, width=12)
        multiply_text.grid(row=2, column=2)

        # Sets Multiplication Command
        multiply_button = \
            canvas_multiply.create_image(40, 40, image=self.add_multiply_img)
        canvas_multiply.tag_bind(multiply_button,
                                 "<Button>", clicked_multiply_button)
        self.root.bind('3', clicked_multiply_button)

        # Creates Division Widget
        canvas_divide = Canvas(master=self.middle_buttons_frame,
                               width=82, height=82, bg=GREY,
                               highlightthickness=0)
        canvas_divide.grid(row=1, column=3)

        # Division Text
        divide_text = Label(master=self.middle_buttons_frame,
                            text="(4) Division",
                            font=(MAIN_FONT, "7", "bold"),
                            bg=GREY, fg=DIVIDE_TEXT_COLOUR, width=12)
        divide_text.grid(row=2, column=3)

        # Sets Division Command
        divide_button = \
            canvas_divide.create_image(40, 40, image=self.add_divide_img)
        canvas_divide.tag_bind(divide_button,
                               "<Button>", clicked_divide_button)
        self.root.bind('4', clicked_divide_button)

    def window_bottom_frame(self):
        """Bottom Proximity: Button Navigation Frame Function (Row 3)."""
        self.bottom_buttons_frame.grid(row=3, column=0, rowspan=4)

        # Exit Program & Help/Info Button Link
        def clicked_exit_program_button():
            self.root.destroy()

        def clicked_help_and_info_button():
            self.root.destroy()
            HelpAndInfo()

        # Exit Program Button
        exit_program_button = Button(master=self.bottom_buttons_frame,
                                     text="(ESC) Quit",
                                     font=(MAIN_FONT, "11", "bold"),
                                     fg=DARK_BLUE, bg=LIGHT_BLUE,
                                     height=1, width=16, relief="ridge",
                                     command=clicked_exit_program_button)
        exit_program_button.grid(row=3, column=0, padx=8, pady=0)
        self.root.bind('<Escape>', lambda event: clicked_exit_program_button())

        # Help & Info Button
        help_and_info_button = Button(master=self.bottom_buttons_frame,
                                      text="(I) Help & Info",
                                      font=(MAIN_FONT, "11", "bold"),
                                      fg=DARK_BLUE, bg=LIGHT_BLUE,
                                      height=1, width=16, relief="ridge",
                                      command=clicked_help_and_info_button)
        help_and_info_button.grid(row=3, column=1, padx=8, pady=0)
        self.root.bind('<i>', lambda event: clicked_help_and_info_button())


class QuizInterface:
    """Quiz Interface Class Window."""

    def __init__(self, operator):
        """Initializes Frame & Quiz Variables."""
        self.root = Tk()
        self.root.title("Maths Master Quiz")
        self.root.resizable(False, False)
        self.root.configure(bg=GREY)
        self.root.geometry(POSITION)

        # Creates Top, Middle & Bottom Proximity Frame
        self.top_heading_frame = Frame(self.root, padx=10, pady=10, bg=GREY)
        self.middle_quiz_frame = Frame(self.root, bg=GREY, padx=10, pady=40)
        self.bottom_buttons_frame = Frame(self.root, bg=GREY, padx=10, pady=20)

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

        # Calls Frames Methods, Elements & Displays GUI
        self.window_top_frame()
        self.window_middle_frame()
        self.window_bottom_frame()
        self.generate_new_question()
        self.root.mainloop()

    def window_top_frame(self):
        """Top Proximity: Headings Frame Function."""
        self.top_heading_frame.grid(row=0, column=0)

        # Main & Subheading Labels
        heading_text = "Maths Master Quiz"
        main_heading = Label(master=self.top_heading_frame, text=heading_text,
                             font=(MAIN_FONT, "20", "bold"),
                             bg=GREY, fg=WHITE, width=30)
        main_heading.pack(pady=(10, 0))

        # Sets Question Number
        subheading_text = f"Question {self.question_number} of 10"
        self.subheading = Label(master=self.top_heading_frame,
                                text=subheading_text,
                                font=(MAIN_FONT, "10"),
                                bg=GREY, fg=LIGHT_BLUE, width=80)
        self.subheading.pack(pady=(10, 0))

    def window_middle_frame(self):
        """Middle Proximity: Quiz Interface Frame Function (Row 1-4)."""
        self.middle_quiz_frame.grid(row=1, column=0, rowspan=2)

        # Quiz Questions Heading
        self.operator_text = Label(master=self.middle_quiz_frame,
                                   text=self.question,
                                   font=(MAIN_FONT, "35", "bold"),
                                   bg=GREY, fg=WHITE, width=10)
        self.operator_text.grid(row=2, column=0)

        # Entry Feedback
        self.feedback_text = Label(master=self.middle_quiz_frame,
                                   text="Please type an answer",
                                   font=(MAIN_FONT, "9"),
                                   bg=GREY, fg=LIGHT_BLUE, width=50)
        self.feedback_text.grid(row=3, column=0)

        # Entry Feedback
        self.user_entry = Entry(master=self.middle_quiz_frame,
                                font=(MAIN_FONT, "12"),
                                width=18, justify=CENTER)
        self.user_entry.grid(row=4, column=0)
        self.user_entry.focus_force()

        # Runs Function for Question
        self.generate_new_question()

    def window_bottom_frame(self):
        """Bottom Proximity: Button Navigation Frame Function (Row 5)."""
        self.bottom_buttons_frame.grid(row=5, column=0, rowspan=4)

        # Help & Info Button Link
        def clicked_return_to_menu_button():
            """Closes Window."""
            self.root.destroy()
            MathsMasterApp()

        # Return To Menu Button
        return_to_menu_button = Button(master=self.bottom_buttons_frame,
                                       text="Return To Menu",
                                       font=(MAIN_FONT, "11", "bold"),
                                       fg=DARK_BLUE, bg=LIGHT_BLUE,
                                       height=1, width=16, relief="ridge",
                                       command=clicked_return_to_menu_button)
        return_to_menu_button.grid(row=5, column=0, padx=8, pady=10)
        self.root.bind('<Escape>',
                       lambda event: clicked_return_to_menu_button())

        # Submit Answer Button
        self.next_question_button = Button(master=self.bottom_buttons_frame,
                                           text="Submit Answer",
                                           font=(MAIN_FONT, "11", "bold"),
                                           fg=DARK_BLUE, bg=LIGHT_BLUE,
                                           height=1, width=16, relief="ridge",
                                           command=self.check_answer)
        self.next_question_button.grid(row=5, column=1, padx=8, pady=10)
        self.root.bind('<Return>', lambda event: self.check_answer())
        self.root.bind('<space>', lambda event: self.check_answer())

    def randomize_numbers(self):
        """Generates & Displays Two Random Numbers."""
        self.number_one = random.randint(MIN_RANGE, MAX_RANGE)
        self.number_two = random.randint(MIN_RANGE, MAX_RANGE)

        if self.operator == "+":
            """Sets Heading Question & Correct Answer."""
            self.question = f"{self.number_one} + {self.number_two}"
            self.answer = self.number_one + self.number_two

        elif self.operator == "-":
            """Generates New Question Until Answer Greater Than a Negative."""
            while True:
                self.number_one = random.randint(MIN_RANGE, MAX_RANGE)
                self.number_two = random.randint(MIN_RANGE, MAX_RANGE)
                self.question = f"{self.number_one} - {self.number_two}"
                self.answer = self.number_one - self.number_two

                if self.answer >= 0:
                    break

        elif self.operator == "*":
            self.question = f"{self.number_one} × {self.number_two}"
            self.answer = self.number_one * self.number_two

        else:
            number_one_divisor = [i for i in range(1, self.number_one + 1)
                                  if self.number_one % i == 0]
            """Sets Whole Numbers as Answers."""
            if number_one_divisor:
                self.number_two = random.choice(number_one_divisor)

            else:
                """Handles Empty Divisor."""
                self.number_two = 1

            self.question = f"{self.number_one} ÷ {self.number_two}"
            self.answer = self.number_one // self.number_two

    def generate_new_question(self):
        """Generates New Numbers & Updates as New Question."""
        self.randomize_numbers()
        self.operator_text.config(text=self.question)

        # Clears Entry Box
        self.user_entry.delete(0, END)

        # Updates Question Number
        subheading_text = f"Question {self.question_number} of 10"
        self.subheading.config(text=subheading_text)
        self.question_number += 1

        # Disables Button if 10 Question Iterated
        if self.question_number > QUESTIONS + 1:
            self.subheading.config(text="Quiz Finished")
            self.next_question_button.config(state="disabled")

            if len(self.incorrect_list) == 0:
                self.root.destroy()
                MathsMasterApp()

            else:
                self.root.destroy()
                HistoryAndExport(self.incorrect_list)

    def check_answer(self):
        """Checks User Input as Correct, Incorrect, or Invalid."""
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

            # Compares Correct Answer & User Input to Mark
            if user_answer == correct_answer:
                self.feedback_text.config(text=f"Correct: {operation_str} "
                                               f"is {correct_answer}")
                self.feedback_text.config(fg=GREEN)

            elif user_answer < MIN_NUM:
                self.feedback_text.config(text=f"Number too small, "
                                               f"please enter a "
                                               f"bigger number.")
                self.feedback_text.config(fg=ORANGE)
                self.user_entry.delete(0, END)
                return

            elif user_answer > MAX_NUM:
                self.feedback_text.config(text=f"Number too big, "
                                               f"please enter a "
                                               f"smaller number.")
                self.feedback_text.config(fg=ORANGE)
                self.user_entry.delete(0, END)
                return

            else:
                self.feedback_text.config(text=f"Incorrect: {operation_str} is"
                                               f" {correct_answer}")
                self.incorrect_list.append(f"{operation_str} = "
                                           f"{correct_answer}")
                self.feedback_text.config(fg=RED)

            # If Integers Valid, Generates New Question
            self.generate_new_question()

        # Addresses Invalid Input
        except ValueError:
            self.feedback_text.config(text="Invalid input. "
                                           "Please enter a valid number.")
            self.feedback_text.config(fg=RED)
            self.user_entry.delete(0, END)

        # Given Unknown Error, Addresses
        except Exception as e:
            self.feedback_text.config(text=f"An error occurred: {str(e)}")
            self.feedback_text.config(fg=RED)
            self.user_entry.delete(0, END)


class HelpAndInfo:
    """Help And Info Class Window."""

    def __init__(self):
        """Initializes Frame Instances."""
        self.root = Tk()
        self.root.title("Maths Master: Help & Info")
        self.root.resizable(False, False)
        self.root.configure(bg=GREY)
        self.root.geometry(POSITION)
        self.root.focus_force()

        # Creates Top, Middle & Bottom Proximity Frame
        self.top_heading_frame = Frame(self.root, padx=10, pady=10, bg=GREY)
        self.middle_buttons_frame = Frame(self.root, bg=GREY, padx=10, pady=40)
        self.bottom_buttons_frame = Frame(self.root, bg=GREY, padx=10, pady=20)

        # Calls Frames Methods & Elements & Displays GUI
        self.window_top_frame()
        self.window_middle_frame()
        self.window_bottom_frame()
        self.root.mainloop()

    def window_top_frame(self):
        """Top Proximity: Headings Frame Function."""
        self.top_heading_frame.grid(row=0, column=0)

        # Main & Subheading Labels
        heading_text = "Help & Information"
        main_heading = Label(master=self.top_heading_frame, text=heading_text,
                             font=(MAIN_FONT, "20", "bold"), bg=GREY,
                             fg=WHITE, width=30)
        main_heading.pack(pady=(10, 0))

        subheading_text = "Need help? " \
                          "Have a read on how to use the Math Master GUI."
        subheading = Label(master=self.top_heading_frame, text=subheading_text,
                           font=(MAIN_FONT, "10"), bg=GREY,
                           fg=LIGHT_BLUE, width=80)
        subheading.pack(pady=(10, 0))

    def window_middle_frame(self):
        """Middle Proximity: Button Operators Frame Function (Row 1-2)."""
        self.middle_buttons_frame.grid(row=1, column=0, rowspan=2)

        # Help/Information Text
        help_and_info_text = ("This program helps you improve your basic math "
                              "skills. Choose from add, subtract, multiply, "
                              "or divide to take a quiz. Each quiz has 10 "
                              "random questions. \n\n"
                              "If you get a question wrong, you can view your "
                              "history of incorrect answers and export them"
                              " for future review.")
        help_and_info = Label(master=self.middle_buttons_frame,
                              text=help_and_info_text,
                              font=(MAIN_FONT, "10",),
                              bg=GREY, fg=LIGHT_BLUE, wraplength=420)
        help_and_info.grid(row=2, column=0, pady=10)

    def window_bottom_frame(self):
        """Bottom Proximity: Button Navigation Frame Function (Row 3)."""
        self.bottom_buttons_frame.grid(row=3, column=0, rowspan=4)

        # Return To Menu Button Link
        def clicked_return_to_menu_button():
            self.root.destroy()
            MathsMasterApp()

        # Help & Info Button
        return_to_menu_button = Button(master=self.bottom_buttons_frame,
                                       text="Return To Menu",
                                       font=(MAIN_FONT, "11", "bold"),
                                       fg=DARK_BLUE, bg=LIGHT_BLUE,
                                       height=1, width=16, relief="ridge",
                                       command=clicked_return_to_menu_button)
        return_to_menu_button.grid(row=3, column=0, padx=8, pady=10)
        self.root.bind('<Escape>',
                       lambda event: clicked_return_to_menu_button())


class HistoryAndExport:
    """History And Export Class Window."""

    def __init__(self, incorrect_list):
        """Initializes Frame & File Writing Instances."""
        self.root = Tk()
        self.root.title("Maths Master: History & Export")
        self.root.resizable(False, False)
        self.root.configure(bg=GREY)
        self.root.geometry(POSITION)

        # Creates Top, Middle & Bottom Proximity Frame
        self.top_heading_frame = Frame(self.root, padx=10, pady=10, bg=GREY)
        self.middle_buttons_frame = Frame(self.root, bg=GREY, padx=10, pady=40)
        self.bottom_buttons_frame = Frame(self.root, bg=GREY, padx=10, pady=20)

        # Sets Filename and Answers List
        self.filename = ""
        self.answers_list = incorrect_list
        self.file_naming = None
        self.user_entry = None

        # Calls Frames Methods & Elements & Displays GUI
        self.window_top_frame()
        self.window_middle_frame()
        self.window_bottom_frame()
        self.root.mainloop()

    def window_top_frame(self):
        """Top Proximity: Headings Frame Function."""
        self.top_heading_frame.grid(row=0, column=0)

        # Main & Subheading Labels
        heading_text = "History & Export"
        main_heading = Label(master=self.top_heading_frame, text=heading_text,
                             font=(MAIN_FONT, "20", "bold"),
                             bg=GREY, fg=WHITE,
                             width=30)
        main_heading.pack(pady=(10, 0))

        subheading_text = "Revise your wrong answers." \
                          "(When exporting, if file name " \
                          "already exists, it will be replaced)"
        subheading = Label(master=self.top_heading_frame, text=subheading_text,
                           font=(MAIN_FONT, "10"), bg=GREY, fg=LIGHT_BLUE,
                           width=80)
        subheading.pack(pady=(10, 0))

    def window_middle_frame(self):
        """Middle Proximity: Button Operators Frame Function (Row 0-5)."""
        self.middle_buttons_frame.grid(row=1, column=0,
                                       rowspan=2, padx=10, pady=0)

        recent_label = Label(master=self.middle_buttons_frame,
                             text="Recent Incorrect Answers",
                             font=(MAIN_FONT, "10",), bg=GREY, fg=LIGHT_BLUE,
                             wraplength=420)
        recent_label.grid(row=0, column=0, pady=0)

        # Correct Answers Frame
        corrected_answers_frame = Frame(self.root, padx=10, pady=10, bg=GREY)
        corrected_answers_frame.grid(row=2, column=0,
                                     rowspan=2, padx=10, pady=(72, 0))

        # Iterates Over List
        for row_num, answer in enumerate(self.answers_list):
            answer_label = Label(master=corrected_answers_frame, text=answer,
                                 font=(MAIN_FONT, "8"), bg=GREY, fg=LIGHT_BLUE,
                                 wraplength=80)
            answer_label.grid(row=row_num, column=0, padx=5, pady=0)

        # Export Entry Frame
        export_entry_frame = Frame(self.root, padx=10, pady=10, bg=GREY)
        export_entry_frame.grid(row=4, column=0,
                                rowspan=2, padx=10, pady=(0, 0))

        # Answers List Saving Heading
        self.file_naming = Label(master=export_entry_frame,
                                 text="Export Answers",
                                 font=(MAIN_FONT, "10",),
                                 bg=GREY, fg=LIGHT_BLUE)
        self.file_naming.grid(row=4, column=0, pady=0)

        # User Entry List
        self.user_entry = Entry(master=export_entry_frame,
                                font=(MAIN_FONT, "12"),
                                width=18, justify=CENTER)
        self.user_entry.grid(row=5, column=0)
        self.user_entry.focus_force()

    def window_bottom_frame(self):
        """Bottom Proximity: Button Navigation Frame Function (Row 6)."""
        self.bottom_buttons_frame.grid(row=6, column=0, rowspan=4)

        # Return To Menu Button Link
        def clicked_return_to_menu_button():
            """Closes Exporting Menu and Opens Main Menu."""
            self.root.destroy()
            MathsMasterApp()

        # History & Export Link
        def export_answers_list():
            """Saves File's Name as .txt."""
            with open(self.filename, 'w') as file:
                for answer in self.answers_list:
                    file.write(answer + '\n')
                    self.file_naming.config(text=f"File Saved as"
                                                 f" '{self.filename}'")
                    self.file_naming.config(fg=GREEN)

        def naming_check():
            """Validate Filename Input."""
            self.filename = self.user_entry.get()

            if not self.filename:
                """Saves File as Current Time."""
                current_date = datetime.datetime.\
                    now().strftime("%d-%m-%Y_%H-%M-%S")
                self.filename = current_date + "_answers_list.txt"
                export_answers_list()

            elif any(not c.isalnum() and c != '_' for c in self.filename):
                """Restricts Saving File with Special Characters."""
                self.file_naming.config(text="No Special "
                                             "Characters or Spaces!")
                self.file_naming.config(fg=RED)

            else:
                """Given Validity, Saves File."""
                self.filename = self.filename + ".txt"
                export_answers_list()

        # Return To Menu Button
        return_to_menu_button = Button(master=self.bottom_buttons_frame,
                                       text="Return To Menu",
                                       font=(MAIN_FONT, "11", "bold"),
                                       fg=DARK_BLUE, bg=LIGHT_BLUE,
                                       height=1, width=16, relief="ridge",
                                       command=clicked_return_to_menu_button)
        return_to_menu_button.grid(row=6, column=0, padx=8, pady=0)
        self.root.bind('<Escape>',
                       lambda event: clicked_return_to_menu_button())

        # Export Button
        export_button = Button(master=self.bottom_buttons_frame, text="Export",
                               font=(MAIN_FONT, "11", "bold"),
                               fg=DARK_BLUE, bg=LIGHT_BLUE,
                               height=1, width=16,
                               relief="ridge", command=naming_check)
        export_button.grid(row=6, column=1, padx=8, pady=10)
        self.root.bind('<Return>', lambda event: naming_check())


# Runs Math Master App
MathsMasterApp()
