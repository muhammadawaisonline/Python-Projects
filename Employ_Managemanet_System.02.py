import re  # For regular expressions

# Base class for employees
class Employee:
    total_employees = 0
    employee_list = []

    def __init__(self, name, email, salary):
        self._name = name
        self._email = email
        self._salary = salary
        
        # Validate email format using regex
        if not self.validate_email(self._email):
            raise ValueError(f"Invalid email format: {self._email}")

        Employee.total_employees += 1
        Employee.employee_list.append(self)

    # Getter for name
    @property
    def name(self):
        return self._name

    # Setter for name
    @name.setter
    def name(self, new_name):
        self._name = new_name

    # Getter for email
    @property
    def email(self):
        return self._email

    # Getter for salary
    @property
    def salary(self):
        return self._salary

    # Setter for salary
    @salary.setter
    def salary(self, new_salary):
        self._salary = new_salary

    # Class method to track total employees
    @classmethod
    def total_employee_count(cls):
        return cls.total_employees

    # Class method to print all employee details
    @classmethod
    def list_all_employees(cls):
        return [f"{emp._name} ({emp._email}) - ${emp._salary}" for emp in cls.employee_list]

    # Method to validate email using regular expressions
    @staticmethod
    def validate_email(email):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email) is not None

    # Abstract method for calculating annual salary
    def calculate_annual_salary(self):
        raise NotImplementedError("Subclasses must implement this method")


# Inherited class for Full-time employees
class FullTimeEmployee(Employee):
    def __init__(self, name, email, salary):
        # Calling the base class (Employee) constructor
        super().__init__(name, email, salary)

    def calculate_annual_salary(self):
        return self.salary * 12  # Full-time employees' salary is multiplied by 12


# Inherited class for Part-time employees
class PartTimeEmployee(Employee):
    def __init__(self, name, email, hourly_rate, hours_worked):
        # Calculate salary for part-time employees
        salary = hourly_rate * hours_worked
        # Calling the base class (Employee) constructor
        super().__init__(name, email, salary)
        self._hourly_rate = hourly_rate
        self._hours_worked = hours_worked

    def calculate_annual_salary(self):
        return self.salary * 52  # Weekly salary * 52 weeks


# Demonstrating the Employee Management System

# Creating full-time and part-time employees
emp1 = FullTimeEmployee("Alice Johnson", "alice.j@example.com", 5000)
emp2 = PartTimeEmployee("Bob Smith", "bob.smith@example.com", 20, 30)  # $20/hr for 30 hours
emp3 = FullTimeEmployee("Charlie Brown", "charlie.b@example.com", 6000)

# List all employees
print(f"Total employees: {Employee.total_employee_count()}")
print("Employee List:")
print("\n".join(Employee.list_all_employees()))

# Calculate and display annual salaries
print(f"\n{emp1.name}'s Annual Salary: ${emp1.calculate_annual_salary()}")
print(f"{emp2.name}'s Annual Salary: ${emp2.calculate_annual_salary()}")
print(f"{emp3.name}'s Annual Salary: ${emp3.calculate_annual_salary()}")
