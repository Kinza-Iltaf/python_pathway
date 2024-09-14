class Student:
    def __init__(self,name , age):
        self.name = name
        self.age = age

    def __student_details(self,reg_no,password):
        self.reg_no = reg_no
        self.password = password
        print("Reg_no ",self.reg_no,"And password ",self.password)
       
    def print_details(self,r,p):
       self.__student_details(r,p)

s1 = Student("Alice", 28)        
print("Student Personal info ")
print(s1.name)
print(s1.age)
reg_no = int(input("Enter your registration number "))
password = int(input("Enter your password"))
print("Studnet private data is ")
s1.print_details(reg_no,password)








  


            




        

