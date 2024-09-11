import os

# File to store transactions
TRANSACTIONS_FILE = "transactions.txt"

# Function to load transactions from a file
def load_transactions():
    transactions = []
    if os.path.exists(TRANSACTIONS_FILE):
        with open(TRANSACTIONS_FILE, 'r') as file:
            for line in file:
                description, amount = line.strip().rsplit(':', 1)
                transactions.append((description, float(amount)))
    return transactions

# Function to save transactions to a file
def save_transactions(transactions):
    with open(TRANSACTIONS_FILE, 'w') as file:
        for description, amount in transactions:
            file.write(f"{description}:{amount}\n")

# Function to add an income or expense
def add_transaction(transactions):
    description = input("Enter the description of the transaction (e.g., 'groceries', 'salary'): ").strip()
    try:
        amount = float(input("Enter the amount (positive for income, negative for expense): "))
        transactions.append((description, amount))
        print(f"Transaction '{description}' added successfully.\n")
    except ValueError:
        print("Invalid amount. Please enter a number.\n")

# Function to show all transactions
def show_transactions(transactions):
    if transactions:
        print("\nYour transactions:")
        for description, amount in transactions:
            transaction_type = "Income" if amount > 0 else "Expense"
            print(f"{description}: {amount} ({transaction_type})")
    else:
        print("No transactions recorded yet.\n")

# Function to show the current balance
def show_balance(transactions):
    balance = sum(amount for _, amount in transactions)
    print(f"\nYour current balance is: {balance}\n")

# Function to delete a transaction
def delete_transaction(transactions):
    show_transactions(transactions)
    try:
        index = int(input("Enter the number of the transaction to delete: ")) - 1
        if 0 <= index < len(transactions):
            removed_transaction = transactions.pop(index)
            print(f"Transaction '{removed_transaction[0]}' removed successfully.\n")
        else:
            print("Invalid transaction number.\n")
    except (ValueError, IndexError):
        print("Invalid input. Please try again.\n")

# Main function for the budget tracker
def budget_tracker():
    transactions = load_transactions()  # Load existing transactions from file

    while True:
        print("Budget Tracker Menu:")
        print("1. Add a transaction")
        print("2. View transactions")
        print("3. View balance")
        print("4. Delete a transaction")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == '1':
            add_transaction(transactions)
            save_transactions(transactions)  # Save after adding
        elif choice == '2':
            show_transactions(transactions)
        elif choice == '3':
            show_balance(transactions)
        elif choice == '4':
            delete_transaction(transactions)
            save_transactions(transactions)  # Save after deletion
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.\n")

# Run the Budget Tracker
budget_tracker()
