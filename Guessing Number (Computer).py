#"Guess the Number" (Computer)
import random

def computer_guess():
    print("Think of a number between 1 and 100.")
    low = 1
    high = 100
    attempts = 0

    while True:
        attempts += 1
        guess = random.randint(low, high)
        print(f"\nComputer's guess: {guess}")

        user_response = input("Is your number (h)igher, (l)ower, or is the guess (c)orrect? ").lower()

        if user_response == "h":
            low = guess + 1
        elif user_response == "l":
            high = guess - 1
        elif user_response == "c":
            print(f"\nYay! Computer guessed the number in {attempts} attempts.")
            break
        else:
            print("Invalid input. Please enter h, l, or c.")

computer_guess()


