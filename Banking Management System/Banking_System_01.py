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

# Function to create a new account
def create_account(accounts):
    account_number = input("Enter account number: ").strip()
    name = input("Enter account holder's name: ").strip()
    
    if account_number in accounts:
        print("Account with this number already exists.")
    else:
        account = BankAccount(account_number, name)
        accounts[account_number] = account
        print(f"Account created for {name} with account number {account_number}.")
        save_accounts(accounts)

# Main function for the Banking System
def banking_system():
    accounts = load_accounts()  # Load existing accounts from file

    while True:
        print("\nBanking System Menu:")
        print("1. Create a new account")
        print("2. View balance")
        print("3. Deposit money")
        print("4. Withdraw money")
        print("5. View transaction history")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == '1':
            create_account(accounts)
        elif choice in ['2', '3', '4', '5']:
            account_number = input("Enter your account number: ").strip()
            if account_number in accounts:
                account = accounts[account_number]
                if choice == '2':
                    account.view_balance()
                elif choice == '3':
                    amount = float(input("Enter amount to deposit: "))
                    account.deposit(amount)
                    save_accounts(accounts)
                elif choice == '4':
                    amount = float(input("Enter amount to withdraw: "))
                    account.withdraw(amount)
                    save_accounts(accounts)
                elif choice == '5':
                    account.view_transactions()
            else:
                print("Account not found.")
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the Banking System application
banking_system()
