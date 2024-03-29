# Basic Calculator
# Imports a necessary library that allows for different operations
import operator

# User input
equation = input("In: ")

# Creates a dictionary for the operators using the library
dictionary = {
  "+": operator.add, 
  "-": operator.sub, 
  "/": operator.floordiv,
  "%": operator.mod,
  "*": operator.mul,
}
# Does a bunch of checks on the input
if equation.isdecimal() or equation.isalpha() or equation.count(" ") != 0:
  print("Invalid Input")
else:
  # Loops through the dictionary
  try:
    for i in dictionary:
      # Finds the operator the equation uses
      if equation.count(i) == 1:
        # Defines the 2 numbers in the equation
        A = int(equation.split(i)[0])
        B = int(equation.split(i)[1])
        # Checks to make sure there are no negative numbers
        if A < 0 or B < 0:
          print("Invalid Input")
          break
        # Prints the result
        else:
          print(f"The result is {dictionary.get(i)(A, B)}.")
          break
      elif equation.count(i) > 1:
        print("Invalid Input")
  # If it runs into any errors it prints "Invalid Input"
  except:
    print("Invalid Input")
