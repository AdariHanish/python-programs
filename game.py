import random

print("Welcome to the Number Guessing Game!")

secret_number = random.randint(1, 100)
guesses_taken = 0

while guesses_taken < 6:
    print("Guess a number between 1 and 100:")
    guess = int(input())

    guesses_taken += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        break  # Correct guess

if guess == secret_number:
    print("Congratulations! You guessed the number in", guesses_taken, "guesses!")
else:
    print("Sorry, you ran out of guesses. The number was", secret_number)
