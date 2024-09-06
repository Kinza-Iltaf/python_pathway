
# Write a recursive function factorial that calculates the factorial of a given non-negative integer n.

def factorial(n):
     if n > 0:
        if n == 0 :
            return 1
        else:
            return n * factorial(n-1)
        
n = 6
fac = factorial(6)   
print(fac)     



      
        
   