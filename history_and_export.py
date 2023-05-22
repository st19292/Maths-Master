# Project: Maths Master
# Component 4.24: Export Entry
# 22052023: Export Entry with None


# Classes Importing
from tkinter import *
'''GUI Python Module'''


# Maths Master Main Menu
class MathsMasterApp:
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

        answers_list = ['21 + 5 = 26', '11 + 11 = 22', '1 + 13 = 14', '16 + 21 = 37', '7 + 22 = 29', 
                        '1 + 2 = 3', '13 + 23 = 36', '20 + 22 = 42', '24 + 8 = 32', '18 + 19 = 37']

        # Iterates First Five in List
        for i in range(5):
            answer_label = Label(master=corrected_answers_frame, text=answers_list[i],
                                 font=("Raleway", "8"), bg="#242424", fg="white",
                                 wraplength=70)
            answer_label.grid(row=i + 1, column=0, padx=5, pady=0)
            """Iterates Next Number as Next Row"""

        # Iterates Last Five in List
        for i in range(5, 10):
            answer_label = Label(master=corrected_answers_frame, text=answers_list[i],
                                 font=("Raleway", "8"), bg="#242424", fg="white",
                                 wraplength=70)
            answer_label.grid(row=i - 4, column=1, padx=5, pady=0)
            """When i = 5, 5 - 4 is 1 for Row & Column 1"""

        # Export Entry Frame
        export_entry_frame = Frame(self.root, padx=10, pady=10, bg="#242424")
        export_entry_frame.grid(row=4, column=0, rowspan=2, padx=10, pady=(0, 0))

        # Heading
        file_naming = Label(master=export_entry_frame, text="Export Test",
                             font=("Raleway", "10",), bg="#242424", fg="white")
        file_naming.grid(row=4, column=0, pady=0)

        # The
        self.user_entry = Entry(master=export_entry_frame, font=("Raleway", "12"), width=18, justify=CENTER)
        self.user_entry.grid(row=5, column=0)

    def menu_bottom_frame(self):
        """Bottom Proximity: Button Navigation Frame Function"""

        # Bottom Proximity, Footer Navigation (Row 3)
        self.bottom_buttons_frame.grid(row=6, column=0, rowspan=4)

        # Return To Menu Button Link
        def return_to_menu_button_clicked():
            """Testing Button"""
            print("Return To Menu Button clicked!")

        # History & Export Link
        def export_button_clicked():
            """Testing Button"""
            print("Export Button clicked!")

        # Return To Menu Button
        return_to_menu_button = Button(master=self.bottom_buttons_frame, text="Return To Menu",
                                       font=("Raleway", "11", "bold"), fg="black", bg="white",
                                       height=1, width=16, relief="flat", command=return_to_menu_button_clicked)
        return_to_menu_button.grid(row=6, column=0, padx=8, pady=0)

        # Export Button
        export_button = Button(master=self.bottom_buttons_frame, text="Help & Info",
                               font=("Raleway", "11", "bold"), fg="black", bg="white",
                               height=1, width=16, relief="flat", command=export_button_clicked)
        export_button.grid(row=6, column=1, padx=8, pady=10)


MathsMasterApp()
