
# Write a recursive function factorial that calculates the factorial of a given non-negative integer n.

def factorial(n):
     if n < 0:
        print("You Entered Negative number:")
     if n == 0 :
        return 1
     else:
        return n * factorial(n-1)
        
n = int(input("Enter a number:"))
fac = factorial(6)   
print("Fatorial of ", n , "is:", fac)     



      
        
   