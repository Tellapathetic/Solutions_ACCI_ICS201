# For given integer n ≤ 9 print a ladder of n steps. The k-th step consists of the integers from 1 to k without spaces between them.
# This input is the # of steps
steps = int(input("In: "))
# This variable is what is printed in every iteration of the for loop
currentstep = ""
# This if gate checks if the # of steps is less than 9
if steps <= 9:
  # Prints each step through a for loop
    [print("".join([str(x+1) for x in range (i+1)])) for i in range (steps)]