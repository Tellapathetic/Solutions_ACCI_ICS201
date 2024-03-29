# bored

#Part 1
word = input("In: ")
if word.endswith("ey") == True:
  print("-eys")
elif word.endswith("y") == True:
  print("-ies")
elif word.endswith("ife") == True:
  print("-ives")
else:
  print("-s")

#Part 2
num = input("In: ")
if float(num) > 0:
  print(num,"is positive") 
elif int(num) < 0:
  print(num,"is negative")