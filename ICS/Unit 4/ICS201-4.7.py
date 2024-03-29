# Create a variable to control the main loop and set it to true
loop = True
# Ask the user for a integer until an integer greater than 2 is inputted
while loop:
  usernumber = int(input("In: "))  
  if usernumber < 2:
    continue
  else:
    # Check to see if any number can divide the number without remainder
    for i in range (usernumber):
      if i < 2:
        continue
      else:
        # If a number like that is found print "not prime" break from the for loop and make the loop variable False
        if usernumber % i == 0:
          print("not prime")
          loop = False
          break
    else:
      # If a number isn't found print "prime" and make the loop variable False
      print("prime")
      loop = False