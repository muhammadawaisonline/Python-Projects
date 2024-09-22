import json
INVENTORY_FILE = 'inventory.json'

# Load inventory from file
def load_inventory():
    try:
        with open(INVENTORY_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Save inventory to file
def save_inventory(inventory):
    with open(INVENTORY_FILE, 'w') as file:
        json.dump(inventory, file, indent=4)

# Add new item to inventory
def add_item(inventory, item_name, quantity):
    if item_name in inventory:
        print(f"{item_name} already exists in inventory. Updating quantity instead.")
        update_item(inventory, item_name, quantity)
    else:
        inventory[item_name] = quantity
        save_inventory(inventory)
        print(f"Added {item_name} with quantity {quantity}.")

# Update existing item quantity
def update_item(inventory, item_name, quantity):
    if item_name in inventory:
        inventory[item_name] += quantity
        save_inventory(inventory)
        print(f"Updated {item_name} to quantity {inventory[item_name]}.")
    else:
        print(f"{item_name} not found in inventory.")

# Display inventory
def display_inventory(inventory):
    if inventory:
        print("Inventory:")
        for item, quantity in inventory.items():
            print(f"- {item}: {quantity}")
    else:
        print("Inventory is empty.")

def main():
    inventory = load_inventory()
    
    while True:
        print("\nInventory Management System")
        print("1. Add item")
        print("2. Update item")
        print("3. Display inventory")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            add_item(inventory, item_name, quantity)
        elif choice == "2":
            item_name = input("Enter item name to update: ")
            quantity = int(input("Enter quantity to add: "))
            update_item(inventory, item_name, quantity)
        elif choice == "3":
            display_inventory(inventory)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
