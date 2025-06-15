"""
This first exercise is designed to get your fingers warmed up for the rest of the book. It also introduces a number of topics that will repeat themselves over your Python career: loops, user input, converting types, and comparing values.

- Write a function (guessing_game) that takes no arguments.
- When run, the function chooses a random integer between 0 and 100 (inclusive).
- Then ask the user to guess what number has been chosen.
- Each time the user enter a guess, the program indicates one of the following
    - Too high.
    - Too low.
    - Just right.
- If the user guesses correctly, the program exits. Otherwise, the user is asked to try again.
- The program only exits after the user guesses correctly.
"""
from random import randint

def guessing_game():
    secret_number = randint(0, 100)

    while (True):
        guess = input("Enter number: ")

        if guess.isnumeric():
            guess = int(guess)
            if guess > secret_number:
                print("Too high.")
            elif guess < secret_number:
                print("Too low.")
            else:
                print("Just right.")
                break
        else:
            continue

if __name__ == '__main__':
    guessing_game()
