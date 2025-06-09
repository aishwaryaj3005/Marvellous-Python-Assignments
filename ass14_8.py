class Vehical:
    def start(self):
        print("Inside Vehical Class")

class Car(Vehical):
    def Start(self):          #overriding method
        print("Inside Car Class")

obj1 = Vehical()
obj1.start()

obj2 = Car()
obj2.Start()

'''
OUTPUT :
Inside Vehical Class
Inside Car Class
'''