#Bored
#Part 1
true = True
false = False
print(true and false)
print(true or false)

#Part 2
while (True):
  integer = input("Enter an integer: ")
  try:
    integer = int(integer)
  except:
    print("Not acceptable answer")
    continue
  else:
    break
if integer != 0:
  print(true)
else:
  print(false)


#Part 3
while (True):
  num = input("Enter a number: ")
  try:
    num = float(num)
  except:
    print("Not acceptable answer")
    continue
  else:
    break
if num <= 10 and num >= 0:
  print(true)
else:
  print(false)

#Part 4
food = input("Input food: ")
drink = input("Input drink: ")
if food.strip().lower() == "pizza" and drink.strip().lower() == "pop":
  print(false)
else:
  print(true)
  
#Part 5
while (True):
  integer2 = input("Enter an integer: ")
  try:
    integer2 = int(integer2)
  except:
    print("Not acceptable answer")
    continue
  else:
    break
if integer2 % 2 == 0:
  print("The integer",integer2,"is True")
else:
  print("The integer",integer2,"is False")
