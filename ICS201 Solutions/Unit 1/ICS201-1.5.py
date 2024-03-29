# 1. Ask the user to "Input an integer: ". Store it in a variable, then convert to an integer. Add 3 to variable. Output the variable.
integer = input("Input an integer: ")
integer = int(integer)
print(integer + 3)

# 2. Ask the user to "Input a number: ". Store it in a variable. Concatenate the number 4 to the end. Convert it to a float. Add 2 to it. Output the variable.
number = input("Input a number: ")
number = number + "4"
number = float(number) + 2
print(number)

# 3. Ask the user to "Input a radius: ". Store it as a variable. Convert it to a float. Use the number as the radius to calculate the area of a circle and output it. Use 3.14 as the value for pi.
radius = input("Input a radius: ")
radius = float(radius)
print(radius * radius * 3.14)

# 4. Ask the user to "Input a number: ". Store it in a variable. Convert it to a float. Multiply its value by 12 then round the number down to the nearest whole number. Output the final value of the variable.
number = input("Input a number: ")
number = float(number)
print(int((number * 12) // 1))

# 5. Ask the user to "Input an integer: ". Store it in a variable. Convert it to an integer. Add 5 to it. Output "Your number + 5 is var". Replace var with your variable using placeholders.
integer = input("Input an integer: ")
integer = int(integer) + 5
print(f"Your number + 5 is {integer}")
