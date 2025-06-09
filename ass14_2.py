class Rectangle:

    def __init__(self, Length, Breath):
        self.Length = Length
        self.Breath = Breath

    def Compute(self):
        Area = self.Length * self.Breath
        Perimeter = 2 * (self.Length + self.Breath)
        print("Area :", Area, ", Perimeter :", Perimeter)

obj = Rectangle(4, 8)
obj.Compute()

'''
OUTPUT :
Area : 32 , Perimeter : 24
'''    