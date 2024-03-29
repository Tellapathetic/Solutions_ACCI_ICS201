# Bored

# Part 1
# Ask for a positive number and repeats the question if a negetave number is inputed. 
while True:
  integer = input("In: ")
  if int(integer) >= 0:
    # Prints every even integer between 0 and that number.
    for i in range ((int(integer)+2)//2):
      if i == (int(integer)//2):
        print(2*i)
      else:
        print(2*i, end = '')
    break


# Part 2
# Ask for a positive integer. if it's negetive will output nothing.
while True:
  integer = int(input("In: "))
  if int(integer) >= 0:
    # Prints every integer less than the input starting from the input and ending at 0 
    while integer > 0:
      print(integer-1, end = "")
      integer -= 1
    break
