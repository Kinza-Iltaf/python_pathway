
#  Write a Python program that prints "Hello, World!" and then prints your name on the next line.

print("Hello, World!")
print("Bruce Lee")

# Create a variable age and assign it your age. Then, print a message that includes your age using that variable.
age = 18
print("i am", age, "years old")

# Create variables for your first name and last name. Print a greeting message that includes both names.
first_Name = "Bruce"
last_Name = "Lee"
print("Hello!",first_Name, last_Name)


# Write a program that takes two numbers as input from the user, adds them, and prints the result.
num1 = int(input("Enter The First Number:",))
num2 = int(input("Ener The Second Number:",))

sum = num1 + num2

print("Sum Of", num1, "And", num2 , "is:", sum) 

# Write a program that calculates the area of a rectangle using width and height as inputs from the user.
length = int(input("Enter the Length of Rectangle:",))
width = int(input("Enter the Width of Rectangle:",))
area = length * width

print("Area of Rectangle is:",area)

# Convert a string representing a number (e.g., "123") to an integer and then perform arithmetic operations with it.

num1 = "123"
num2 = 5
num1 = int(num1)  #type casting
sum = num1 + num2
 
print("Sum is:",sum)

# Convert a float to an integer and print both values to show the difference.
float_value = 45.2
int_value = int(45.2) #typecasting

print("Integer Value:", int_value)
print("Float Value:", float_value)

# Create a program that asks the user for their favorite color and then prints a message saying, "Your favorite color is [color]."

color = str(input("Enter your favorite color:"),)
print("Your favorite color is:", color)

# Write a program that takes a number as input from the user and prints whether the number is even or odd.

num = int(input("Ener a number:",))
