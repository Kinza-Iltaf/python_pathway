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




       
       



