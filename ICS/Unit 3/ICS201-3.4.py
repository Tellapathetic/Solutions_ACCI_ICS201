# Given N numbers: the first number in the input is N, after that N integers are given. Count the number of zeros among the given integers and print it.
# Empty List to store # of 0s
zerolist = []
# For loop for N length
for i in range(int(input("In: "))):
  # Append the number of 0s in each input into the empty list.
  zerolist.append(input(f"In #{i+1}: ").count("0"))
# Print the sum of the list
print(sum(zerolist))