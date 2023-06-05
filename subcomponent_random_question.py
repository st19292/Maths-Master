# Project: Maths Master - Quiz Interface Randomizer Subcomponent
# Component 2.2.4: Finished Quiz Program Draft
# 14052023: Draft Layout for all Operators


# Classes Importing
import random
'''Randomizer Module'''


# Randomizes Two Number from 1 to 25
number_one = random.randint(1, 25)
number_two = random.randint(1, 25)

# Answer Set as their Sum
answer = number_one + number_two


while True:
    """Main Loop Input"""

    # Try Except until Correct User Input
    try:
        user_answer = float(input(f"What is {number_one} + {number_two}: "))

        # Notes Input as Correct or Incorrect
        if user_answer == answer:
            print("Correct!")
            break
        else:
            print(f"Incorrect, the answer is {answer}!")

    # Addresses Invalid Input
    except ValueError:
        print("Invalid input. Please enter a valid number.")

    # Given Unknown Error, Addresses
    except Exception as e:
        print(f"An error occurred: {str(e)}")


"""
import random

number_one = random.randint(1, 25)
number_two = random.randint(1, 25)

answer = number_one - number_two

while True:
    try:
        user_answer = float(input(f"What is {number_one} - {number_two}: "))
        if user_answer == answer:
            print("Correct!")
            break
        else:
            print(f"Incorrect, the answer is {answer}!")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
"""


"""
import random

number_one = random.randint(1, 25)
number_two = random.randint(1, 25)

answer = number_one * number_two

while True:
    try:
        user_answer = float(input(f"What is {number_one} x {number_two}: "))
        if user_answer == answer:
            print("Correct!")
            break
        else:
            print(f"Incorrect, the answer is {answer}!")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
"""


"""
import random

number_one = random.randint(1, 25)

# Adds Difficulty & Preventing Simple Prime Numbers Questions
number_one_divisor = [i for i in range(1, number_one + 1) if number_one % i == 0]
number_two = random.choice(number_one_divisor)

answer = number_one / number_two

while True:
    try:
        user_answer = float(input(f"What is {number_one} ÷ {number_two}: "))
        if user_answer == answer:
            print("Correct!")
            break
        else:
            print(f"Incorrect, the answer is {answer}!")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
"""
