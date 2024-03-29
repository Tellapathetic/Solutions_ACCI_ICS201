# bored
# Asks for an input until it recieves an integer greater than 2
number = int(input("In: "))
while number < 2:
  number = int(input("In: "))
# Divides the input by every number greater than 1 but lower than it's self to find a factor
for i in range (2,number):
  # If a factor is found then it prints "not prime"
  if number % i == 0:
    print("not prime")
    break
else:
  # If it doesn't find a factor it prints "prime"
  print("prime")