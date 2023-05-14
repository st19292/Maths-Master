# Classes Importing
from tkinter import *
'''GUI Python Module'''

from PIL import Image, ImageTk
'''GUI Images Added'''


# Creates Window
root = Tk()
root.title("Addition Quiz")
root.resizable(False, False)
root.configure(bg="#242424")


# Top Proximity, Header (Row 0)

# Primary Headers Frame
headings_frame = Frame(master=root, padx=10, pady=10, bg="#2B2B2B")
headings_frame.grid(row=0, column=0)

# Main & Subheading Labels
menu_heading_text = "Addition Quiz"
main_heading = Label(master=headings_frame, text=menu_heading_text,
                     font=("Raleway", "20", "bold"), bg="#2B2B2B", fg="white",
                     width=30)
main_heading.pack(pady=(10, 0))

menu_subheading_text = "Question 1 of 10"
subheading = Label(master=headings_frame, text=menu_subheading_text,
                   font=("Raleway", "10"), bg="#2B2B2B", fg="white",
                   width=80)
subheading.pack(pady=(10, 0))


# Middle Proximity, Addition Quiz Interface (Row 1-2)

# Addition Quiz Frame
addition_quiz_frame = Frame(root, bg="#242424", padx=10, pady=40)
addition_quiz_frame.grid(row=1, column=0, rowspan=2)


# Question Heading
addition_text = Label(master=addition_quiz_frame, text="77 + 33",
                      font=("Raleway", "35", "bold"), bg="#242424", fg="white",
                      width=10)
addition_text.grid(row=2, column=0)


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
