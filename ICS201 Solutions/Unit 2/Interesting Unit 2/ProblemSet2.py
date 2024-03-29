# Bored
# Here I import a library
import operator

# Start off with the input statement. Then I create a dictionary with acceptable operations. This utilizes the imported library
problem, operatordictionary = input("In: "), {"+": operator.add, "-": operator.sub, "//": operator.floordiv, "%": operator.mod, "*": operator.mul,}

# Here it finds out how many times each operator appears in the problem
operatorcount = [problem.count(list(operatordictionary.keys())[i]) for i in range (len(list(operatordictionary.keys())))]

  # It then uses the catalogue to determine possible invalid inputs
if sum(operatorcount) != 1 or problem.startswith("-") == True or problem.count(" ") != 0: 
  print("Invalid Input.")
else:
  # Then it prints the result
  try:
    #The 300 character print statement
    print("The result is ", operatordictionary[(list(operatordictionary.keys())[operatorcount.index(1)])]([int(i) for i in problem.split(list(operatordictionary.keys())[operatorcount.index(1)])][0],[int(i) for i in problem.split(list(operatordictionary.keys())[operatorcount.index(1)])][1]),".", sep="")
  except:
    print("Invalid Input.")

# Recap of what I learned through this problem set
# 1. I should use shorter variable names and create new variables to simplify (keyword: "should")
# 2. What the operator library is