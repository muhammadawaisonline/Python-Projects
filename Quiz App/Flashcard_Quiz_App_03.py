import json
from datetime import datetime

EXPENSES_FILE = 'expenses.json'

# Load expenses from file
def load_expenses():
    try:
        with open(EXPENSES_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save expenses to file
def save_expenses(expenses):
    with open(EXPENSES_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)

# Add new expense
def add_expense(expenses, description, amount, category):
    expense = {
        "description": description,
        "amount": amount,
        "category": category,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    expenses.append(expense)
    save_expenses(expenses)
    print(f"Added expense: {description}, Amount: {amount}, Category: {category}")

# View expenses by category
def view_expenses_by_category(expenses, category):
    print(f"\nExpenses for category: {category}")
    filtered_expenses = [exp for exp in expenses if exp["category"] == category]
    if filtered_expenses:
        for exp in filtered_expenses:
            print(f"{exp['date']}: {exp['description']} - ${exp['amount']}")
    else:
        print("No expenses in this category.")

# Generate total expense report
def generate_report(expenses):
    total = sum(exp['amount'] for exp in expenses)
    print(f"\nTotal expenses: ${total}")

def main():
    expenses = load_expenses()

    while True:
        print("\nExpense Tracker")
        print("1. Add an expense")
        print("2. View expenses by category")
        print("3. Generate total expense report")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter expense description: ")
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            add_expense(expenses, description, amount, category)
        elif choice == "2":
            category = input("Enter category to view: ")
            view_expenses_by_category(expenses, category)
        elif choice == "3":
            generate_report(expenses)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
