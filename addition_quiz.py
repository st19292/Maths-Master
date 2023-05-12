# Classes Importing
from tkinter import *
'''GUI Python Module'''

from PIL import Image, ImageTk
'''GUI Images Added'''


# Creates Window
root = Tk()
root.title("Addition Quiz")
root.resizable(False, False)
root.geometry('500x550')
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

question_number = 1
subheading_text = f"Question Number {question_number}"
subheading = Label(master=headings_frame, text=subheading_text,
                   font=("Raleway", "10"), bg="#2B2B2B", fg="white",
                   width=80)
subheading.pack(pady=(10, 0))


# Middle Proximity, Quiz Interface (Row 1-2)

# Quiz Interface Frame
headings_frame = Frame(master=root, padx=10, pady=10, bg="#2B2B2B")
headings_frame.grid(row=1, column=0)

# Main & Subheading Labels
menu_heading_text = "77 + 33"
main_heading = Label(master=headings_frame, text=menu_heading_text,
                     font=("Raleway", "40", "bold"), bg="#2B2B2B", fg="white",
                     width=30)
main_heading.pack(pady=(10, 0))



# Displays GUI
root.mainloop()
