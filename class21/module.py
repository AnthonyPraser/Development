import os
import pandas as pd

class BankAccount:
    
    

    # Init Function
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
        self.transactions = []


    # __str__
    def __str__(self):
        return f"Owner: {self.owner}\nOpening Balance: {self.balance}"


    # deposit_funds()
    def deposit_funds(self, amount):
        t = {'owner': self.owner, 'type': 'deposit', 'amount': {amount}}
        self.transactions.append(t)
        return self.transactions
        

    # withdraw_funds()
    def withdraw_funds(self, amount):
        t = {'owner': self.owner, 'type': 'withdrawal', 'amount': {amount}}
        self.transactions.append(t)
        return self.transactions

        


    # # get_balance()
    # def get_balance(self):
    #     pass


    # # get_transaction()
    # def get_transaction(self):
    #     pass


    # # transaction_count()
    # def get_transaction(self):
    #     pass


    # # transaction_history()
    # def transaction_history(self):
    #     pass


    # # save_transaction()
    # def save_transaction(self):
    #     pass

# Create my class instance 
anthony_account = BankAccount("Anthony", 4000)


# Testing __str__
# print(my_bank_account)

# Testing deposit
anthony_account.deposit_funds(50)
anthony_account.deposit_funds(200)
anthony_account.deposit_funds(300)

# Testing withdraw
anthony_account.withdraw_funds(100)
anthony_account.withdraw_funds(20)
anthony_account.withdraw_funds(150)




























































































