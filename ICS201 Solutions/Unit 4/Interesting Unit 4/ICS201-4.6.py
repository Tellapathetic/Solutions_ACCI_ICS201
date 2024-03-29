# bored

# Part 1
# Create a list and a copy of the list
list = [int(input("In: ")) for i in range (3)]
list2 = list.copy()
# Adds 0 to the second list
list2.insert(0,0)
# Prints the 2 lists
print(list)
print(list2)

# Part 2
# Creates a sorted list
list = [input("In: ") for i in range (4)]
# Sorts and Reverses the list
list.sort()
list.reverse()
# Prints the list reverse
print(list)