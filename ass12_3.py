class Arithmetic:

    def __init__(self):
        self.value1 = 0
        self.value2 = 0

    def Accept(self):
        self.value1 = int(input("Enter first value : "))
        self.value2 = int(input("Enter second value : "))

    def Addition(self):
        self.result = self.value1 + self.value2
        print("Addition :", self.result)
    
    def Subtraction(self):
        self.result = self.value1 - self.value2
        print("Subtraction :", self.result)

    def Multiplication(self):
        self.result = self.value1 * self.value2
        print("Multiplication :", self.result)
    
    def Division(self):
        self.result = self.value1 / self.value2
        print("Division :", self.result, "\n")

obj1 = Arithmetic()
obj1.Accept()
obj1.Addition()
obj1.Subtraction()
obj1.Multiplication()
obj1.Division()

obj2 = Arithmetic()
obj2.Accept()
obj2.Addition()
obj2.Subtraction()
obj2.Multiplication()
obj2.Division()

'''
OUTPUT:
Enter first value : 4
Enter second value : 2
Addition : 6
Subtraction : 2
Multiplication : 8
Division : 2.0

Enter first value : 6
Enter second value : 3
Addition : 9
Subtraction : 3
Multiplication : 18
Division : 2.0
'''