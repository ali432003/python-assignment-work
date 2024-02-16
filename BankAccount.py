class BankAccount:
    def __init__(self,accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance
    def Deposit(self,amt):
        self.balance += amt
        return "Sucessfully amount Rs.{} is deposited your new Balance is Rs.{}".format(amt,self.balance)
    def Withdrawal(self,amt1):
            if amt1 > self.balance:
                return "insufficient amount current balance is Rs.{}".format(self.balance)
            else:    
                self.balance -= amt1
                return "Sucessfully amount Rs.{} withdrawal remaining balance is Rs.{}".format(amt1,self.balance)
    def bankfees(self):
        bf = self.balance*(5/100)  #5% of balance.
        self.balance -= bf
    def display(self):
        print("Account Number: ",self.accountNumber)
        print("Account Name: ",self.name)
        print('Account Balance: Rs',self.balance)            
        
            
b = BankAccount('0000-0000-123',"Ali Aamir",5000)

b.display()      
print('\n')
b.Deposit(500)
b.display()
print('\n')
b.Withdrawal(600)
b.display()
print('\n')
b.bankfees()
b.display()     