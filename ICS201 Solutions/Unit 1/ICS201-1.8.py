# 1. Create two Booleans called bool1 which is assigned to True, and bool2 that is assigned to False. Output the result of them being ANDed together, then output the result of them being ORed together. Output these results on different lines.
bool1 = True
bool2 = False
print(bool1 and bool2)
print(bool1 or bool2)

# 2. Ask the user, "Enter an integer: ". Check if the integer is NOT 0. If it isn't, output True. Otherwise output False.
integer = int(input("Enter an integer: "))
if integer != 0:
  print(bool1)
else:
  print(bool2)


# 3. Ask the user, "Enter a number: ". Check if the number is between 0 and 10 (Inclusively). Output True if it is. False otherwise.
num = float(input("Enter a number: "))
if num <= 10 and num >= 0:
  print(bool1)
else:
  print(bool2)

# 4. Ask the user to "Input food: ". Then ask them to "Input drink: ". If they input pizza and pop as their inputs, Output False. Otherwise output True.
food = input("Input food: ")
drink = input("Input drink: ")
if food == "pizza" and drink == "pop":
  print(bool2)
else:
  print(bool1)
  
# 5. Ask the user, “Enter an integer: ” Input the user’s response from the keyboard, test the integer to see if it is even (use the modulus operator % and 2 to do this), and then output the result as shown below (several runs are shown):
integer = int(input("Enter an integer: "))
if integer % 2 == 0:
  print("The integer",integer,"is True")
else:
  print("The integer",integer,"is False")
  