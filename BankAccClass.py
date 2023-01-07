class Account():
    def __init__(self, owner = 'None', balance = 0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Owner : {self.owner}, Account Balance : {self.balance}"

    def deposit(self, depamount):
        
        self.balance = self.balance + depamount
        print(f"Amount Rs. {depamount} deposited successfully. Current Balance is Rs. {self.balance}.")     #Using f string instead of format . f string allows us to embed the value of an expression inside the curly braces
        
    def withdraw(self, witamount):
        
        if (witamount>self.balance):
            print("Transaction not possible, invalid amount!!")
        else:
            self.balance = self.balance - witamount
            print("Withdrawl of Rs. {} successfull. Current Balance Rs. {}.".format(witamount,self.balance))
    
def selection():
    if choice==1:
        value = int(input("Enter the amount you want to deposit : "))
        bankAcc.deposit(value)
    
    elif choice==2:
        value = int(input("Enter the amount you want to withdraw : "))
        bankAcc.withdraw(value)

    elif choice ==3:
        print(bankAcc)

    else:
        print("Invalid Choice")

bankAcc = Account("Anjan", 100)

choice = int(input("Enter 1 for Deposit.\nEnter 2 for Withdrawl.\nEnter 3 for Balance Enquiry.\n"))
selection()
