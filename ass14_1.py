class Employee:
    
    def __init__(self, Name, ID, Salary):
        self.Name = Name
        self.ID = ID
        self.Salary = Salary
        
    def Display(self):
        print("Name :", self.Name, ", ID :", self.ID, ", Salary :", self.Salary)

obj = Employee("Rohit", 101, 50000)
obj.Display()

'''
OUTPUT :
Name : Rohit , ID : 101 , Salary : 50000
'''