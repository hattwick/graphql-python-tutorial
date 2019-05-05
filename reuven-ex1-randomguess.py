# Python Workouts with Reuven
# Exercises 1.2.1 - Random Integer Guess
# Tested in Python3.7 variants

import random

answer = random.randint(0, 100)

while True:
    user_guess = int(input("What is your guess? "))  # out of bounds value is a fatal error
    print(f"Test value = {answer}")

    if user_guess == answer:
        print(f"Correct! The answer is {user_guess}")
        break

    else:
        print(f"Sorry. The answer was {answer}")
        print("Try again.")