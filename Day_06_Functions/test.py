
def fac_cal(num):
    result=1
    for val in range(1 , num+1):
        result *= val
    return result
num = int(input("enter a number:"))
factorial = fac_cal(num)
print("The factorial of", num , "is:", factorial)