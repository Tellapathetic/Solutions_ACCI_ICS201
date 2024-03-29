# bored

# Import the random and os module
import random, os
# All the varibles required to run the game
wordlist,alphabet,wins,games,hangman,consent = [["Easy","loud","hello","yellow","picnic","sparrow"],["Medium","there is no i in gaslight","classic","diverse","income","percent"],["Hard","frazzled","wristwatch","xylophone","jaywalk","buzzwords"]],["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",],[0,0,0],[0,0,0],["  _________ \n    |     | \n    |    / \ \n    |    \_/ \n    |   \ | / \n    |    \|/ \n    |     | \n    |     | \n    |    / \ \n    |   /   \ \n    | \n____|____","  _________ \n    |     | \n    |    / \ \n    |    \_/ \n    |   \ | / \n    |    \|/ \n    |     | \n    |     | \n    |    /  \n    |   /    \n    | \n____|____","  _________ \n    |     | \n    |    / \ \n    |    \_/ \n    |   \ | / \n    |    \|/ \n    |     | \n    |     | \n    |      \n    |       \n    | \n____|____","  _________ \n    |     | \n    |    / \ \n    |    \_/ \n    |   \ |  \n    |    \| \n    |     | \n    |     | \n    |      \n    |       \n    | \n____|____","  _________ \n    |     | \n    |    / \ \n    |    \_/ \n    |     |  \n    |     | \n    |     | \n    |     | \n    |      \n    |       \n    | \n____|____","  _________ \n    |     | \n    |    / \ \n    |    \_/ \n    |       \n    |      \n    |      \n    |      \n    |      \n    |       \n    | \n____|____","  _________ \n    |      \n    |     \n    |     \n    |       \n    |      \n    |      \n    |      \n    |      \n    |       \n    | \n____|____"],"y"

# Print a welcome message
print("Welcome to Hangman! \n")

while consent == "y":
  # Define some variables
  guesses,tries = [],6
  # Have the player select the difficulty
  while True:
    difficulty = input("Please select a difficulty. (Enter 1/2/3) \n 1. Easy: Simple and short. \n 2. Medium: Middling in length and difficulty. \n 3. Hard: Very difficult puzzles \n You get 6 lives regardless of what difficulty you pick! \n \n")
    try:
      if int(difficulty) < 1 or int(difficulty) > 3:
        raise
      else:
        os.system("clear")
        break
    except:
      os.system("clear")
      print("That is not a valid input. \n")
  
  # Pick a word from the word list
  word = wordlist[int(difficulty)-1][random.randint(1,len(wordlist[int(difficulty)-1])-1)]
  
  # Create a variable with the same value as the selected word
  word2 = word
  # Change the "word2" variable into a series of "_"s
  for i in alphabet:
    if i not in guesses:
      word2 = word2.replace(i,"_")
  
  # Loop to run the game until you lose or the puzzle is completed
  while True:
    # Prints the gallows and the dashes and the previous Guesses
    print(hangman[tries],"                    ",word2,"\n \nGuesses: \n", " ".join(guesses), f"\nRemaining: {tries} \n")
    # Takes the user input for their guess
    guess = input("Make a guess: ").lower()
    # Run the guess through some checks
    if guess not in alphabet or guess in guesses:
      os.system("clear")
      print("That is not a valid input. \n")
      continue
    guesses.append(guess)
    if word.count(guess) == 0:
      tries -= 1
    # Redefine "word2" into "word"
    word2 = word
    # Change "word2" into a series of "_"s
    for i in alphabet:
      if i not in guesses:
        word2 = word2.replace(i,"_")
    if word2 == word or tries == 0:
      games[int(difficulty)-1] += 1
      if tries > 1:
        wins[int(difficulty)-1] += 1
      os.system("clear")
      break
    else:
      os.system("clear")
  # Loop to ask the player to play again.
  while True:
    print(hangman[tries],"                    ",word2,"\n \nGuesses: \n", " ".join(guesses), f"\nRemaining: {tries} \n")
    if tries < 1:
      print(f'Good Try! The word was "{word}" \nYou have {sum(wins)} wins out of {sum(games)} games')
    else: 
      print(f"Congratulations you beat the puzzle \nYou have {sum(wins)} wins out of {sum(games)} games")
    consent = input("Would you like to play again? (y/n): ").lower()
    if consent == "y" or consent == "n":
      os.system("clear")
      if consent == "n":
        print("Goodbye!")
      break
    else:
      os.system("clear")
      print("That is not a valid input.")