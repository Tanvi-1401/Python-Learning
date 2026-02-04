class Account:
    def __init__(self, balance, accNo):
        self.balance = balance
        self.accNO = accNo
    
    def credit_balance(self):
        credits = int(input("Enter amount to credit: "))
        self.balance += credits
        print("Updated balance is: ", self.get_balance())    
        
    def debit_balance(self):
        debits = int(input("Enter amount to debit: "))
        self.balance -= debits
        print("Updated balance is: ", self.get_balance())  
        
    def get_balance(self):
        return self.balance      
        
a1 = Account(5000, "101SB") 
print(a1.balance, a1.accNO)
a1.credit_balance()
a1.debit_balance()       