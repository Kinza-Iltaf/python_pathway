# Problem: Employee and Manager
# Create a class Employee that has the following:
# Attributes: name, salary
# Methods:
# get_details() - prints the employee's details
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def print_details(self, name,salary):
        print("Employee name:",self.name) 
        print("Employee salary:",self.salary)   
class Manager(Employee):
        def __init__(self, name, salary , department):
             super().__init__(name, salary)
             self.dep = department

        def get_details(self):  
               print("Manager name:",self.name) 
               print("Manager salary:",self.salary)  
               print("Manager Department:",self.dep) 

manager = Manager("karan", 1248,"HR")  
manager.get_details()  

        
        

       

# Create a class Manager that inherits from Employee and adds the following:

# Attributes: department
# Methods:
# Override get_details() to include the department in the output.
# Objective:
# Implement both classes.
# Create objects of both classes and call their get_details() methods.
# Example:
# python
# Copy code
# Output should include:
# Employee Name: John
# Salary: 50000
# Manager Name: Sarah
# Salary: 90000
# Department: HR









  


            




        

