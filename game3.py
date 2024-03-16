import random

def play_game():
  """
  Plays a round of Rock-Paper-Scissors against the computer.

  Returns:
      None
  """

  # Available options for the computer
  options = ["rock", "paper", "scissors"]

  # Get user input
  user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

  # Check for valid input
  if user_choice not in options:
    print("Invalid choice. Please choose rock, paper, or scissors.")
    return

  # Computer chooses randomly
  computer_choice = random.choice(options)

  # Determine the winner
  if user_choice == computer_choice:
    print("It's a tie!")
  elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
  else:
    print("You lose!")

  # Reveal the computer's choice
  print("The computer chose:", computer_choice)

# Main game loop
while True:
  play_game()

  # Ask if the user wants to play again
  play_again = input("Play again? (y/n): ").lower()
  if play_again != "y":
    break

# Exit message
print("Thanks for playing!")
