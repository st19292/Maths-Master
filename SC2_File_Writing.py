# Subcomponent 4.2.3: Saving Conditions

# Classes
import datetime
"""Module Allows Date Retrieval"""


# Iterates & Stores Answers
def save_list():
    """Saves File's Name as .txt"""
    with open(filename, 'w') as file:
        for answer in answers_list:
            file.write(answer + '\n')


# Answers List
answers_list = ['21 + 5 = 26', '11 + 11 = 22', '1 + 13 = 14', '16 + 21 = 37', '7 + 22 = 29',
                '1 + 2 = 3', '13 + 23 = 36', '20 + 22 = 42', '24 + 8 = 32', '18 + 19 = 37']

# Custom Naming
filename = input("Enter the filename for the answers list: ")

# If Unnamed, Saves File as Date; Fails if Spaces/Special Characters
if not filename:
    current_date = datetime.datetime.now().strftime("%m-%d-%Y")
    filename = current_date + "_answers_list.txt"
    save_list()
elif any(not c.isalnum() for c in filename):
    print("No Special Characters or Spaces!")
