# 1.Create a list of integers with 5 elements from user input. Calculate the average of all the numbers in the array. Output the average. Swap the first and last element.
# Create a list with 5 integers
list = [int(input("In #1: ")),int(input("In #2: ")),int(input("In #3: ")),int(input("In #4: ")),int(input("In #5: "))]
# Print the average of the list
print(sum(list)/5)
# Swap the first and last element 
list.append(list.pop(0))
list.insert(0,list.pop(-2))
# Print the new list
print(list)

# 2. Ask the user for an integer N. Ask the user for N integers and store them in a list. Ask the user for a value. Output the first index of that value. Output the length of the list. (Use len to get).
# Create an empty list
list = []
# Ask the user for N integers and append them to the list.
for i in range (int((input("In: ")))):
  list.append(int(input(f"In #{i+1}: ")))
# Ask the user for a value. Output the first index of that value.
print(list.index(int(input("In: "))))
# Print the length of the list
print(len(list))
