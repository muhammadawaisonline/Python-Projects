import os

# File where passwords will be stored
PASSWORD_FILE = "passwords.txt"

# Function to load the passwords from the file
def load_passwords():
    passwords = {}
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, 'r') as file:
            for line in file:
                account, password = line.strip().split(':')
                passwords[account] = password
    return passwords

# Function to save the passwords to the file
def save_passwords(passwords):
    with open(PASSWORD_FILE, 'w') as file:
        for account, password in passwords.items():
            file.write(f"{account}:{password}\n")

# Function to add a new password
def add_password(passwords):
    account = input("Enter account name (e.g., 'email', 'bank', etc.): ").strip()
    password = input(f"Enter password for {account}: ").strip()
    passwords[account] = password
    print(f"Password for '{account}' added successfully.\n")

# Function to retrieve a password
def retrieve_password(passwords):
    account = input("Enter the account name to retrieve the password: ").strip()
    if account in passwords:
        print(f"Password for '{account}': {passwords[account]}\n")
    else:
        print(f"No password found for '{account}'.\n")

# Function to delete a password
def delete_password(passwords):
    account = input("Enter the account name to delete: ").strip()
    if account in passwords:
        del passwords[account]
        print(f"Password for '{account}' deleted successfully.\n")
    else:
        print(f"No password found for '{account}'.\n")

# Function to display all stored accounts
def display_accounts(passwords):
    if passwords:
        print("Stored accounts:")
        for account in passwords:
            print(f"- {account}")
    else:
        print("No accounts stored.\n")

# Main function for the password manager
def password_manager():
    passwords = load_passwords()  # Load existing passwords from file

    while True:
        print("Password Manager Menu:")
        print("1. Add a new password")
        print("2. Retrieve a password")
        print("3. Delete a password")
        print("4. Display all accounts")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == '1':
            add_password(passwords)
            save_passwords(passwords)  # Save after adding
        elif choice == '2':
            retrieve_password(passwords)
        elif choice == '3':
            delete_password(passwords)
            save_passwords(passwords)  # Save after deletion
        elif choice == '4':
            display_accounts(passwords)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.\n")

# Run the Password Manager
password_manager()
