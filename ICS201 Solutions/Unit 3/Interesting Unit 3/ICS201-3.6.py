# Bored

import random

# Part 1
# prints 5 random numbers between 50 and 100
for i in range (5):
  print(random.randint(50,100))

# Part 2
# prints a random float from 40-70, excluding 50-60.
while True:
  a = random.uniform(40, 70)
  if a <= 60 and a >= 50:
    continue
  else:
    print(a)
    break

# Part 3
#If the user inputs any number other than 0 it prints a random integer between 0 and 100. Repeats until 0 is entered.
while True:
  a = int(input("In: "))
  if a == 0:
    break
  else:
    print(random.randint(0,100))