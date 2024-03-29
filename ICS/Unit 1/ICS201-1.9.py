# 1. Output the phrase "Hello World" WITH the quotations.
print('"Hello World"')

# 2. Ask the user to "Input a word: ". Output the word back but with only lower case letters. On a new line output the word in only upper case letters
word = input("Input a word: ")
print(word.lower())
print(word.upper())

# 3. Ask the user to "Input a word that is at least 5 letters long: ". Output the 2nd to 4th letters.
word = input("Input a word that is at least 5 letters long: ")
output = word[1] + word[2] + word[3]
print(output)

# 4. Ask the user to "Input a word: ". Output the index of the first occurrence of the letter "o".
word = input("Input a word: ")
print(word.index("o"))

# 5. Ask the user to "Input a word: ". Output the length of the word.
word = input("Input a word: ")
print(len(word))