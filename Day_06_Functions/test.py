
 
def print_list( list , n=0 ): # n is here default parameter.
    if len(list) == n:
        return 0
    else:
        print(list[n])
        print_list(list,n+1)

list = [3,5,6,8]

print_list(list)       
        
   