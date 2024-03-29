# 1. Triangle Building
A = float(input("Input a number: "))
B = float(input("Input a number: "))
C = float(input("Input a number: "))

if A + B <= C:
  print("No Triangle")
elif A == B and A == C:
  print("Equilateral")
elif A == B or B == C or A == C:
  print("Isosceles")
else:
  print("Scalene")
