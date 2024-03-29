# 1. Ask the user for an integer N. Ask the user for N strings. Store the strings in a list. Output the second last index in the list. (Remember indexes work the same way for lists as they did for strings)
# Create an empty list
list = []
# Ask the user for an integer N. Ask the user for N strings to append.
for i in range (int(input("In: "))):
  list.append(input(f"In #{i+1}: "))
# Print the second last input
print(list[-2])

# 2. Ask the user for floats until they enter 0. Store them in a list (including the zero). Ask the user for 3 strings. Store them in a list. Combine the lists. (This can be done by using + between two lists). Output the new list. Output the length of the list.
# Create an empty list
floatlist = []
# Append float values to the list until 0 is inputted
while True:
  floatyfloat = float(input("In: "))
  floatlist.append(floatyfloat)
  if floatyfloat == 0:
    break
# Add 3 strings to the list
combolist = floatlist + [input("In: "),input("In: "),input("In: ")] 
# Print the list
print(combolist)
# Print the length of the list
print(len(combolist))