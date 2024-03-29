# Bored

# Necessary Imports
import random

# Some Variables
games = 0
wins = 0
gameloop = True


# Welcome Message
print("Welcome to pick a number!")

# Game Loop
while gameloop:
  # Generates a random number between 1 and 10
  number = random.randint(1,10)  
  
  # Takes the user input and runs it through various checks.
  try:
    # Ensures the input is a number
    guess = int(input("Pick a number from 1-10: "))
    
    # Ensures the input is between 1 and 10
    if guess > 10 or guess < 1:
      raise
    
  # If the input is invalid it states it and continues to the next iteration of the game loop
  except:
    print("Sorry that input was not valid.")
    continue

  # If the user input is valid it moves on to checking if the user gets a point 
  else:
  # Checks if the random number and guess are the same and rewards points and increases the game #
    if number == guess:
      games += 1
      wins += 1
      print(f"The number was {number}.  You got a point! \nCurrent Score: {wins}")

  # If they are not the same it does not reward points but the game # counter still increases
    else:
      games += 1
      print(f"The number was {number}.  Sorry you didn't get a point. \nCurrent Score: {wins}")
      
  # Asks the user if they would like to play again and responds according to their input
    while True:
      playagain = input("Would you like to play again (Enter yes or no)? ").lower()
      if playagain == "yes":
        break
      elif playagain == "no":
        print(f"You got {wins} out of {games} games correct.")
        gameloop = False
        break
      else:
        print("Sorry that input was not valid.")