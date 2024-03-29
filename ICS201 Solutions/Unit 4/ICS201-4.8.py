# 1. Create a dictionary with the following keys and values: {a : 1, b : 2, d : 4, g : 7, j: 10} Get a letter from input.  If it is one of the letters in the dictionary, output the corresponding value.  If it is not, output -1.
# Create a dictionary assigning letters numerical values.
letterdictionary = {"a" : 1, "b" : 2, "d" : 4, "g" : 7, "j": 10}
# Get a userinput
userinput = input("In: ")
# Convert the userinput into numbers using the dictionary
if userinput in letterdictionary:
  print(letterdictionary[userinput])
# If it's impossible print "-1"
else:
  print("-1")

# 2. Ask the user for 5 ages and names and assign them to a dictionary. Output the dictionary.
print("\n",{input(f"Name #{i+1}: "):int(input(f"Age #{i+1}: ")) for i in range(5)},sep="")