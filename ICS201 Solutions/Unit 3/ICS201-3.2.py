# 1. Ask the user to "Input a positive integer: "   If the user inputs a negative number, ask them again for to "Input a positive integer: "  Once you have a positive number.  Output a the number multiplied by 2.
while True:
  # Ask for a positive integer until a positive number is inputted
  uno = int(input("Input a positive integer: "))
  if uno >= 0:
    # Print that number * 2
    print(2*uno)
    break

# 2. Password Creator
while True:
  # Checks if the 2 inputs are equal
  if input("Input a password: ") == input("Confirm the password: "):
    # If they are equal print "success" if not then ask for new inputs
    print("success.")
    break

# 3. Multiples
# While loop that checks if 2 inputs are equal
while True:
  # Takes the userinputs
  dos = int(input("Input an integer: "))
  uno = int(input("Input an integer that is a multiple of the first integer: "))
  # Checks if the second input is divisable by the first
  if uno % dos == 0:
    # If they are multiples print "success" if not then ask for new inputs
    print("success.")
    break