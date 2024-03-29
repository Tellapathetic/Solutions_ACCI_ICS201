# Bored

output,x = "", int(input("In: ")) 
#Checks to make sure input is lower than or equal to 9
if x <= 9:
  for i in range (x):
    # Creates and prints a ladder of steps
    output = output + str(i+1)
    print(output)