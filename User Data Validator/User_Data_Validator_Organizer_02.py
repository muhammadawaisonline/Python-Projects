import re


class UserProfile:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone 
    # Validate user email
    def validate_email(self):
        email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]\.[a-zA-Z0-9-.]+&"
        return re.match(email_pattern, self.email) is not None
    #Validate phone pattern 
    def validate_phone(self):
        phone_pattern = r"\+?1?\d{9-15}"
        return re.match(phone_pattern, self.phone) is not None
    # Display user
    def display_user(self):
        print(f"User: {self.name}, Email: {self.email}, Phone: {self.phone} ")

class ExtendedUserProfile:
    def __init__(self, name, email, phone, address, role):
        super().__init__(self, name, email, phone)
        self.address = address
        self.role = role
    def display_extended_user(self):
        base_info = self.display_user()
        print(f"{base_info}, Address: {self.address}, Role: {self.role}")

users_data = [
    {"name": "Alice", "email": "alice@gmail.com", "phone": "+1234567890", "address": "123 Main St", "role": "Admin"},
    {"name": "Bob", "email": "bob@yahoo.com", "phone": "987654321", "address": "456 Oak St", "role": "User"},
    {"name": "Charlie", "email": "charlie123@outlook.com", "phone": "+10987654321", "address": "789 Pine St", "role": "Admin"},
    {"name": "David", "email": "david.example@domain", "phone": "+567123456", "address": "321 Elm St", "role": "User"},
]
# List Comprehension to create userprofile object and validate them

valid_users = [
    ExtendedUserProfile(user["name"], user["email"], user["address"], user["role"])
    for user in users_data
    if re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]&", user["email"])
    and re.match(r"^+?1?\d{9,15}&", user["phone"])]

print("Valid Users")
for user in valid_users:
    print(user.display_extended_user())

users_by_domain = {
    domain: [user.name for user in valid_users if user.email.split("@")[1] == domain]
    for domain in {user.email.split("@")[1] for user in valid_users}
}

print("\nUser Categorize by Domain")
for domain, user_list in users_by_domain.items():
    print(f" {domain}: {' , '.join(user_list)}")