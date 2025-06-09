class Student:
    School_Name = "ABC School"

    def __init__(self, Name, Roll_No):
        self.Name = Name
        self.Roll_No = Roll_No

    def Display(self):
        print("Name :", self.Name)
        print("Roll No :", self.Roll_No)
        print("School Name :", Student.School_Name+"\n")

obj1 = Student("Riya", 12)
obj1.Display()

Student.School_Name = "DEF School"
print("After changing school name :\n")

obj2 = Student("Rahul", 15)
obj2.Display()

'''
OUTPUT :
Name : Riya
Roll No : 12
School Name : ABC School

After changing school name :

Name : Rahul
Roll No : 15
School Name : DEF School
'''