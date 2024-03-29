# 1. The variable _word_ holds a string from user input do the following tests:
word = input("In: ")
if word.endswith("ey"):
  print("-eys")
elif word.endswith("y"):
  print("-ies")
elif word.endswith("ife"):
  print("-ives")
else:
  print("-s")

# 2.The variable _num_ holds an integer user input write a conditional statement that does the following:
number = int(input("In: "))
if number < 0:
  print(f"{number} is negative") 
elif number > 0:
  print(f"{number} is positive")