from math import sqrt
def check_primality(num):
  if num <= 1:
    return False
  if num <= 3:
    return True
  if num % 2 == 0 or num % 3 == 0:
    return False
  i = 5
  while i * i <= num:
    if num % i == 0 or num % (i + 2) == 0:
      return False
    i += 6
  return True
def is_composite(num):
  if not check_primality(num):
    return True
  return False
number = int(input("enter a number:"))
if is_composite(number):
  print(number, "is a composite number.")
else:
  print(number, "is a prime number.")
