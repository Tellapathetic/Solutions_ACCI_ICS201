# 1. Even numbers less than a positive #
# Variable
positive = -1
# Asks for an input greater than 0 until it gets an input greater than 0
while positive <= 0:
  positive = int(input("In: "))
# Prints all even numbers less than or equal to the input
print("".join([str(i) for i in range (positive+1) if i%2==0]))

# 2. Decreasing Numbers
positive = -1
# Asks for an input greater than 0 until it gets an input greater than 0
while positive <= 0:
  positive = int(input("In: "))
# Prints all numbers less than the input
print("".join([str(positive-(i+1)) for i in range (positive)]))