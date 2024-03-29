# 1. Output the boolean value True
print(True)

# 2. Ask the user, "Input an integer: ". Output True when the input is larger than 5. False when it is not.
integer = int(input("Input an integer: "))
if integer > 5:
  print(True)
else:
  print(False)

# 3. Ask the user, "Input the letter a:". Output True when the input is a. Output False when it is not.
letter = input("Input the letter a: ")
if letter == "a":
  print(True)
else:
  print(False)

# 4. Ask the user, "Input a word earlier in the dictionary than google: ". Output True when the input is earlier in the dictionary than google. Output False when it is not.
word = input("Input a word earlier in the dictionary than google: ")
if word >= "google":
  print(False)
else:
  print(True)

# 5. Ask the user, "Input an integer: ". Ask the user, "Input another integer: ". Output "Your numbers multiplied together are greater than 40: ", Followed by the True if they multiply to be greater than 40, False if they do not.
num1 = int(input("Input an integer: "))
num2 = int(input("Input another integer: "))
if num1 * num2 > 40:
  print("Your numbers multiplied together are greater than 40: True")
else:
  print("Your numbers multiplied together are greater than 40: False")