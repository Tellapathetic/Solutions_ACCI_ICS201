# bored  

# Part 1
# Create list with all user inputs
list = [input(f"In #{i+1}: ") for i in range (int(input("In: ")))]
# Print an edited list that removes odd indice elements.
print(" ".join([list[i] for i in range (len(list)) if i % 2 == 0]))

# Part 2
# Ask for 6 inputs and creates a list
list = [int(input("In: ")) for i in range (6)]
# Prints the even numbers in that list
print(" ".join([str(i) for i in list if i %2==0]))

# Part 3
# Asks for 4 inputs and creates a list
list = [input("In: ") for i in range (4)]
# Checks if "hello" is in the list and prints accordingly
if "hello" in list:
  print("true")
else:
  print("false")