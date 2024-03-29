# Bored
import random

# Part 1
# User inputs string
string = input("In: ")
# Output random letter
print(string[random.randint(0,len(string)-1)])

# Part 2
print(random.randint(int(input("In #1: ")),int(input("In #2: "))))

# Part 3
while True:
  # User inputs integer
  integer = int(input("In: "))
  # Checks if the input is 0
  if integer == 0:
    break 
  # Output random digit
  print(str(integer)[random.randint(0,len(str(integer))-1)])