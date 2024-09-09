
# Task : 01
# Opening file and Reading Data from that file

f = open("notes.txt", "r") #open file command and r is for reading mode.
contect = f.read()        # storing the data of file in content object.
print(contect)             # print the data.
f.close()                 # closing the file.

 # Task : 02
# Reading specific part in file

f = open("notes.txt", "r") #open file command and r is for reading mode.
contect = f.read(4)       #reading first 4 string.
print(contect)             # print the data.
f.close()                 # closing the file.


# Task : 03
# Reading file line by line

f = open("notes.txt", "r") 
line_1 = f.readline()     
print("Line 1 in File:", line_1)    

line_2 = f.readline()     
print("Line 3 in File", line_2)  

line_3 = f.readline()     
print("Line 3 in File:",line_3) 

f.close() 

# Task : 04
# writing something in file:

f = open("test.txt" , "w")
f.write("i am programmer. i love coding.") #this line will overwrite this line

# Task : 05
# Appending something in file:
f = open("test.txt" , "a")
f.write(" \nBecause i want to learn machine learning.")


# Task : 06
# using + mode:
# write and read a data from file in such way that existing data does not affect.

f = open("test.txt" , "r+")
content = f.read()
f.write("programmer" + content) 

# Task : 07
# write a program that write and read the data after truncating(removing/deletion) the existing data.

f = open("test.txt" , "w+")
content = f.read()
f.write("john" ) 
f.close()


# Task : 08
# write a program to append the data at the end of the file without truncating the existing data:

f = open("test.txt" , "a+")
content = f.read()
f.write(" Abraham" ) 
f.close()


# Task : 09
# delete a file name delete through python code:

import os 
os.remove("delete.txt")

# Task : 10
# write a program that wite the below data in file.
# Hi Everyone.
# We are learning file I/O
# using python.
# i like programming in python.

with open("test.txt", "w") as f:
    f.write("Hi Everyone.\nWe are learning file I/O\nusing java.\ni like programming in java.")


# Task : 11
# write a program that replace the java word with python and update the file data.

with open("test.txt", "r") as f:
   content = f.read()

new_data = content.replace("java", "python")   

print(content)

print(new_data)

with open("test.txt", "w") as f:
   f.write(new_data)

# Task : 12

# search for the word " learning " exist in the file or not:

with open("test.txt", "r") as f:
   content = f.read()

Search = content.find("learning")

if Search >= 0:
   found = True
   print("Found at index:", Search)
else:
   print("Not found")

# Task : 13
# search for the word " learning " exist in the file or not: also print the line at which it exist.

data = True
word   = "programming"
line_no = 1
with open("test.txt", "r") as f:
 while data:
   data = f.readline()
   if word in data : 
      print("The word found at line:",line_no)


# Task : 14
# write a program that print the total even number is file
with open("test.txt", "r") as f:
    data = f.read()
    print(data)
    count = 0
    num = data.split(",")
    for val in num:
        if int(val)%2 == 0:
            count+=1
print(count)      

  # Task : 15 
# 1. Basic File Operations: Opening and Reading
# Write a Python program to:
# Open a file named example.txt in read mode.
# Read the entire content of the file.
# Print the content to the console

f = open("test.txt", "r")
content = f.read()
print("The entire content of the file is:\n",content)

 # Task : 16
# 2. Reading Specific Characters
# Modify the previous program to read only the first 15 characters of the file.

f = open("test.txt", "r")
content = f.read(15)
print("The first 15 charaters of file is:\n",content)

 # Task : 17
#  3. Reading Line by Line
# Write a Python program to read the first two lines of a file named example.txt.

f = open("test.txt", "r")
line_1 = f.readline()
print("Line one:", line_1)

line_2 = f.readline()
print("Line one:", line_2)

# Task : 18

# 4. Writing to a File (Overwrite)

# Write a Python program to open a file in write mode, overwrite its content with "Hello, World!", and then close the file.

f = open("test.txt", "w")
f.write("Hello, World!")
f.close()

# Task : 19
# 5. Appending to a File

# Write a Python program that appends the text "I love Python." to an existing file example.txt.

with open("test.txt", "a") as f:
    f.write("I love Python")


# Task : 20
# 6. Reading and Writing with r+ Mode
# Write a Python program to:

# Open a file named example.txt in r+ mode.
# Read the existing content.
# Write "Hello" at the beginning of the file   
with open("test.txt", "r+") as f:
      content= f.read()
      print("Before", content)
      f.seek(0)
      f.write("Hello")
      print("After:",content)  

# Task : 21
# 8. Working with Binary Files
# Write a Python program to:
# Open a binary file named image.png in binary read mode.
# Read the first 1024 bytes of the file.

with open("Cafe menu.png", "rb") as f:
   content= f.read(1024)
   print(content)


# Task : 22
# 10. Simultaneous Read and Write using w+ Mode

# Write a Python program to:

# Open a file in w+ mode.
# Write "First Line" to the file.
# Move the cursor to the start of the file and read the content

with open("Cafe menu.png", "w+") as f:
    f.write("First Line")
    f.seek(0)
    data = f.read()
    print(data)















