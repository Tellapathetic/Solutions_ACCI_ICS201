import random

# 1. Ask the user for a String. Output a random letter from that string.
# Ask the user for a String.
userstr = input("In: ")
# Pick a random letter from that string
letter = random.randint(0,len(userstr)-1)
# Print that letter
print(userstr[letter])

# 2. Ask the user for an integer. Ask the user for a second integer. Output a random integer from the first integer to the second integer (inclusive).
# Ask the user for 2 integers
userint1 = int(input("In #1: "))
userint2 = int(input("In #2: "))
# Pick a random number between those 2 integers
randomint = random.randint(userint1,userint2)
# Print that number.
print(randomint)

# 3. Ask the user for an integer. Output a random digit from the integer. Repeat until the user enters 0.
while True:
  # Ask the user for a integer.
  userint = int(input("In: "))
  # If the input is 0 break from the loop
  if userint == 0:
    break
  # If not
  else:
    # Pick a random number from that integer.
    number = random.randint(0,len(str(userint))-1)
    # Print that number
    print(str(userint)[number])