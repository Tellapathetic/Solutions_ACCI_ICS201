# Import necessary libraries
import random, os
# Define Variables
values,games,wins,iteration = [[" "," "," ",],[" "," "," ",],[" "," "," ",]],0,0,0
# Defining a function to print the board
def map():
  os.system("clear")
  print("Tic-Tac-Toe".center(20))
  print("      |     |\n   ",values[0][0],"  |  ",values[0][1],"  |  ",values[0][2],"\n _____|_____|_____\n      |     |\n   ",values[1][0],"  |  ",values[1][1],"  |  ",values[1][2],"\n _____|_____|_____\n      |     |\n   ",values[2][0],"  |  ",values[2][1],"  |  ",values[2][2],"\n     "," |     |  ", sep="")
# Defining a function to ask the player to play again
def outcome2(score,text):
  global games,wins
  games,wins = games + 1, wins + score
  map()
  print(text,f"\nOut of {games} games you have won {wins}")
  while True:
    playagain = input("Would you like to play again? ")
    if playagain == "yes" or playagain == "no":
      return playagain
    else:
      map()
      print(text,f"\nOut of {games} games you have won {wins}\nInvalid Input")    
# Defining a function to check if a player won
def outcome(score,text):
  if values[1][1] != " " and values[1][1] == values[0][0] and values[1][1] == values[2][2]:
    return outcome2(score,text)
  if values[1][1] != " " and values[0][2] == values[1][1] and values[1][1] == values[2][0]:
    return outcome2(score,text)
  for i in range (3):
    if values[0][i] != " " and values[1][i] == values[0][i] and values[0][i] == values[2][i]:
      return outcome2(score,text)
    if values[i][0] != " " and values[i][1] == values[i][0] and values[i][0] == values[i][2]:
      return outcome2(score,text)
# Draw the board
map()
while True:
  while True:
    # Ask the player for a column from the board and applies checks
    while True:
      x = input("Select a column: (1/2/3): ")
      try:
        x = int(x)
        if x > 3 or x < 1:
          raise
      except:
        map()
        print("Invalid Input")
        continue
      map()
      break
    # Ask the player for a row from the board and applies checks 
    while True:
      y = input("Select a row (1/2/3): ")
      try:
        y = int(y)
        if y > 3 or y < 1:
          raise
      except:
        map()
        print("Invalid Input")
        continue
      break
    # Checks to see if the selected space has already been taken
    if values[y-1][x-1] != " ":
      map()
      print("That spot is already taken")
      continue
    # Assigns the space to the player
    else:
      values[y-1][x-1] = "X"
      iteration += 1
      break
  # Checks if the player has won and acts accordingly
  playagain = outcome(1,"Good Game, you won!")
  if playagain == "no":
    os.system("clear")
    print("Goodbye!")
    break
  elif playagain == "yes": 
    values = [[" "," "," ",],[" "," "," ",],[" "," "," ",]]
    map()
    continue
  # Checks if a draw has occured and acts accordingly
  if iteration > 4:
    playagain = outcome2(0,"Looks like a draw!")
    if playagain == "no":
      os.system("clear")
      print("Goodbye!")
      break
    elif playagain == "yes": 
      values = [[" "," "," ",],[" "," "," ",],[" "," "," ",]]
      map()
      continue
  # Has an advanced neural network known as RNG select a space to be taken.
  while True:
    robotx,roboty = random.randint(0,2), random.randint(0,2)
    if values[roboty][robotx] != " ":
      continue
    else:
      values[roboty][robotx] = "O"
      map()
      break
  # Checks if the robot has won and acts accordingly
  playagain = outcome(0,"Good Game, but the robot won!")
  if playagain == "no":
    os.system("clear")
    print("Goodbye!")
    break
  elif playagain == "yes":
    values = [[" "," "," ",],[" "," "," ",],[" "," "," ",]]
    map()