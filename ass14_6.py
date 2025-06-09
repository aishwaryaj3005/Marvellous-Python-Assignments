class Calulator:

    def __init__(self):
        self.no1 = int(input("Enter first number : "))
        self.no2 = int(input("Enter second number : "))

    def Add(self):
        print("Addition :", self.no1 + self.no2)
    
    def Subtract(self):
        print("Subtraction :", self.no1 - self.no2)
    
    def Multiply(self):
        print("Multiplication :", self.no1 * self.no2)

    def Divide(self):
        print("Division :", self.no1 / self.no2)

obj = Calulator()
obj.Add()
obj.Subtract()
obj.Multiply()
obj.Divide()

'''
OUTPUT :
Enter second number : 8
Addition : 20
Subtraction : 4
Multiplication : 96
Division : 1.5
'''