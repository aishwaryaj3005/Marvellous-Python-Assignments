class Bookstore:

    noofbooks = 0

    def __init__(self, Name, Author):
        self.Name = Name
        self.Author = Author
        Bookstore.noofbooks += 1

    def display(self):
        print(self.Name, "by", self.Author,".", "No of Books :", Bookstore.noofbooks)

obj1 = Bookstore("Linux System Programming", "Robert Love")
obj1.display()

obj2 = Bookstore("C Programming", "Dennis Ritchie")
obj2.display()

'''
OUTPUT :
Linux System Programming by Robert Love . No of Books : 1
C Programming by Dennis Ritchie . No of Books : 2
'''