class BankAccount:
    ROI = 10.5

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print("\nName :", self.Name)
        print("Amount :", self.Amount)
        
    def Diposit(self):
        diposit_amt = float(input("Enter Amount to diposit : "))
        self.Amount += diposit_amt
        print("Amount after diposit :", self.Amount)

    def Withdraw(self):
        withdraw_amt = float(input("Enter Amount to withdraw : "))
        self.Amount -= withdraw_amt
        print("Amount after withdraw :", self.Amount)

    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        print("Interest on Balance at", BankAccount.ROI, "is :", interest)

obj1 = BankAccount("Rahul", 45000)
obj1.Display()
obj1.Diposit()
obj1.Withdraw()
obj1.CalculateInterest()

obj2 = BankAccount("Riya", 50000)
obj2.Display()
obj2.Diposit()
obj2.Withdraw()
obj2.CalculateInterest()

'''
OUTPUT :
Name : Rahul
Amount : 45000
Enter Amount to diposit : 5000
Amount after diposit : 50000.0
Enter Amount to withdraw : 2000
Amount after withdraw : 48000.0
Interest on Balance at 10.5 is : 5040.0

Name : Riya
Amount : 50000
Enter Amount to diposit : 2000
Amount after diposit : 52000.0
Enter Amount to withdraw : 50000
Amount after withdraw : 2000.0
Interest on Balance at 10.5 is : 210.0
'''