# bored
# Part 1
# Creates a list
list = [int(input(f"In #{i+1}: ")) for i in range (5)]
# Prints the average of the list
print(sum(list)/len(list))
# Removes the first and last element
start = list.pop(0)
end = list.pop(-1)
# Readds the removed elements
list.append(start)
list.insert(0, end) 
# Prints the edited list
print(list)

# Part 2
# Creates a list
list = [input(f"In #{i+1}: ") for i in range (int(input("In: ")))]
# Prints the index of the value the user wants
print(list.index(input("In: ")))
# Prints the length of the list
print(len(list))