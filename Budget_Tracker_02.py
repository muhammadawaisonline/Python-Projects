import os
TRANSACTIONS_FILE = "transactions.txt"

# Function for loading transactions



# Functio for adding Transactions

def add_tansaction(transactions):
    description = input("Write the description of your transactions like (Grocery, Salary): ").strip()
    try:
        amount = float(input("Write the amount(Positive for income and Negative for expenses): "))
        transactions.append((description, amount))
    except ValueError:
        print(f" {amount}: Enter amount in numbers.\n ")

def load_transactions():
    transactions = []
    if os.path.exists(TRANSACTIONS_FILE):
        with open(TRANSACTIONS_FILE, "r") as file:
            for line in file:
                description, amount = line.strip().rsplit(":", 1)
                transactions.append((description, float(amount)))
    return transactions 


def save_transactions(transactions):

    with open(TRANSACTIONS_FILE, "w") as file:
        for description, amount in transactions:
            file.write(f"{description}: {amount}\n")

# Function for show transactions
def show_transactions(transactions):
    if transactions:
        print("\nYour Transactions")
        for i, (description, amount) in enumerate(transactions, 1):
            transaction_type = "income" if amount>0 else "Expenses"
            print(f"{i}. {description}: {amount} ({transaction_type})")
    else:
        print("You haven't made any transaction yet.")


# Function to show balance
def show_balance(transactions):
    balance = sum(amount for _, amount in transactions)
    print(f"\nYour Current blalance is: {balance}")

# Function for delete transactions

def delete_trasactions(transactions):
    show_balance(transactions)
    try: 
        index = int(input("Enter the number of transactions to delete: ")) - 1
        if 0 <= index < len(transactions):
            remove_transaction = transactions.pop(index)
            print(f"'{index + 1}. {remove_transaction[0]}' has been deleted. ")
        else:
            print(f"{index} transaction doesnot exist.\n")
    except ValueError:
        print("Invalid choice: Read Instruction Carefully and try again.\n")


def budget_tracker():
    transactions = load_transactions()
    while True:
        print("Budget Tracker Menu")
        print("1. Add a Transactions")
        print("2. View Transactions")
        print("3. View Balance")
        print("4. Delete Transaction")
        print("5. Exit")
    
        choice = input("Please Select one Option (1-5): ")
        if choice in ["1", "2", "3", "4", "5"]:
            if choice == "1":
                add_tansaction(transactions)
                save_transactions(transactions)
            elif choice == "2":
                show_transactions(transactions)
            elif choice == "3":
                show_balance(transactions)
            elif choice == "4":
                show_transactions(transactions)
                delete_trasactions(transactions)
                save_transactions(transactions)
            elif choice == "5":
                print("Goodbye.")
                break
        else:
            print("Wrong Choice: Please Choice 1-5 (1-5) Number: ")



if __name__ == "__main__":
    budget_tracker()

    

