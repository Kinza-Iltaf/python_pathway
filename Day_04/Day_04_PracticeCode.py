# Task : 01
# Create a dictionary that store the student related data and also print the dictionary type too.

student =  {
   " name" :"john",
    "class" : 5,
    "grade" :"A",
}
print(student)
print(type(student))


# Task : 02
# create a dictionary type variable and access its first two elements.

profile = {
    "Name" : "Sara",
    "Total_Posts" : 107,
    "Followers"    : 358,
    "Following"   : 876,
    "is_active"   : "True",
}

print("Here is the First Two elements of Profile(dic):")
print(profile["Name"])
print(profile["Total_Posts"])

#Task :03
# create a dictionary type variable and access it value and change it through key

profile = {

    "Name" : "Sara",
    "Total_Posts" : 107,
    "Followers"    : 358,
    "Following"   : 876,
    "is_active"   : "True",

}

print("The User Profile Info:", profile)

profile["Name"] = "Hamna"

print("Values After Name Updation:", profile)

# Task : 04
# Create a dictionary named student_info that includes the following keys:

# "Name": The student's name (e.g., "Alex").
# "Age": The student's age (e.g., 20).
# "subjects" :  "Math": 85, "English": 78, "Science": 92
    
student_info = {
  "Name" : "Alex",
  "Age"  : 20,
  "Subjects" :  {
      "Math" : 85,
      "English" : 79,
      "Science" : 92,
  }

 }

# Print the entire student_info dictionary.

print("Student Info Is:", student_info)

# Access and print the marks for "Science".
print("Marks of Science:",student_info["Subjects"]["Science"])

# Update the marks for "Math" to 90.

student_info["Subjects"]["Math"] = 90
print("Marks of Math:",student_info["Subjects"]["Math"])

# Add a new subject "History" with marks 88.
student_info["Subjects"]["History"] = 88
print("Marks of History:",student_info["Subjects"]["History"])

# Print the updated student_info dictionary.
print("Updated Student Info:", student_info)

# find the total keys in student_info dictionary
Total_keys = len(student_info)
print("The total Keys are:", Total_keys)

# Return the all keys of Student_info in form of list through typecasting and print the type as well
print("Typecasting of Keys into List:", list(student_info.keys()))
print("The Type of Student info is:", type(student_info))

# Return All the vlaues of keys in student_info

print("The Values of Keys Are:", student_info.values())

# Return All the values in form of key:value 

print("Keys and Values in form of Tupples:", student_info.items())

print(student_info.get("Name"))  #accessing value through get() function

print(student_info["Name"])  #by simple method

# Add city value "city": "maly" through update method

student_info.update({"City":"Maly"})
print("After Updation if Student info:", student_info)

# Task : 05
# store the following words into pythone dictionary:
#  "cat" : "small animal" , "table" : "a piece of furniture" , "list of facts and figure"

words_meaning = {
    "cat" : "small animal" , 
    "table" : ["a piece of furniture" , "list of facts and figure"]

}
print("Here are the meaning of some words:", words_meaning)

# Task : 06
# You are given a list of subjects for students. Assume one classroom is required for 1
# subject. How many classrooms are needed by all students.
# ”python” ,“java” ,“C++” ,“python” ,“javascript” ,“java” ,“python” ,“java” ,“C++” ,“C”

# Note: Here are every subject there required one class. like for python we need one class so all for samae subject student.
# like for python we need one class 
#  for java we need one class
# so here the things repeating  like in list we have three python students but for all of them we need one classroom.
# for solving this question the best approch is set where duplicated values get ignored.

subjects ={"python" , "java", "c++" , "python", "js" , "java" , "python" , "java" , "c++" , " c" }
print("Class room:", subjects)

print("Total number of class rooms:", len(subjects))

# Task: 07
# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.

Marks_of_sujects = {}

print("Initail Dictionary for Student marks that is empty:", Marks_of_sujects)
p_marks = int(input("Enter marks for physics:"))

p_marks = int(input("Enter marks for physics:"))

p_marks = int(input("Enter marks for physics:"))

