# bored
# Part 1
# Create a dictionary and a variable storing a user input 
dictionary = {"a" : 1, "b" : 2, "d" : 4, "g" : 7, "j": 10}
letter = input("In: ")
# If the input is in the dictionary print the value that corresponds with that key
if letter in dictionary:
  print(dictionary[letter])
# If the input is not in the dictionary print "-1"
else:
  print(-1)

# Part 2
# Creates a dictionary
dictionary = {}
# User assigns values to the dictionary
for i in range (5):
  name = input(f"Name #{i+1}: ")
  dictionary[name] = int(input(f"Age #{i+1}: "))
# Prints the dictionary
print("\n",dictionary,sep="")