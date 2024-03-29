# Bored

# Part 1
# Create list
list = [int(input("In: ")) for i in range (5)]
# Delete List item #3
del list[2]
# Output
print(list)

# Part 2
# Create list
list = [input("In: ") for i in range (5)]
# Append new list item
list.append(input("Extra In: "))
# Output
print(list)

# Part 3
# Create list
list = [float(input("In: ")) for i in range (4)]
del list[list.index(float(input("Remove Value: ")))]
# Output
print(list)

# Part 4
# Create list
list = [int(input("In: ")) for i in range (4)]
# Output
print(list[2:4])