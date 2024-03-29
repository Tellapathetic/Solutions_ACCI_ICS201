import math

# 1. Ask the user to "Input a number: ". Output the square root of the number. Output the result
num = float(input("Input a number: "))
print(math.sqrt(num))

# 2. Ask the user to "Input a number: ". Output the integer square root of the number. Output the result.
num = int(input("Input a number: "))
print(math.isqrt(num))

# 3. Ask the user to "Input a number: ". Round the number down to the nearest whole number. Output the result.
num = float(input("Input a number: "))
print(int(num//1))

# 4. Ask the user to "Input a number: ". Round the number up to the nearest whole number. Output the result.
num = float(input("Input a number: "))
print(math.ceil(num))

# 5. Ask the user to "Input a number: ". Ask the user to "Input another number: ". Multiply the two numbers together. Divide by 2. Then Round down to the nearest whole number. Output the result.
num = float(input("Input a number: "))
num1 = float(input("Input another number: "))
print((int(num*num1)//2))