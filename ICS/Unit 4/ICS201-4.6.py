# 1. Ask the user for 3 integers. Store them in a list Copy the list. Insert the integer value 0 at the first index. Output both lists
# Create a list with 3 user-inputted integers
list = [int(input("In: ")),int(input("In: ")),int(input("In: "))]
# Make a copy of the list
copylist = list.copy()
# Insert the integer value 0 at the first index.
copylist.insert(0,0)
# Output both lists
print(list)
print(copylist)

# 2. Ask the user for 4 Strings. Store them in a list Sort the list. Reverse the list. Output the list
# Ask the user for 4 strings and store them in a list
list = [input("In: "),input("In: "),input("In: "),input("In: ")]
# Sort the list
list.sort()
# Reverse the list
list.reverse()
# Output the list
print(list)