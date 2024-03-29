# 1.  Ask the user for an integer.  If they supply you with an integer, multiply it by two and output it.  If they do not, output "Invalid Input"
try:
  num = float(input("In: "))
except:
  print("Invalid Input")
else:
  if num % 1 == 0:
    print(int(2 * num))
  else:
    print("Invalid Input")

# 2. Ask the user for a word.  If they supply you with only letters, output the word followed by " is your word"  Otherwise, output "Invalid Input"
word = input("In: ")
if word.isalpha():
  print(f"{word} is your word")
else:
  print("Invalid Input")

# 3. Ask the user for a word.  Check if it starts and ends with the same letter. Output the word if it is, otherwise output the word followed by " does not start and end with the same letter"  Ensure that the word is only letters.  If it is not, output "Invalid Input"
word = input("In: ")
if word.isalpha():
  if word[0] != word[-1]:
    print(f"{word} does not start and end with the same letter")
  else:
    print(word)
else:
  print("Invalid Input")

# 4. Ask the user for a word.  Check if it is all lowercase, all uppercase, a mix or all spaces.  Output the result to the user.  Output "Invalid Input" if it is not all letters or spaces.
word = input("In: ")
if word.isalpha():
  if word.isspace():
    print("all spaces")
  elif word.isupper():
    print("all uppercase")
  elif word.islower():
    print("all lowercase")
  else:
    print("mixed")
else:
  print("Invalid Input")