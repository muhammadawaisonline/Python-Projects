import json

INVENTORY_FILE = "inventory.json"
def load_inventory():
    try:
        with open(INVENTORY_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_item(inventory):
    with open(INVENTORY_FILE, "w") as file:
        json.dump(inventory, file, indent =  4)

def add_item(inventory, item_name, quantity ):
    if item_name in inventory:
        print(f"{item_name} already exist. Let's update the quantity.")
        update_quantity(inventory, item_name, quantity)
    else:
        inventory[item_name] = quantity
        save_item(inventory)
        print(f"Added {item_name} with quantity {quantity}.")

def update_quantity(inventory, item_name, quantity):
    if item_name in inventory:
        inventory[item_name] +=quantity
        print(f"Updated {item_name} with quantity {inventory[item_name]}.")
    else:
        print(f"{item_name} does not exist.")
def display_inventory(inventory):
    if inventory:
        print("Invenotry📃")
        for item, quantity in inventory.items():
            print(f"-{item}: {quantity}")
    else:
        print("No item has been added yet in inventory.")

def inventory_management_system():
    inventory = load_inventory()
    while True:
        print("\nInventory Management System")
        print("\nSelect one Option")
        print("1. Add Item")
        print("2. Update quantity")
        print("3. View Inventory")
        print("4. Exit")

        choice = input("Enter one option (1-4): ")

        if choice == "1":
            item_name = input("Enter Item Name: ")
            quantity = int(input("Enter Quantity: "))
            add_item(inventory, item_name, quantity)
            save_item(inventory)
        elif choice =="2":
            item_name = input("Enter Item name: ")
            quantity = int(input("Enter quantity: "))
            update_quantity(inventory, item_name, quantity)
            save_item(inventory)
        elif choice == "3":
            display_inventory(inventory)
        elif choice == "4":
            print("Goodbye. 👋")
            break
    

if __name__ == "__main__":
    inventory_management_system()