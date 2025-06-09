class Book:

    def __init__(self, Price):
        self.__Price = Price

    def GetPrice(self):
        print("Initial Price :", self.__Price)
        return self.__Price
        
    
    def SetPrice(self, NewPrice):
        if NewPrice >= 0:
            self.__Price = NewPrice
        else:
            print("Price cannot be negetive.")
        print("Updated Price :", self.__Price)

obj = Book(500)
obj.GetPrice()
obj.SetPrice(600)

'''
OUTPUT :
Initial Price : 500
Updated Price : 600
'''