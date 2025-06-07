class Numbers:

    def __init__(self, Value):
        self.Value = Value

    def ChkPrime(self):
        for i in range(2, self.Value):
            if self.Value % i == 0:
                return False
        if self.Value > 1:
            return True
        return False

    def ChkPerfect(self):
        sum = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                sum += i
        return sum == self.Value

    def Factors(self):
        factors = []
        for i in range(1, self.Value):
            if self.Value % i == 0:
                factors.append(i)
        return factors

    def SumFactors(self):
        sum = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                sum += i
        return sum
    
    def display(self):
        print("\nValue :", self.Value)
        print("Is Prime :", self.ChkPrime())
        print("Is Perfect :", self.ChkPerfect())
        print("Factors :", self.Factors())
        print("Sum of factors :", self.SumFactors())

obj1 = Numbers(4)
obj1.ChkPrime()
obj1.ChkPerfect()
obj1.Factors()
obj1.SumFactors()
obj1.display()

obj2 = Numbers(28)
obj2.ChkPrime()
obj2.ChkPerfect()
obj2.Factors()
obj2.SumFactors()
obj2.display()

'''
OUTPUT :
Value : 4
Is Prime : False
Is Perfect : False
Factors : [1, 2]
Sum of factors : 3

Value : 28
Is Prime : False
Is Perfect : True
Factors : [1, 2, 4, 7, 14]
Sum of factors : 28
'''