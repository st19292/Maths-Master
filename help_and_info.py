# Project: Maths Master
# Component 3.3: Finished Component
# 14052023: Added Openable Window via Button & Quit


# Classes Importing
from tkinter import *
'''GUI Python Module'''


# Maths Master Main Menu
class MathsMasterApp:
    def __init__(self):
        """Initializes Math Master Instance"""

        self.root = Tk()
        self.root.title("Maths Master: Help & Info")
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
        menu_heading_text = "Help & Information"
        main_heading = Label(master=self.top_headings_frame, text=menu_heading_text,
                             font=("Raleway", "20", "bold"), bg="#2B2B2B", fg="white",
                             width=30)
        main_heading.pack(pady=(10, 0))

        menu_subheading_text = "Need help? Have a read on how to use the Math Master GUI."
        subheading = Label(master=self.top_headings_frame, text=menu_subheading_text,
                           font=("Raleway", "10"), bg="#2B2B2B", fg="white",
                           width=80)
        subheading.pack(pady=(10, 0))

    def menu_middle_frame(self):
        """Middle Proximity: Button Operators Frame Function"""

        # Middle Proximity, Quiz Choice (Row 1-2)
        self.middle_operators_frame.grid(row=1, column=0, rowspan=2)

        # Addition Text
        help_and_info_text = ("This program helps you improve your basic math skills. "
                              "Choose from addition, subtraction, multiplication, or "
                              "division to take a quiz. Each quiz has 10 random questions. \n\n"
                              "If you get a question wrong, you can view your history of " 
                              "incorrect answers and export them for future review.")
        help_and_info = Label(master=self.middle_operators_frame, text=help_and_info_text,
                              font=("Raleway", "10",), bg="#242424", fg="white",
                              wraplength=420)
        help_and_info.grid(row=2, column=0, pady=10)


    def menu_bottom_frame(self):
        """Bottom Proximity: Button Navigation Frame Function"""

        # Bottom Proximity, Footer Navigation (Row 3)
        self.bottom_buttons_frame.grid(row=3, column=0, rowspan=4)

        # Return To Menu Button Link
        def return_to_menu_button_clicked():
            """Testing Button"""

            # Creates Window
            window = Tk()
            window.title("Maths Master")
            window.configure(bg="#242424")

            # Primary Headers Frame
            headings_frame = Frame(master=window, padx=10, pady=10, bg="#2B2B2B")
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

            # Quit Button
            quit_window = Button(window, text="Quit", font=("Raleway", "11", "bold"), fg="black", bg="white",
                                      height=1, width=16, relief="flat", command=window.destroy)
            quit_window.grid(row=1, column=0)

            # Displays GUI
            window.mainloop()


        # Help & Info Button
        return_to_menu_button = Button(master=self.bottom_buttons_frame, text="Return To Menu",
                                      font=("Raleway", "11", "bold"), fg="black", bg="white",
                                      height=1, width=16, relief="flat", command=return_to_menu_button_clicked)
        return_to_menu_button.grid(row=3, column=0, padx=8, pady=10)


MathsMasterApp()
