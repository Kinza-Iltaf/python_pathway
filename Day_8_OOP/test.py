# test file

class Student:
    def __init__(self,name, marks1 , marks2, marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
    def avg_marks(self):
        sum = self.marks1 + self.marks2 + self.marks3

       
        return sum/3


student1 = Student("karan", 3, 3, 3)
marks_avg = student1.avg_marks()

print("Marks average is:", marks_avg)
        

