# Bored

# Prints the sum of a list comprehension
print(sum([input(f"In #{i+1}: ").count("0") for i in range (int(input("In: ")))]))