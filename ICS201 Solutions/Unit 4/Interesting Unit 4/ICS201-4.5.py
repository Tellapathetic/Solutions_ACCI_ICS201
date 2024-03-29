# bored

# Part 1
# prints the second last index of a list made up of N number of user inputted strings
print([input(f"In #{i+1}: ") for i in range (int(input("In: ")))][-2])

# Part 2
# Creates an empty list
list = []
# Appends user inputs to the empty list until 0 is inputted
while True:
  list.append(float(input("In: ")))
  if list[-1] == 0:
    break
# Adds 3 user inputted strings to the list
list += [input("In: ") for i in range (3)]
# Prints the list and the length of the list
print(list)
print(len(list))