Marks_of_sujects.update({"Physics": p_marks})
Marks_of_sujects.update({"chemistry": p_marks})
Marks_of_sujects.update({"Math": p_marks})


print("marks of Student in Subjects:", Marks_of_sujects)

# Task: 08
# Create a dictionary to store information about a student, including their name, age, grade, and a list of subjects they are studying. Add another key for their percentage and update it later.

student_info = {
    "Name" : "john",
    "Age"  : 23 ,
    "Grade": "A+",
    "Subjects": ["physics" , "chemistry", "math" , "Bio" ,]
}

print("Student Info:", student_info)

student_info["percentage"] = 89

print("Student info After Adding Percentage key to the dictionary:", student_info)

# Print the student's name, age, and subjects. Update the student's grade and percentage and then print the updated dictionary.

student_info.update({"Grade":"B"})
student_info.update({"percentage":78})

print("Student info after updating the grade and percentage:" , student_info)

# Task: 09
# Create a dictionary to store employee records where each key is the employee's ID and the value is another dictionary containing the employee's name, department, and salary.

employee_info = {

    "id_01" : {
        "emp_name": "wana",
        "dep":"machanical",
        "salary" : 8000000,

    },

     "id_02" :{
        "emp_name": "john",
        "dep":"bio",
        "salary" : 200000,

    },

     "id_03" :{
        "emp_name": "Sara",
        "dep":"IT",
        "salary" : 800000,

    },

     "id_04" :{
        "emp_name": "bruce",
        "dep":"HR",
        "salary" : 560000,

    }

}
# Add a new employee to the dictionary.

employee_info["id_05"] = {"emp_name":"Neha", "dep" : "management" , "salary": 67900}

print("Employee Info after adding new employee:", employee_info)
# Update the salary of an existing employee.

employee_info["id_01"].update({"salary":3})
employee_info["id_02"].update({"salary":5})
employee_info["id_03"].update({"salary":7})
employee_info["id_04"].update({"salary":9})
employee_info["id_05"].update({"salary":11})
print("Employee info After salary Updation:" , employee_info)
# Print the details of an employee by accessing their ID.

print("Employee ID_01 Info:", employee_info["id_01"])
# Print all employee IDs.
print("ID's of all employees:", employee_info.keys())


# Task: 10
# 3. Nested Dictionary for Courses:

# Create a nested dictionary where the outer dictionary contains course names as keys, and the values are dictionaries containing the number of students enrolled and the course duration in weeks.

# courses: python , java , c++

course_Details = {

    "python" :{
        "Total_student" : 46 ,
        "Course_duration" : " 13 weeks",
    },

      "java" :{
        "Total_student" : 82 ,
        "Course_duration" : " 20 weeks",
    },

      "c++" :{
        "Total_student" : 29 ,
        "Course_duration" : " 15 weeks",
    },

}

print("Course Details are:", course_Details)

# Add a new course to the dictionary.

course_Details["web dev"]= {"Total_student":59 , "Course_duration" : " 3 weeks",}

print("After adding new course:", course_Details)
# Access and print the duration of a specific course.

print("Duration of c++ course:", course_Details["c++"][ "Course_duration"])
# Update the number of students enrolled in a course.

course_Details["c++"].update({ "Total_student" : 23 })
course_Details["java"].update({ "Total_student" : 33 })
course_Details["python"].update({ "Total_student" : 53 })
course_Details["web dev"].update({ "Total_student" : 63 })

print("After updation of Enrolled Student:", course_Details)

# Task: 11
# 4. Inventory Management:

# Create a dictionary to manage inventory in a store where keys are item names and values are the quantity of those items.

invertory_system = {
    "Apples":34,
    "Bananas":65,
    "Graps":25,
    "peers":37,
    "Strabery":54,
}
print("Items in inventory system:", invertory_system)

# Add items to the inventory. 

invertory_system["Oranges"] = 43

print("After adding new item:", invertory_system)
# Update the quantity of an existing item.

invertory_system.update({"Apples":30})

