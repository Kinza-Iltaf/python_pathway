                    #   Practice Codes for Function
# Task  :01
# write a  that take two numbers from users and return the sum and then call that function

def cal_sum(num1, num2):
    return num1+num2

num1 = int(input("Enter a number:"))
num2 = int(input("Enter another number:"))

result = cal_sum(num1 , num2)
print("Sum of", num1 , "and" , num2 , "is:", result)

# Task : 02
# Define a function that print your name and print it on screen 10 times through while and for loop:

# Through while loop
def print_name(name):
    print(name)


name = str(input("Enter your name:"))
init = 0

while init<=9:
    print_name(name)

    init+=1

# Through for loop 

def print_name(name):
    print(name)

name = str(input("Enter your name:"))

for val in range(0 , 10):
    print_name(name)  

# Task : 03
# write a program that calculate the average of three numbers
def cal_avg(num1 , num2 , num3):
    sum = num1 + num2 + num3
    avg = sum/3
    return avg

num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
num3 = int(input("enter third number:"))
result = cal_avg( num1, num2 ,num3)
print("The Average of", num1 , "," , num2 , "and", num2, "is:" , result)

 
#  Task : 04
# write a function that take list as parameter and print its length
list = [3,5,6,7,8]

def fun_len(list):
    result = len(list)
    print ("The length of list is:",result)
fun_len( list) 

#  Task : 04
# write a function that take list as parameter and print its element not in list format like 3 , 4, 5, 6.. not in way [2,3,5,66,4]
list = [3,5,6,7,8]

def fun_len(list):
    for val in list:
        print(val, end=" ")

fun_len(list)

# Task : 05
# write a function that print the factorial of number taken by user.


def fac_cal(num):
    result=1
    for val in range(1 , num+1):
        result *= val
    return result
num = int(input("enter a number:"))
factorial = fac_cal(num)
print("The factorial of", num , "is:", factorial)
   
    