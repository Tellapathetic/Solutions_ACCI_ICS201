#Bored

side1 = float(input("Input a number: "))
side2 = float(input("Input a number: "))
side3 = float(input("Input a number: "))


if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
  print("No Triangle")
elif side1 == side2 and side1 == side3:
  print("Equilateral")
elif side1 == side2 or side1 == side3 or side2 == side3:
  print("Isosceles")
else:
  print("Scalene")
