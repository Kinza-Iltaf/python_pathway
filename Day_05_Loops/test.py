# Take a number from user as input and find its factorial
num = int(input("Enter the last number:"))
fac = 1   
init = 1
while init <= num:
    fac *= init
    init+=1 

print("factorial of  number ",num, "is:", fac)