print("After updatig the Quantity of Apples:", invertory_system)
# Remove an item from the inventory.

invertory_system.pop("Apples")
print("After removing the Apples item:", invertory_system)
# Print the total number of items in the inventory.

print("Total numbers of Items:", len(invertory_system.keys()))

# Task : 12
# 5. Phone Book:
# Create a dictionary to simulate a phone book where keys are contact names and values are their phone numbers.

phone_book = {
    "johm" : 9136897,
    "Michel" : 3435235,
    "sara": 45366343,
    "farah": 89438938,
}

print("Phone Book Details:", phone_book)
# Add a few contacts to the phone book.
phone_book["Adam"] = 4349347
phone_book["Maly"] = 45673
phone_book["Bruce"] = 435639

print("AFter Adding some contacts:", phone_book)
# Print a contact’s phone number using their name.
print("Contact Number Of Adam:", phone_book["Adam"])
# Update a contact's phone number.
print("Sara's numberr befone updation:", phone_book["sara"])

phone_book.update({"sara":434232})

print("Sara's numbers after updation:", phone_book["sara"])
# Print all contacts and their phone numbers.

print("Contacts with phone number:" , phone_book.items())


        # ******  Practice Questions and Solutions: Sets ******



# Task : 01
# 1. Unique Cities:

# Create a set of cities visited by you in the past year.

visited_cities = {"New York", "Los Angeles", "Chicago"}

print("Cities we visited last times:", visited_cities)
print("Type of visited_cities: ", type(visited_cities))
# Add a few more cities to the set.
visited_cities.add("kolampur")
print("After adding new city:", visited_cities)

# Attempt to add a duplicate city and observe what happens.
visited_cities.add("kolampur") # this name would get ignored in output bcz it is duplicated.
print("After adding duplicated city name:", visited_cities)
# Remove a city from the set.

visited_cities.remove("New York")

print("After removing the New York:", visited_cities)
# Print the final set of cities.

print("Final set of visited cities:", visited_cities)

# Task : 02
# 2. Common Friends:
# Create two sets representing friends you have from two different schools.

group1 = {"john", "Alice"}
group2 = {"Bob", "Sarah", "john"}
# Find and print the common friends between the two sets.
print("Common Friend Between The groups:", group1.intersection(group2))
# Find the union of both sets to get a list of all friends.
print("All friend:", group1.union(group2))
# Remove a friend from one of the sets and print the updated set.
group2.remove("john")
print("Group 2 frinds after Removal of John:", group2)

# Task : 03
# 3. Set Operations:

# Create two sets: one containing numbers from 1 to 5 and another containing numbers from 4 to 8.
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
# Perform the union operation on these sets and print the result.
print("Union of set1 and set2:", set1.union(set2))
# Perform the intersection operation and print the result.
print("Intersection of set2 and set2 is: ", set1.intersection(set2))
# Use the difference() method to find elements present in the first set but not in the second, and vice versa.
print("Difference of (set1/set2):", set1.difference(set2))

print("Difference of (set2/set1):", set2.difference(set1))


# Task : 04
# Unique Words in a Sentence:

# Take a sentence as input and convert it into a set of words.
sentence = str(input("Enter a sentence:" ))

# Print the unique words in the sentence by using a set.
set1 = set(sentence.split())
print(set1)
# Add a new word to the set and print the updated set.

set1.add("great")
print("updated list:", set1)
# Check if a particular word is present in the set.

print("Checking for word 'great' :", "great" in set1)


# Task : 05
# 5. Managing a Classroom:

# Create a set containing the names of students in a classroom.
std_names = {"john" , "Alice" , "Bob", "Michel"}
print("Student of class: ", std_names)
# Add a new student to the set.

std_names.add("Lee")
print("Students names after addition of new student:" , std_names)
# Remove a student who has left the classroom.

std_names.remove("john")
print("Students name after leaving john:", std_names)
# Print the total number of students currently in the classroom.

total_std = len(std_names)
print("Total students in class:", total_std)
# Check if a particular student is in the classroom.

print("Is Alice exist in classroom:", "Alice" in std_names)















