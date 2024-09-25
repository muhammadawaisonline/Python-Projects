import os
import json
from datetime import datetime

ACCOUNT_FILE = "accounts.json"

class BankAccount:
    def __init__(self, account_number, account_name, balance = 0):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited {amount} on {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}")
        print(f"Deposited {amount} Successfully! You current balance is: {self.balance} ")

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance  -=amount
            self.transactions.append(f"Withdrawn {amount} on {datetime.now().strftime("%Y-%m-%d %H:%M:$S")}")
            print(f" withdawn {amount} successfully! Your current balance is: {amount}")
        else:
            print("Insufficient balance!")
    
    def view_balance(self):
        print(f"Account Balance is: {self.balance}")

    def transactions_history(self):
        if not self.transactions:
            print(" No Transaction Found.")
        else:
            for transaction in self.transactions:
                print(transaction) 

