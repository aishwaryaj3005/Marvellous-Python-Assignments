class Employer:

    def __init__(self, Name, Department, Salary):
        self.Name = Name                # Public
        self._Depart = Department       # Protected
        self.__Salary = Salary          # Private
    
    def Display(self):
        print("Name :", self.Name)
        print("Department :", self._Depart)
        print("Salary :", self.__Salary)

obj = Employer("Riya", "English", 50000)
obj.Display()

print(obj.Name)
print(obj._Depart)
print(obj.__Salary)

'''
OUTPUT :
Name : Riya
Department : English
Salary : 50000
Riya
English
# Error
'''