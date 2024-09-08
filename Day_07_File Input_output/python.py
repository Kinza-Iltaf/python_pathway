
# Opening file and Reading Data from that file

f = open("notes.txt", "r") #open file command and r is for reading mode.
contect = f.read()        # storing the data of file in content object.
print(contect)             # print the data.
f.close()                 # closing the file.


# Reading specific part in file

f = open("notes.txt", "r") #open file command and r is for reading mode.
contect = f.read(4)       #reading first 4 string.
print(contect)             # print the data.
f.close()                 # closing the file.

# Reading file line by line

f = open("notes.txt", "r") 
line_1 = f.readline()     
print("Line 1 in File:", line_1)    

line_2 = f.readline()     
print("Line 3 in File", line_2)  

line_3 = f.readline()     
print("Line 3 in File:",line_3) 

f.close() 




