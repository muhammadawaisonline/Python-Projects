import os
import json
from datetime import datetime

# File to store account details
ACCOUNTS_FILE = "accounts.json"

# Class representing a Bank Account
class BankAccount:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance
        self.transactions = []

    # Deposit money
    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited {amount} on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Deposited {amount} successfully. Current balance: {self.balance}")

    # Withdraw money
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrew {amount} on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Withdrew {amount} successfully. Current balance: {self.balance}")

    # View balance
    def view_balance(self):
        print(f"Account balance: {self.balance}")

    # View transaction history
    def view_transactions(self):
        if not self.transactions:
            print("No transactions found.")
        else:
            print("\nTransaction history:")
            for transaction in self.transactions:
                print(transaction)

# Function to load accounts from a file
def load_accounts():
    if os.path.exists(ACCOUNTS_FILE):
        with open(ACCOUNTS_FILE, 'r') as file:
            try:
                accounts_data = json.load(file)
                accounts = {acc_num: BankAccount(acc_num, acc["name"], acc["balance"])
                            for acc_num, acc in accounts_data.items()}
                # Restoring transactions
                for acc_num, acc in accounts.items():
                    acc.transactions = accounts_data[acc_num]["transactions"]
                return accounts
            except json.JSONDecodeError:
                return {}
    return {}

# Function to save accounts to a file
def save_accounts(accounts):
    with open(ACCOUNTS_FILE, 'w') as file:
        accounts_data = {acc_num: {
            "name": acc.name,
            "balance": acc.balance,
            "transactions": acc.transactions
        } for acc_num, acc in accounts.items()}
        json.dump(accounts_data, file)

