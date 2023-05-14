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
