
# Bored

# Part 1
# Asks for a positive integer until it recieves one
while True:
  integer = input("Input a positive integer: ")
  if int(integer) >= 0:
    break
# Prints that integer multiplied by 2
print(int(integer)*2)

# Part 2
# Asks for 2 equal inputs
while True:
  Password = input("Input a password: ")
  Confirm = input("Confirm the password: ")
  if Password == Confirm:
    # Prints "success." when it receives valid inputs
    print("success.")
    break

# Part 3
# Asks for an integer and a multiple of that integer
while True:
  Integer = input("Input an integer: ")
  Multiple = input("Input an integer that is a multiple of the first integer: ")
  if int(Multiple) % int(Integer) == 0:
    # prints "success." when it receives valid inputs
    print("success.")
    break
  