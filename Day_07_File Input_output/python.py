
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

   












