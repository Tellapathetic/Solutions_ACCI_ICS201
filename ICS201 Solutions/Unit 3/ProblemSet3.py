# Imports
import random

# Variables
Gs = 0
Ws = 0

# A Welcome Message to greet the user.
print("Welcome to pick a number!")

# Ask them to pick a number from 1-10.  If they give invalid input, ask again.
while True:
  try:
    UserInput = int(input("Pick a number from 1-10: "))
    if UserInput < 1:
      raise Exception
    elif UserInput > 10:
      raise Exception
  except:
    print("Sorry that input was not valid.")
    continue

  # Generate a random number.  Output the number to the user.
  random = random.randint(1,10) 
  # If they guessed correctly, give them a point.  If they did not, don't get them a point.
  if UserInput == random:
    Ws += 1
    Gs += 1
    print(f"The number was {random}.  You got a point!")
  else:
    Gs += 1
    print(f"The number was {random}.  Sorry you didn't get a point.")
  # Display their current score at the end of each round.
  print(f"Current Score: {Gs}")
  while True:
    # Ask the user if they would like to play again.  If they select yes, repeat the above steps (with the exception of the welcome message).
    UserInput = input("Would you like to play again (Enter yes or no)? ")
    if UserInput.lower() == "yes":
      break
    # If they select no, output their total score compared to how many game played.
    elif UserInput.lower() == "no":
      print(f"You got {Ws} out of {Gs} games correct.")
      break
    else:
      print("Sorry that input was not valid.")
  if UserInput.lower()=="no":
    break