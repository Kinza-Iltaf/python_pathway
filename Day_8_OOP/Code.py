# code

# Problem:
# Create a class called Dog that has two attributes: age and breed. Then, create an instance of the class and access these attributes using the instance.
class Dog:
    name = "Blesky"
    age = 12
    def __init__(self):
        print("Here is the constructor:")


Dog1 = Dog() #here we don't need to class the class because of constructor.


# problem
# Create a class called Car that has two attributes: brand and year. Use a constructor to initialize these attributes when an object is created. Then, create an instance of the class and print out the car's brand and year.

class Car:
   
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

car1= Car("mecedes",2010)  

print(car1.brand)
print(car1.year)   

# Problem:
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

        





