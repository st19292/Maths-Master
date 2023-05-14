import random

number_one = random.randint(0, 99)
number_two = random.randint(0, 99)

answer = number_one + number_two
user_answer = int(input(f"{number_one} + {number_two}"))

if user_answer == answer:
    print("Correct!")
else:
    print(f"Incorrect, the answer is {answer}!")
    