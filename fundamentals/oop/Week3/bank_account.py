class BankAccount:
    # don't forget to add some default values for these parameters!
    accounts = []
    def __init__(self, int_rate, balance): 
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)
                
    def deposit(self, amount):
        # your code here
        self.balance+=amount
        return self
        
        
    def withdraw(self, amount):
        # your code here
        if(self.balance - amount)>=0:
            self.balance-=amount
        else:
            print("Insuficient Funds: charging a $5 fee")
            self.balance-=5
        return self

    def display_account_info(self):
        # your code here
        print(f"**********")
        print(f"Balance: {self.balance}")
        print(f"**************")
        return self
        
    def yield_interest(self):
        # your code here
        if self.balance > 0:
            self.balance+= (self.balance*self.int_rate)
        return self

    @classmethod
    def print_all_accounts(cls):
        for accs in cls.accounts:
            accs.display_account_info()

    
# acc1 = BankAccount(0.5, 1000)
# acc2 = BankAccount(0.75, 100)

# acc1.deposit(100).deposit(100).deposit(100).withdraw(50).yield_interest().display_account_info()
# acc2.deposit(10).deposit(10).deposit(10).withdraw(5).yield_interest().display_account_info()

# BankAccount.print_all_accounts()