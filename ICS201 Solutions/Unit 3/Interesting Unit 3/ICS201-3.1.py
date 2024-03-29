# Bored

# Part 1
integer = input("In: ")
i = 1
#While i is less than or equal to the inputted integer it prints i starting from 1
while i <= int(integer):
  if i == int(integer):
    print(i)
  else:
    print(i, end = " ")
  i += 1

# Part 2
integer = input("In: ")
i = 0
#While i is less than double the inputted integer it prints i starting from 0
while i < int(integer)*2:
  if i == int(integer)*2 - 1:
    print(i)
  else:
    print(i, end = " ")
  i += 1