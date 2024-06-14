def create_star_letter(letter):
  """
  Creates a string representing a letter made of stars.

  Args:
      letter: The letter to be represented by stars (uppercase).

  Returns:
      A string containing the star representation of the letter.
  """

  star_patterns = {
      'A': """
      ***
     * *
    *****
   """,
      'B': """
     ****
    *   *
     ****
    *   *
     ****
   """,
      'C': """
     ****
    *    *
   *
    *    *
     ****
   """  }

  if letter not in star_patterns:
    return None  
  return star_patterns[letter]
n = lambda x: ''.join(create_star_letter(char) + '\n' for char in x.upper()) if x else ""
print(n("PYTHON"))
