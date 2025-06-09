class Person:

    def __init__(self, Name, Age):
        self.Name = Name
        self.Age = Age

    def Display(self):
        print("Name :", self.Name)
        print("Age :", self.Age)

class Teacher(Person):

    def __init__(self, Name, Age, Subject, Salary):
        super().__init__(Name, Age)
        self.Subject = Subject
        self.Salary = Salary

    def Display(self):
        super().Display()
        print("Subject :", self.Subject)
        print("Salary :", self.Salary)

obj = Teacher("Rahul", 20, "Science", 20000)
obj.Display()

'''
OUTPUT :
Name : Rahul
Age : 20
Subject : Science
Salary : 20000
'''