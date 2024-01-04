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
        t = {'owner': self.owner, 'type': 'deposit', 'amount': amount}
        self.transactions.append(t)
        return self.transactions
        

    # withdraw_funds()
    def withdraw_funds(self, amount):

        deposits = sum(s['amount'] for s in self.transactions if s['type'] == 'deposit')
        total_balance = deposits + self.balance
        
        if total_balance < amount:
            print("Insufficient Funds")
        else:
            t = {'owner': self.owner, 'type': 'withdraws', 'amount': amount}
            self.transactions.append(t)
            return self.transactions

       





    

      


    # get_balance()
    def get_balance(self):
        deposits = sum(s['amount'] for s in self.transactions if s['type'] == 'deposit')
        withdraws = sum(s['amount'] for s in self.transactions if s['type'] == 'withdraws')
        balance = self.balance + (deposits - withdraws)
        print(f'Your account balance is ${balance: 2f}')

        
       
        


    # get_transaction()
    def get_transaction(self):
        print(self.transactions)

    def get_transaction_count(self):
        print(len(self.transactions))
        


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
anthony_account.deposit_funds(300)

# Testing withdraw
anthony_account.withdraw_funds(400)
anthony_account.withdraw_funds(200)
anthony_account.withdraw_funds(100)

# Testing get balance
anthony_account.get_balance()

# Testing get transactions
anthony_account.get_transaction()

# Testing transaction count
anthony_account.get_transaction_count()




























































































