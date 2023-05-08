# Classess Importing
from tkinter import *
'''GUI Python Module'''

# Creates Window
maths_master = Tk()
maths_master.title("Maths Master")
maths_master.geometry("350x350")
maths_master.configure(bg="#242526")

# Main & Subheading
main_heading = Label(text = "Maths Master", 
                    font = ("Gill Sans Ultra Bold", "20"), bg = "#242526", fg = "white",
                    width = "20", height = "2")
main_heading.pack()

subheading = Label(text = "Test your maths knowledge through choosing a basic facts challenge!", 
                font = ("Gill Sans MT", "10"), bg = "#242526", fg = "white",
                width = "80", height = "2")
subheading.pack()



'''
main_heading = Label(top_frame, text = "Frame", width = "20", height = "4", font = ("Arial", "20", "bold"))
main_heading.pack(fill=X)
'''

# Displays GUI
maths_master.mainloop()
