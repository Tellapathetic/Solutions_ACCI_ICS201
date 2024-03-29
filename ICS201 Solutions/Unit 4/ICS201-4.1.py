# 1. Ask the user for 5 integers, store them inside a list. Remove the 3rd element. Output the list.
# Create an empty list
intlist = []
# Append 5 user inputs to the list
for i in range (5):
  intlist.append(int(input("In: ")))
# Delete the 3rd value in the list
del intlist[2]
# Print the list
print(intlist)

# 2. Ask the user for 5 Strings, store them inside a list. Ask for 1 more input and append it to the list. Output the list.
# Create an empty list
strlist = []
# Append 5 user inputs to the list
for i in range (5):
  strlist.append(input("In: "))
# Append 1 more value
strlist.append(input("Extra In: "))
# Print the list
print(strlist)

# 3. Ask the user for 4 float, store them inside a list. Ask the user for a value to remove. Remove the first instance of that value. Output the list.
# Create an empty list
floatlist = []
# Append 4 user inputs to the list
for i in range (4):
  floatlist.append(float(input("In: ")))
# Remove an input from the list that has the same value as the new user input
floatlist.remove(float(input("Remove Value: ")))
# Print the list
print(floatlist)

# 4. Ask the user for 4 integers, store them inside a list. Output the last 2 integers ONLY.
# Create an empty list
intlist = []
# Append 4 user inputs to the list
for i in range (4):
  intlist.append(int(input("In: ")))
# Print the last 2 inputs in the list
print(intlist[2:4])