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

def load_accounts():
    if os.path.exists(ACCOUNT_FILE):
        with open(ACCOUNT_FILE, "r") as file:
            try:
                accounts_data = json.load(file)
                accounts = {acc_num: BankAccount(acc_num, acc["name"], acc["balance"])
                    for acc_num, acc in accounts_data.items()}
                #Restoring Accounts transaction history
                for acc_num, acc in accounts.items():
                    acc.transaction = accounts_data[acc_num]["transactions"]
                return accounts
            except json.JSONDecodeError:
                return {}
    return {}

def save_account(accounts):
    with open(ACCOUNT_FILE, "w") as file:
        accounts_data = { acc_num: {
            "name": acc.name,
            "balance": acc.balance,
            "transactions": acc.transactions
            } for acc_num, acc in accounts.items()}
        json.dump(accounts_data, file)

def create_accoount(accounts): 
    account_number = input("Enter Your Account Number: ")
    account_name = input("Enter Your Account name: ").strip()
    if account_number in accounts:
        print(f"Account {account_number} already exist!")
        
    else: 
        
        new_account = BankAccount(account_number, account_name)
        accounts[account_number] = new_account
        print(f"Account created for {account_name} with Account Number {account_number}")
        save_account(accounts)
    

