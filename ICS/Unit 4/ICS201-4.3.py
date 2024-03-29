# 1. Ask the user for number of integers integers and store them in a list. Find and output all its elements with even **indices** (i.e. A[0], A[2], A[4], ...) on the same line with a space between them.
# Create an empty list
list = []
# Ask the user for an integer and run the for loop for that many iterations.
for i in range (int(input("In: "))):
  # if the iteration is divisable by 2 record the user input
  if i % 2 == 0:
    list.append(input(f"In #{i+1}: "))
  # if not store the input in a unused variable to be rewritten
  else:
    worthless = input(f"In #{i+1}: ")
# Print the list
print(" ".join(list))



# 2. Ask the user for 6 integers and store them in a list. Output all the elements with even values on the same line with a space between them. Use a for-loop that iterates over the list itself and not over its indices. 
# Create an empty list
list = []
# Append 6 integers to the list
for i in range (6):
  list.append(input("In: "))
# Remove odd integers from the list
# Create a new empty list
list2 = []
# If an integer from the first list is divisable by 2 add it to the second list
for i in list:
  if int(i) % 2 == 0:
    list2.append(i)
# Print the second list
print(" ".join(list2))

# 3. Ask the user for 4 Strings and store them in a list. Output true if one of the strings is "hello", false otherwise.
# Create a list with 4 user inputted strings.
list = [input("In: "), input("In: "), input("In: "), input("In: ")]
# If one of the inputs is "hello" print true
if "hello" in list:
  print("true")
# Otherwise print false
else:
  print("false")