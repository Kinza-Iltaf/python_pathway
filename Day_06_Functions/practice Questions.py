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
   

# Task :06
#write program that convert pakistani ruppy into dollar.where 1$=180 PKR  
def convertor(usd): # function defination
    value = usd *180
    return value

usd = int (input("enter the amount of dollars you want to convert:"))

final = convertor(usd)   # function call
print(usd , " $ is equal to:", final, "PKR.")

# Task : 07
# Write a function that take input from user and then return string about that number is even or odd.
def Varification(num):
    if num % 2 == 0:
        print("Even:")
    else:
        print("odd:")

num = int(input("enter a number:"))

Varification(num)

# Task : 08

# Calculate the factorial through recursion function

def fact(n):
    if n==0:
        return 1
    else:
        factorial = n * fact(n-1)
        return factorial
    

n = int(input("enter a number:"))

f = fact(n)
print(f)

# Task : 09
# calculate nth natural numbers sum through recursion:

def sum_cal(n):
    if n == 0:
        return 0
    else:
        sum = n + sum_cal(n-1)
        return sum
    
n = int(input("Enter a number:"))

sum = sum_cal(n)
print("The sum of natural numbers till", n , "is:", sum)  


#  Task : 10
# Write a recursive function that print the element of list.

def print_list( list , n=0 ): # n is here default parameter.
    if len(list) == n:
        return 0
    else:
        print(list[n])
        print_list(list,n+1)

list = [3,5,6,8]
print_list(list) 

# Task : 11
# Write a Python function called greet that takes a person's name as a parameter and prints a greeting message in the format "Hello, [name]!".

def greet(name):
    print("Hello " , name)
    
name = str(input("Enter your name:"))
greet(name)    


# Task : 12
# Write a function square that takes a number as input and returns its square.


def square(num):
    return num*num

n = int(input("Enter a number:"))
square = square(n)  #function calling
print("The square of ", n , "is:", square)


# Task : 13
#  Write a function display_date that prints the current date.

from datetime import datetime #importing built in function
def display_date():
    print(datetime.now().strftime(" %y year, %m month, %d day "))

display_date()

# Task : 14
# Write a function power that takes two parameters, base and exponent, with the default value of exponent being 2. The function should return base raised to the power of exponent.

def power( b ,e =2  ):
    return b**e
b = int(input("Enter The base:"))
e = int(input("Enter Exponent:"))

print(b,"raised to the power" , e , "is:" , power(b,e))

# Task : 15

# Write a function print_shopping_list that takes a list of items and prints each item prefixed with a bullet point (•).

