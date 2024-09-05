def cal_avg(num1 , num2 , num3):
    sum = num1 + num2 + num3
    avg = sum/3
    return avg

num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
num3 = int(input("enter third number:"))
result = cal_avg( num1, num2 ,num3)
print("The Average of", num1 , "," , num2 , "and", num2, "is:" , result)