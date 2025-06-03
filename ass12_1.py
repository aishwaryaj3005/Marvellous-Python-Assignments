class Demo:
    value =  0

    def __init__(self, no1, no2):
        self.no1 = no1
        self.no2 = no2

    def Fun(self):
        print("Inside Fun : ")
        print("no1 =", self.no1)
        print("no2 =", self.no2)

    def Gun(self):
        print("Inside Gun : ")
        print("no1 =", self.no1)
        print("no2 =", self.no2)

obj1 = Demo(11,21)
obj2 = Demo(51,101)

obj1.Fun()
obj1.Gun()

obj2.Fun()
obj2.Gun()

'''
OUTPUT:
Inside Fun : 
no1 = 11
no2 = 21
Inside Gun : 
no1 = 11
no2 = 21
Inside Fun : 
no1 = 51
no2 = 101
Inside Gun : 
no1 = 51
no2 = 101
'''