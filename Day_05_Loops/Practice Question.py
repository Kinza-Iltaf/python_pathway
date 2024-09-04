# Task : 01
# print your name 10 times on screen:
i = 1
while i<10:
        print("Lorenzo")
        i +=1
# Task : 02
# print no from 1 to 50

count = 0
while count <= 50:
    print(count)
    count+=1

# Task : 03
# print no from 1 to 50 in reverse order:

count = 50
while count >=0:
        print(count)
        count-=1

# Task : 04
# print the table of 3: 3 * 1 = 3.... or you can take a number from user too
tab_num = int ( input ( " Enter the number of which you want to print the table:"))

count = 1
while count <= 10 :
       print(tab_num, "*", count , "=", tab_num * count)
       count+=1

# Task : 05
# print the given list: 
# [1,,4,9,16,25,36,49,64,81,100] : as every number is the square is next number like 1, 2,3,4,5,6,7,8,9,100
# method : 01
# using square method

num = 1
list = []
while num<=10:
       result = num*num
       list.append(result)
       print(num*num)
       num+=1
print("The list is:", list)

# method : 2
# using the difference method

num = 1
difference = 3
result = 1

list = [result]

while num<10:
      result = result + difference
      list.append(result)
      num+=1
      difference+=2
print(" Here is the list:", list)

# Task : 06
# Search for a specific number
num = int(input("Enter number:"))

num_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]  # Use a list instead of a tuple
i = 0

while i <= len(num_list):
    if num == num_list[i]:
        print(num, "Exist at index", i)
        break
 
    i += 1
else:
    print("not exist")             
       
print("loop end")  


# Task : 07
#print the followig list using for loop... num_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

num_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for val in num_list:
      print(val)


# Task: 08
# search specific number in the list
num_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for val in num_list:
      
      print(val)

search = int (input("Enter for number you want to search:"))
fount = False
index = 0
for val in num_list:
      if search == val:
            found = True
            if found == True:
             print("number found at index:", index)
      index+=1      
else:
    print("End")


# Range(): this function is used to print the specific range started from zero and end before that specific number which we provided as input:

# Task: 09
# print even number with the help of range() function and store the values in list:

seq = range(0,101,2)  #...0 start, 101 ending point(101 will not include and loop will end one number before it like at 100),  2 step size (everytime the two will be incremented like 0 then 2 increment next 4 and so on)
list = []
print("list of Even number to 100 is:")
for val in seq:
    list.append(val) 
print(list)

# Task : 10
# print numbers from 1 to 100 with range() and for loop:
# Through for loop:
seq = range(0,101,2)  #...0 start, 101 ending point(101 will not include and loop will end one number before it like at 100),  2 step size (everytime the two will be incremented like 0 then 2 increment next 4 and so on)
list = []
print("list of Even number to 100 is:")
for val in seq:
    list.append(val) 
print(list)
list.reverse()
print(list)

#Method 2

print("Numbers from 100 to 1:")
for i in range(100 , 0 , -1):
     print(i)






       



