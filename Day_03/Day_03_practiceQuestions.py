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







