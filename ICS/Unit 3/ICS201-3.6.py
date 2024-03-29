# Import
import random

# 1. Output a random integer from 50-100 5 times.
print(random.randint(50,100))
print(random.randint(50,100))
print(random.randint(50,100))
print(random.randint(50,100))
print(random.randint(50,100))

# 2. Output a random float from 40-70, excluding 50-60.
while True:
  randomfloat = random.uniform(40,70)
  if randomfloat <= 60 and randomfloat >= 50:
    continue
  else:
    print(randomfloat)
    break

# 3. Ask the user for an integer. Output a random integer from 0-100. Repeat until the user enters 0.
while int(input("In: ")) != 0:
  print(random.randint(0,100))