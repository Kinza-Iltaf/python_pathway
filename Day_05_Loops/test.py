# Take a number from user as input and find its factorial
num = int(input("Enter the last number:"))
fac = 1   
for val in range(1 , num+1):
    fac *= val  

print("factorial of  number ",num, "is:", fac)