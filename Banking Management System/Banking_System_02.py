import os
import json
from datetime import datetime

ACCOUNT_FILE = "accounts.json"

class BankAccount:
    def __init__ (self, account_number, name, balance = 0):
        self.account_number = account_number
        self.name = name
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited {amount} on {datetime.now().strftime("%Y-%m-%\d %H:%M:%S")}")
        print(f"Deposited {amount} Successfully. You current balance is {self.balance}")
    def withdrwal(self, amount):
        if amount > self.balance:
            print("Insufficient Balance!")
        else:
            self.balance -= amount
            self.transactions.append(f" withdrwal {amount} on {datetime.now().strftime("%Y-%m-%\d %H:%M:%S")}")
            print(f" Withdrwal {amount} successfully. Your Current Balance is {self.balance}")
    def view_balance(self):
            print(f"Your Current Balance is: {self.balance} ")

    def transactional_history(self):
        if not self.transactions:
             print("You havn't made any transaction yet!")
        else:
            for transaction in self.transactions:
                print(transaction)
# Function to load account
def load_account():
    if os.path.exists(ACCOUNT_FILE):
        with open(ACCOUNT_FILE, "r") as file:
            try:
                account_data = json.load(file) 
                accounts= {acc_num: BankAccount(acc_num, acc["name"], acc["balance"])
                            for acc_num, acc in account_data.items()}
            # Restoring transactions
                for acc_num, acc in accounts.items():
                    acc.transactions = account_data[acc_num]["transactions"]
                    return accounts
            except json.JSONDecodeError:
                 # Hnadle empty or curropted file
                 return {}
    
    return {}

# Function for Save account 
def save_account(accounts):
    with open(ACCOUNT_FILE, "w") as file:
        accounts_data = {acc_num: {
            "name": acc.name,
            "balance": acc.balance,
            "transactions": acc.transactions
            
        } for acc_num, acc in accounts.items()}
        json.dump(accounts_data, file)

        

def create_account(accounts):
    account_num = int(input("Enter Account Number: "))
    account_name = input("Enter Account name: ")

    
    if account_num in accounts:
        print(f"{account_num} already Exist: Try another one.")
    else:
        account = BankAccount(account_num, account_name)
        accounts[account_num] = account
        print(f" Account has beed created for name {account_name} with {account_num}.")
        save_account(accounts)
        


# Function for Banking System
def banking_system():
    accounts = load_account()

    while True:
        print("\nBanking System")
        print("1. create new account ")
        print("2. View Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. View Transaction History")
        print("6. Exit Program")

        choice = input("Select Option from (1-6): ")
        
        if choice == "1":
                create_account(accounts)   
        elif choice in ["2", "3", "4", "5"]:
            account_num = input("Enter Your account Number: ").strip()
            if account_num in accounts:
                account = accounts[account_num]
                if choice == "2":
                        account.view_balance()
                elif choice == "3":
                     amount = float(input("Enter your deposit ammount: "))
                     account.deposit(amount)
                elif choice == "4":
                     amount = float(input("Enter Your Withdrwal Amount: "))
                     account.withdrwal(amount)
                     save_account(accounts)
                elif choice == "5":
                     account.view_tansactions()
            else:
                 print("Account Not found!")
        elif choice == "6":
             print("Goodbye.")
             break
        else:
             print("Invalid Choice: please tray again.")

if __name__ == "__main__":
     banking_system()     


