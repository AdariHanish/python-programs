import random

def get_word():
  """
  Reads a random word from a text file.

  Returns:
      A random word from the text file, or None if there's an error.
  """

  try:
    with open("words.txt", "r") as f:
      words = f.readlines()
      return random.choice(words).strip()
  except FileNotFoundError:
    print("Error: 'words.txt' file not found. Please create a file with words to play.")
    return None

def play_game():
  """
  Plays a round of word guessing with hints.
  """

  # Get a random word from the file
  word = get_word()
  if word is None:
    return

  # Convert the word to lowercase and hide it with dashes
  hidden_word = "-" * len(word)

  # Game variables
  guesses_remaining = 6
  guessed_letters = set()

  while guesses_remaining > 0 and hidden_word != word:
    print("Hidden word:", hidden_word)

    # Display used letters
    if guessed_letters:
      print("Used letters:", ", ".join(guessed_letters))

    # Get user guess
    guess = input("Guess a letter (or 'hint' for a hint): ").lower()

    # Check if valid input
    if len(guess) != 1 and guess not in ("hint", "h"):
      print("Invalid input. Please enter a single letter or 'hint'.")
      continue

    # Hint functionality
    if guess in ("hint", "h"):
      # Provide a hint (e.g., first/last letter, word category)
      hint_type = random.choice(["first", "last", "category"])
      if hint_type == "first":
        hint = f"The first letter is '{word[0]}'."
      elif hint_type == "last":
        hint = f"The last letter is '{word[-1]}'."
      else:
        # Replace with logic to provide a category hint based on the word (if applicable)
        hint = "Hint unavailable for this word yet."
      print(hint)
      continue

    # Check if guess already used
    if guess in guessed_letters:
      print(f"You already guessed '{guess}'. Try again.")
      continue

    # Update used letters
    guessed_letters.add(guess)

    # Check if guess is in the word
    correct_guesses = 0
    for i, letter in enumerate(word):
      if letter == guess:
        hidden_word = hidden_word[:i] + guess + hidden_word[i + 1:]
        correct_guesses += 1

    if correct_guesses > 0:
      print(f"Correct! '{guess}' is in the word.")
    else:
      guesses_remaining -= 1
      print(f"Incorrect. You have {guesses_remaining} guesses remaining.")

  # Game outcome
  if hidden_word == word:
    print("Congratulations! You guessed the word:", word)
  else:
    print("You ran out of guesses. The word was:", word)

# Main game loop
while True:
  play_game()

  # Ask if the user wants to play again
  play_again = input("Play again? (y/n): ").lower()
  if play_again != "y":
    break

# Exit message
print("Thanks for playing!")
