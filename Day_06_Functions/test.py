
# n  = int(input("enter a number:"))
# list = [0,1]
# i = 2
# while i<=n:
#     list.append(list[i-1]+list[i-2])
#     i+=1
# print(list)

# def fibanocci_sequence(n):
#     if n <= 1:
#         return n
#     else:
#         return fibanocci_sequence(n-1)+fibanocci_sequence(n-2)
    
# def print_fibonocci(n):
#     if n >= 0:
#         print_fibonocci(n-1)
#         print(n, end=",")

# n = int (input("enter a number:"))
# print_fibonocci(n)  
# 
# 
# Recursive function to calculate Fibonacci number
# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# # Function to print the Fibonacci sequence
# def print_fibonacci_sequence(n):
#     if n >= 0:
#         print_fibonacci_sequence(n - 1)  # Recursive call for earlier terms
#         print(fibonacci(n), end=", ")    # Print the current Fibonacci number

# # Example usage
# n = int(input("Enter a number: "))
# print(f"Fibonacci sequence up to {n}:")
# print_fibonacci_sequence(n)


# Write a function arithmetic_operations that takes two numbers and returns their sum, difference, product, and quotient.

def arithmetic_operations(n1 , n2 ):
   return n1+n2,n1-n2 ,n1*n2,n1/n2 if n2!=0 else "Undefined"

sum,dif , pro , quot = arithmetic_operations(367,78)
print(f"Sum:{sum}\nDifference:{dif}\nProduct:{pro}\nQuotient: {quot}")



      






    






      
        
   