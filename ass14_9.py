class Product:

    def __init__(self, Name, Price):
        self.Name = Name
        self.Price = Price

    def __eq__(self, other):
        return  self.Price == other.Price
    
obj1 = Product("Riya", 20)
obj2 = Product("Rahul", 22)

if(obj1 == obj2):
    print("Price are Equal")
else:
    print("Price are not equal")

'''
OUTPUT :
Price are not equal
'''