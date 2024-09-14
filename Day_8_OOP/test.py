class Student:
    def __init__(self,name , age):
        
        self.name = name
        self.age = age

    def print_name(self):
        print("Hello!",self.name, "You are now",self.age,"years old")  

s1 = Student("Alice", 28)        
s1.print_name() 
del s1.age   
print("After deletion of Object")
print(s1.age) # throw error because the age attribute has been deleted.

# s1.print_name   : it will throw an error as the object s1 is already deleted.







  


            




        

