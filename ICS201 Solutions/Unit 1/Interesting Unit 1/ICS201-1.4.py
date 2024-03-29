#  Bored
#  The entire assignment I kind of just reused the same code over and over so I turned them into functions for simpler use
#  Most of what I did was outside the scope of the assignment, all I really needed was 1 or 2 input statements and then a print statement, but then capitalization bothered me so now this is 90 lines


def question(wording):
  #This just forces you to actually input something
  while (True):
    answer = str(input(wording))
    isspace = answer.isspace()
    if isspace == True or answer == "":
      print("That's not an answer friendo")
    else:
      break
  #After you input an acceptable answer it returns what you wrote 
  #just without any extra spaces
  return answer.strip()


def name_capitalization(name):
  List = name.split()
  output = ""
  #I could use .join() to turn the list into a string
  #but using the for loop below I insure all the items are capitalized before being "concatenated"
  for i in range (len(List)):
    
  #checks for hypenated parts of a name to ensure the both parts are capitalized
    if "-" in List[i]:
      hyphenlist = List[i].split("-")
      for s in range (len(hyphenlist)):
        hyphenlist[s] = hyphenlist[s].capitalize()

      #Turn the seperated hyphenated word back into a single word
      hyphenstr = "-".join(hyphenlist)

      #Replace the uncapitalized word with a capitalized one
      List.pop(i)
      List.insert(i,hyphenstr)

      #Add it to the output
      output = output + " " + hyphenstr 
    else:
      #If not hyphenated go through the list and capitalize normally
      List[i] = List[i].capitalize()
      #Add to the output
      output = output + " " + List[i] 
  return output.strip()

#Final product capitalizes all names to make sure they are correct, even capitalizing names joined by hyphens. I could use regrex or other libraries to simplify but I'm content with the current product. There is a bug where if your name begins with or contains any punctuation other than a "-" it won't capitalize properly. Other than that no other bugs are found as of yet.


# Part 1
your_word = question('Input a word: ')
print(your_word)



# Part 2
alone_firstname = question('Input your first name: ')
capitalized_alone_firstname = name_capitalization(alone_firstname)
print("Hello " + capitalized_alone_firstname)



#Part 3
firstname = question('Input your first name: ')
lastname = question('Input your last name: ')
capitalized_firstname = name_capitalization(firstname)
capitalized_lastname = name_capitalization(lastname)

#What counts as concatenation?
names = {capitalized_lastname, capitalized_firstname}
first_and_last_name = " ".join(names)
print(first_and_last_name)



#Part 4
student1 = question('Input a student: ')
student2 = question('Input another student: ')
capitalized_student1 = name_capitalization(student1)
capitalized_student2 = name_capitalization(student2)
print("Your students are " + capitalized_student1 + " and " + capitalized_student2)