# 1. Ask the user to "Input a word: ". Output that word back to the user.
word = input("Input a word: ")
print(word)

# 2. Ask the user to "Input your first name: ". Output "Hello " followed by their name. Use concatenation.
name = input("Input your first name: ")
print("Hello" + name)

# 3. Ask the to user to "Input your first name: " Then ask them to "Input your last name: " Output the last name then the first name on the same line with a space between them. Do not use concatenation.
name = input("Input your first name: ")
lastname = input("Input your last name: ")
print(lastname,name)

# 4. Ask the user to "Input a student: ". Then ask them to "Input another student: ". Output "Your students are student1 and student2", where student1 and student2 are replaced with the values of your input.
student1 = input("Input a student: ")
student2 = input("Input another student: ")
print(f"Your students are {student1} and {student2}")

