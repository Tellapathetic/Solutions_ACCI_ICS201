# Bored
import math
import random
# I took my code from 1.4 because it's fundamentally the same thing
def question(wording, AnswerType):
  #Wording is the question it asks and type is the type of response it can accept
  
  #The second arg can be 3 things an Integer, A real number, or a positive real number. Represented by the inputs "int" "float" and "+float"
  typelist = [int,float,"+float"]
  if AnswerType not in typelist:
    print("the function is called incorrectly, automatically exporting a random value")
    return str(random.randint(0, 100))
  #This just forces you to actually input something
  while (True):
    answer = str(input(wording))
    answer = answer.strip()
    isspace = answer.isspace()
    
    if isspace == True or answer == "":
      print("That's not an acceptable answer friendo")
      continue

#Now it justs makes sure the answer is acceptable within the parameters of the question
    if AnswerType != typelist [2]:
      try:
        answer = AnswerType(answer)
      except:
        print("That is not an acceptable answer, make sure you follow the instructions")
        continue
      else:
        break
    elif AnswerType == typelist[2]:
      if float(answer) < 0:
        print("Sorry, no numbers below zero")
        continue
      else:
        break
  #After you input an acceptable answer it returns what you wrote 
  #just without any extra spaces
  return str(answer)

#Math with floats is the worst, it's never accurate

#Part 1
input1 = question("Input an integer: " ,int)
input1 = int(input1)
output1 = input1 + 3
print(output1)

#Part 2
input2 = question("Input a number: ",float)
input2 = input2.rstrip("0").rstrip(".")
input2 = str(input2) + "4"
input2 = float(input2)
output2 = input2 + 2
print(output2)

#Part 3
input3 = question("Input a radius: ","+float")
input3 = float(input3)
output3 = input3 * input3 * 3.14
print(output3)

#Part 4
input4 = question("Input a number: ",float)
input4 = float(input4)
output4 = input4 * 12
print(math.trunc(output4))

#Part 5
input5 = question("Input an integer: ",int)
input5 = int(input5)
output5 = input5 + 5
print("Your number + 5 is {var}".format(var = output5))
