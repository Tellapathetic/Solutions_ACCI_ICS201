#Bored

#Part 1
print(True)

#Part 2
number = int(input("Input an integer: "))
if number > 5:
  print(True)
else:
  print(False)

#Part 3
character = input("Input the letter a: ")
if character.lower() == "a":
  print(True)
else:
  print(False)



#Part 4
word = input("Input a word earlier in the dictionary than google: ")
try:
    word = float(word)
except:
  word = word.strip().lower()
  if word >= "google":
    print(False)
  else:
    print(True)
else:
  print(False)

#Part 5
integer = int(input("Input an integer: "))
integer2 = int(input("Input another integer: "))
if integer * integer2 > 40:
  print("Your numbers multiplied together are greater than 40: True")
else:
  print("Your numbers multiplied together are greater than 40: False")