import os
PASSWORD_FILE = "passwords"



# Function to load passwords
def load_passwords():
    passwords = {}
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, "r") as file:
            for line in file:
                account, password = line.strip().split(":")
                passwords[account] = password
    return passwords


# Function to save account in file
def save_password(passwords):
    with open(PASSWORD_FILE, "w") as file:
        for account, password in passwords.items():
            # passwords.item() will return dict_items([('email', '12345'), ('bank', 'abcde'), ('social', '54321')])
            file.write(f"{account}: {password}\n") 

# Function for adding acount and password
def add_password(passwords):
    account = input("Enter your Account Name like (email, bank etc): ").strip()
    password = input(f"Enter password for {account}: ").strip()
    # How to add valus in Dictionaries ==> dictionary[key] = value

    passwords[account] = password

# Function for retrieve password
def retrieve_password(passwords):
    account = input("Enter your account to get back password: ")
    if account in passwords:
        print(f" Password for account {account} is: {passwords[account]}\n ")
    else:
        print(f"Please Enter correct account number: Password for {account} is not available.")

# Function To Display password
def delete_password(passwords):
    account = input("Enter acoount name to delete: ").strip()
    if account in passwords:
        del passwords[account]
        print(f"password for {account} has been deleted successfully.\n")
    else:
        print("Please enter valid acount!")

# Function to display Password
def display_password(passwords):
    if passwords:
        for account in passwords:
            print(f"- {account}")
    else:
        print("No Account Exist!")

# Function to run Password manager App
def password_manager_app():
    passwords = load_passwords()
    while True:
        print("\n Passwords Manager App\n")
        print("\nSelect Rquired Option")
        print("1. Add account")
        print("2. View accounts")
        print("3. Retrieve Password")
        print("4. Delete Account")
        print("5. Exit")

        choice = input("Enter your option: ")
        if choice in ["1", "2", "3", "4", "5"]:
            if choice == "1":
                add_password(passwords)
                save_password(passwords)
            elif choice == "2":
                display_password(passwords)
            elif choice == "3":
                retrieve_password(passwords)
            elif choice == "4":
                delete_password(passwords)
                save_password(passwords)
            elif choice == "5":
                print("Goodbye.")
                break
            else:
                print("Invalid Choice!")
                
        else:
            print("Please choose option from(1-5): ")

if __name__ == "__main__":
    password_manager_app()

