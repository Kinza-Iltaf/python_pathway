# code

# Problem: 01
# Create a class called Dog that has two attributes: age and breed. Then, create an instance of the class and access these attributes using the instance.
class Dog:
    name = "Blesky"
    age = 12
    def __init__(self):
        print("Here is the constructor:")


Dog1 = Dog() #here we don't need to class the class because of constructor.


# problem: 02
# Create a class called Car that has two attributes: brand and year. Use a constructor to initialize these attributes when an object is created. Then, create an instance of the class and print out the car's brand and year.

class Car:
   
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

car1= Car("mecedes",2010)  

print(car1.brand)
print(car1.year)   

# Problem: 03
# Create a class called Book that has three attributes: title, author, and pages. Use a constructor to initialize these attributes when an object is created. Add a method called is_long() that checks if the book has more than 100 pages. If it does, return True, otherwise return False.

class Book:
    def __init__(self, title, author,pages) :

       self.title = title
       self.author = author
       self.pages = pages
    def is_long(self):
        if self.pages > 100:
            return True
        else:
            return False
        
book = Book("Halim", "nimra ahmad", 1203)
print(book.title)
print(book.author)
print(book.pages)
value = book.is_long()
print("checking for number of pages",value )


# problem: 04
# Create a class that take the marks and names of student of three subjects and then make a method that print the average of marks.

class Student:
    def __init__(self,name, marks1 , marks2, marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def avg_marks(self):
        total = self.marks1 + self.marks2 + self.marks3
        return total/3
    
student1 = Student("karan", 3, 3, 3)
avg_marks=student1.avg_marks()
print("HI", student1.name , "Your Average Score is:", avg_marks)

# problem: 05
# create an account class that has two attributes account number and balance.
# cteat methods for debits , ctedits and printing the balance.

class Account:
    def __init__(self, account_no , balance):
        self.acc_no = account_no
        self.balance = balance

    def debit_amount(self,deb_amount):
        self.balance-=deb_amount
        return self.balance,deb_amount
    
    def credit_amount(self , credit_amount ):
        self.balance+=credit_amount
        return self.balance,credit_amount 
    
    def print_balance(self):
        return self.balance
    
account = Account(123456 , 3087345)  

# Account details
print("Balance Details for Account having Number", account.acc_no,"is:", account.balance) 

# After debiting amount
updated_balance,deb_amount = account.debit_amount(2)
print("Your balance after debiting amount",deb_amount,"is",updated_balance)

# After credeting amount
updated_balance,credit_amount = account.credit_amount(3)
print("Your balance after crediting amount",credit_amount,"is",updated_balance)

# current balance after updation
current_balance = account.print_balance()
print("Your updated balance is",current_balance)



            



        





