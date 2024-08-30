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



