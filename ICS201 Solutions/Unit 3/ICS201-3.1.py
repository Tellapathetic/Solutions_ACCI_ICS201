# 1. Ask the user to input an integer. Write a while loop that will print out the numbers starting at 1 and ending at the input inclusive.  The numbers printed should all be on the same line separated by a space.The last number should not have a space after it and should have a new line.
# Variables
uno = 1
dos = int(input("In: "))
# If statement that checks if the input is less than or equal to 0
if dos > 0:
  # While Loop that prints the numbers
  while dos > uno:
    print(uno, end = " ")
    uno +=1
  else:
    print(uno)

# 2. Ask the user to input an integer.Write a while loop that will print out the numbers starting at 0 and ending at twice the end number exclusive.  Each number should be on the same line, separated by a space. The last number should not have a space after it and should have a new line. Sample inputs/outputs:
# Variables
cero = 0
dos = int(input("In: "))
# If statement that checks if the input is less than or equal to 0
if dos >= 0:
  # While Loop that prints the numbers
  while 2*dos > cero+1:
    print(cero, end = " ")
    cero +=1
  else:
    print(cero)