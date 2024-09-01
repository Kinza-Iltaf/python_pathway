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
# Print the details of an employee by accessing their ID.
# Print all employee IDs.













