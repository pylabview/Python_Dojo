# Assignment: User using chaining
# Author: Rodrigo Arguello
# Date: 06/15/2022
from bank_account import BankAccount

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = {
            'checking':BankAccount(int_rate=0.02, balance=0),
            'savings':BankAccount(int_rate=0.02, balance=0),  
        }
    
    # other methods
    
    def make_deposit(self, amount, account_type='checking'):
    # your code here
        self.account[account_type].deposit(amount)
        return self
        
    def make_withdrawal(self, amount, account_type='checking'):
        self.account[account_type].withdraw(amount)

    def display_user_balance(self):
        for acc_type,acc in self.account.items():
            print(f"User: {self.name} account({acc_type}), Balance: ${acc.balance}")
        print("")
        return self

    def transfer_money(self,
                    amount,
                    other_user):
        self.make_deposit(amount)
        other_user.make_deposit(amount)
        self.display_user_balance()
        other_user.display_user_balance()
        


Adrien = User('Adrien','adrien@gmail.com')

Adrien.make_deposit(1000)

Adrien.display_user_balance()

Jose = User('Jose','Jose@gmail.com')

Jose.make_deposit(2000)

Jose.display_user_balance()

Adrien.transfer_money(500, Jose)
