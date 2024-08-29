        #   Day_03 Coding Practice

# Task: 01
# Write a program that ask user to enter the three favorite movies names and make a list of it

favorite_movies = []
m1 = str(input("Enter your First favorite movie name:"))
m2 = str(input("Enter your First favorite movie name:"))
m3 = str(input("Enter your First favorite movie name:"))
favorite_movies.append(m1)
favorite_movies.append(m2)
favorite_movies.append(m3)
print("Your Favorite Movies List is:",favorite_movies)

# Task: 02
# Create a list of your five favorite fruits. Print the list, then replace the third fruit with a new fruit of your choice. Print the updated list.

favorite_Fruits = []
favorite_Fruits.append(input("Enter your 1st favorite fruit:"))
favorite_Fruits.append(input("Enter your 2nd favorite fruit:"))
favorite_Fruits.append(input("Enter your 3rd favorite fruit:"))
favorite_Fruits.append(input("Enter your 4th favorite fruit:"))
favorite_Fruits.append (input("Enter your 5th favorite fruit:"))

print("Your favorite fruits list is:", favorite_Fruits)

# Replaceing of new fruit at 3rd index:

favorite_Fruits[3] = "Apple"

print("Your favorite fruits list After updationd is:", favorite_Fruits)

# Task: 03
# Question: What is the difference between a list and a tuple in Python? Write a small piece of code to demonstrate mutability in lists.

list = [1,2,4,5]
print("List item are:",list)

list[2] = 3
print("New List is:", list)

tup = (1,2,4,5)
print("The Tuple Element are:", tup)

# tup[2] = 3  : this is not allowed because tuples are immutable(unchangable)

# Task: 04
# Question: Given the list numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100], use list slicing to:
# Extract the first five elements.

num = [ 10, 20 , 30, 40, 50, 60, 70, 80, 90, 100]
part1 = num[0:5]
print("First Five Element Of The List:", part1)

# Extract the last three elements.

part2 = num[-3:]
print("Last Three Element Of list:", part2)
# Extract elements from index 3 to 7.

part3 = num[3:7]
print("Values from index 3 to 7:", part3)
# Reverse the list using slicing.

part4 = num[::-1]
print("Reversing List Using slicing:", part4)
# method2 for reversign the list

num = [ 10, 20 , 30, 40, 50, 60, 70, 80, 90, 100]
num.reverse()
print("List in reverse order:", num)

# Task: 05
# Create a list of your five favorite movies. Now:
# Add a new movie to the end of the list using append().

favorite_Movies = ["The Grapes of Wrath", "It's a Wonderful Life", "High Noon ", "To Kill a Mockingbird ", "Rocky "]
# print("List of your Favorite movies:", favorite_Movies)

favorite_Movies.append("The Color Purple")

print ("Movies List after Append:\n", favorite_Movies)
# Sort the list alphabetically using sort().


favorite_Movies.sort()
print("Sorting Movies name:", favorite_Movies)
# Reverse the order of the list using reverse().


reversing_movies = favorite_Movies.sort(reverse=True)
print("Reversing Movies Names In List:", favorite_Movies)
# Insert a new movie at the second position using insert().

favorite_Movies.insert(2,"kuch kuch")
print("New Movies List After Insersion of new Movies:\n", favorite_Movies) 
# Remove the last movie in the list using pop().

favorite_Movies.pop(-1)
print("Updated List after deletion of last movie Name:\n", favorite_Movies)

# Task:06
# Create a list of numbers from 1 to 10. Remove the first even number from the list using the list.remove() method. Print the modified list.

List = [1,2,3,4,5,6,7,8,9,10]

print("Complete List:", List)
List.remove(2)

print("List after removing First even number:", List)

# Task: 07
# Write a Python function that takes a list and a value as input and returns the index of the value using the list.index() method. If the value is not found, handle the exception and return a message saying "Value not found in the list.
List = [3,5, 75, 53,36,63]
print("List Elemnets are:", List)

value = int(input("Enter Value to Find:"))

if value in List:
    index = List.index(value)
    print("Value exist at index:", index)
else:
    print("Entered Value does not exist in the List:")

#     Task: 08
# Create a tuple with five different animals. Print the tuple. Attempt to change the third animal and explain in a comment why the error occurs.

tup = ("dog", "snake", "cat", "cow", "frog")

print("Tupple that contain the animal names:", tup)

# tup[2] = "Fish" not possible becuase the tupples are unmutable

# Task: 09
# Given the tuple colors = ('red', 'blue', 'green', 'yellow', 'orange', 'purple', 'brown'), use slicing to:

# Extract the first three colors.

color = ('red', 'blue', 'green', 'yellow', 'orange', 'purple', 'brown')
part1 = color[:3]
print("Whole tupple Elements:", color)
print("First Three colors of tupple:", part1)
# Extract the last two colors.
part2 = color[-2:]
print("Last two colors in tupple:", part2)
# Reverse the tuple using slicing.
part3 = color[::-1]
print("Reversing the tupple:", part3)


# Task: 10
# write a program to check that enter the list is palindrome or not
list1 = []
list1.append(int(input("Enter the first Element of the list:")))
list1.append(int(input("Enter the second Element of the list:")))
list1.append(int(input("Enter the third Element of the list:")))

print(list1)

copy_list = list1.copy()
copy_list.reverse()

if(list1 == copy_list):
    print("List is palindrome:")
else:
    print("list is not palindrom:")

#     Task: 11
# write a program that count the students in tupple with grade A

grade = ("C", "D", "A", "A", "B", "B", "A")

Count = grade.count("A")
print("Student with grade A in tupple:",Count)

# store these value in list and sort them ("C", "D", "A", "A", "B", "B", "A"):

List = ["C", "D", "A", "A", "B", "B", "A"]

print("List Elements are:", List)

List.sort()

print("List sorting in Acsending order:",List)

List.sort(reverse=True)
print("List sorting in Decending Order:",List)







