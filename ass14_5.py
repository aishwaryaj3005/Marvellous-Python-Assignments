class BankAccount:

    def __init__(self, Acc_no, Name, Balance):
        self.Acc_no = Acc_no
        self.Name = Name
        self.balance = Balance

    def Display(self):
        print("Account Number :", self.Acc_no)
        print("Name :", self.Name)
        print("Balance :", self.balance)

    def Diposit(self):
       self.Dip_amt = float(input("\nEnter Amount to diposit : "))
       self.balance += self.Dip_amt
       print("Amount after diposit :", self.balance)
    
    def Withdraw(self):
        self.withdraw_amt = float(input("\nEnter Amount to withdraw : "))
        self.balance -= self.withdraw_amt
        print("Amount after Withdraw :", self.balance)
        print("\nTotal Balance is :", self.balance)

obj = BankAccount(1234512345, "Riya",5000)
obj.Display()
obj.Diposit()
obj.Withdraw()

'''
OUTPUT :
Account Number : 1234512345
Name : Riya
Balance : 5000

Enter Amount to diposit : 7000
Amount after diposit : 12000.0

Enter Amount to withdraw : 2000
Amount after Withdraw : 10000.0

Total Balance is : 10000.0
'''