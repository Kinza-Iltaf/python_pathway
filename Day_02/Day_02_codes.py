# Task: 01
# Task: Create a program that asks the user to input their first name and last name separately. Then, concatenate the names to display the full name.

first_name = str(input("Enter your first name:",))
last_name = str(input("Enter your last name:",))
full_name = first_name + last_name
print("Your Full Name Is:",full_name)

# Task: 02
#  Write a program that takes a sentence as input from the user and calculates the length of the sentence, including spaces. Display the total number of characters.
sentence = str(input("Enter a Sentence:",))
len_of_sentence = len(sentence)
print("Your entered sentence length is:", len_of_sentence)

# Task: 03
# Given a string, prompt the user to enter an index number, and then display the character at that index.

str1 = "python"
index = int(input("Enter an index at which you find to find the character:"))
print("At your entered index", index , "the character is:",str1[index])

# Task: 04
# Ask the user to input a string and then enter two index numbers (start and end). Slice the string between these indices and display the result.
str1 = str(input("Enter string:"))
slice_of_str = str1[2:9]
print("The slic of", str1 , "is:", slice_of_str)

#Task: 05
# Create a program that checks if a given string ends with the word "Python." Print True if it does, otherwise print False
str1 = str(input("Enter String:"))
print(str1.endswith("python"))

# Task: 06
# Write a program that capitalizes the first letter of a given sentence.
str1 = str(input("Enter a string:"))
new_str = str1.capitalize()
print("Entered String after capitalization function:", new_str)

# Task: 07
# Replace all occurrences of the word "dog" in the sentence "The quick brown dog jumps over the lazy dog" with "cat.

str1 = "The quick brown dog jumps over the lazy dog."
new_str = str1.replace("dog","cat")
print("Old String:", str1)
print("New string:",new_str)

# Task: 08
# Count how many times the letter "a" appears in the string "banana"

str1 = "banana"
print("The letter a occure in string", str1 , str1.count("a"),"times")

# Task: 09
# find the index of the first occurrence of the word "world" in the string "Hello world! Welcome to the world of Python.

str1 = "hello world"
print("The first occurance of world in", str1, "is:", str1.find("world"))

# Task: 10
#  Create a program that checks if a user-entered string is empty or not. If the string is empty, print "String is empty," otherwise print "String is not empty.
str1 = str(input("Enter a string:"))
if(str1 != ""):
    print("string the not empty.")
else:
    print("you entered empty string.")

# Second way
len_of_string = 0
str1 = str(input("enter a string:"))
len_of_string = len(str1)

if(len_of_string != 0):
    print("your string is not empty")
else:
    print("you entered empty string:")

# Task: 11
# Write a program that prompts the user to enter a string. Check if the string starts with "Hello" and ends with "Python". Print appropriate messages based on the results.
str1 = input("Enter a string:")

str_lower = str1.lower()

if(str_lower.startswith("hello") and str_lower.endswith("python")):
    print("Your String start with hello and end with python")
else:
    print("Your String does not start with hello and end with python")

#Task: 12
# Create a program that checks if a given string is a palindrome (a string that reads the same forwards and backwards, e.g., "madam"). If it is, print "It's a palindrome," otherwise print "Not a palindrome.





