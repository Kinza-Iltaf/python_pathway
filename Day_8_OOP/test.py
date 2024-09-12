# test file

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
        

