# Bored

#Part 1
integer = input("In: ")
try:
  integer = int(integer)
except:
  print("Invalid Input")
else:
  print(2 * integer)

#Part 2
word = input("In: ")
if word.isalpha() == True:
  print(word, "is your word")
else:
  print("Invalid Input")


#Part 3
word2 = input("In: ")
if word2.isalpha() == False:
  print("Invalid Input")
elif word2[0] == word2[len(word2) - 1]:
  print(word2)
else:
  print(word2, "does not start and end with the same letter")

#Part 4
word3 = input("In: ")
if word3.isalpha() == False:
  print("Invalid Input")
elif word3.isspace() == True:
  print("all spaces")
elif word3.islower() == True:
  print("all lowercase")
elif word3.isupper() == True:
  print("all uppercase")
else:
  print("mixed")
