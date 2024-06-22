def get_user_input(message):
  while True:
    try:
      number = float(input(message))
      return number
    except ValueError:
      print("Invalid input. Please enter a number.")
def add(x, y):
  return x + y
def subtract(x, y):
  return x - y
def multiply(x, y):
  return x * y
def perform_calculation():
  num1 = get_user_input("Enter the first number: ")
  num2 = get_user_input("Enter the second number: ")
  operation = input("Choose operation (+, -, *): ")
  if operation == "+":
    result = add(num1, num2)
    print(f"{num1} + {num2} = {result}")
  elif operation == "-":
    result = subtract(num1, num2)
    print(f"{num1} - {num2} = {result}")
  elif operation == "*":
    result = multiply(num1, num2)
    print(f"{num1} * {num2} = {result}")
  else:
    print("Invalid operation. Please choose +, -, or *.")
perform_calculation()
