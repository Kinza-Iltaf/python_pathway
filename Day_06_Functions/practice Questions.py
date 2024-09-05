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

 
 