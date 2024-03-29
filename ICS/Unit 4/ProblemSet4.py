# Import nessacary modules and defines variables
import random
easylist = ["black","crush","people","magenta","hard"]
mediumlist = ["heretic","women","phrase","guard","malding"] 
hardlist = ["paraphernalia","insurrection","judgement","easy","protection"]
wins = 0
games = 0

# Gameloop
while True:
  # Variables
  attempts = 5
  inputs = []
  # Loop for selecting the difficulty and selecting a word from that difficulties list
  while True:
    print("\n            H_A_N_G_M_A_N \n")
    difficulty = input("Input a difficulty (easy/medium/hard): ")
    if difficulty.lower() == "easy":
      word = easylist[random.randint(0,len (easylist)-1)]
      break
    elif difficulty.lower() == "medium":
      word = mediumlist[random.randint(0,len(mediumlist)-1)]
      break
    elif difficulty.lower() == "hard":
      word = hardlist[random.randint(0,len(hardlist)-1)]
      break
    else:
      print("Invalid Input \n")
  # Creates a list of dashes the length of the selected word
  word2 = ["_" for i in list(word) if i not in inputs]
  # Loop for running the game
  while True:
    # Prints all visual information
    print("\n\n            H_A_N_G_M_A_N")
    print(" ".join(word2))
    print("\n"," ".join(inputs),"\n",sep="")
    print(attempts,"incorrect guesses remaining")
    # Takes a guess from the user
    guess = input("Guess a letter: ").lower()
    # Checks the users guess and acts accordingly
    if guess in inputs or guess.isalpha() == False or len(guess) != 1:
      print("\nInvalid Input")
      continue
    else:
      inputs.append(guess)
      # Remakes the dashes including guessed letters.
      for i in range (len(word)):
        if word[i] in inputs:
          word2[i] = word[i]
      if guess not in list(word):
        attempts -= 1
      if attempts < 0 or word2.count("_") == 0:
        break
  if attempts < 0: 
    print("\nGood attempt the word was", word,"\n")
    games += 1
  else:
    print("\nCongratz you got the word \n")
    wins += 1
    games += 1
  # Loop for asking the player to play again. It checks their input and acts accordingly.
  while True:
    playagain = input("Would you like to play again? (y/n): ")
    if playagain.lower() == "y":
      break
    elif playagain.lower() == "n":
      print("You won",wins,"out of",games,"games. Goodbye!")
      quit()
    else:
      print("\nInvalid Input")
      continue