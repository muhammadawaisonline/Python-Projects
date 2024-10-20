import re # For regular expression
class Employee:
    total_employee = 0
    employee_list = []
    def __init__(self, name, email, salary):
        self.name = name
        self.email = email
        self.salary = salary
    

    # Validate email format using regex library
        if not self.validate_email(self._email):
            raise ValueError(f"Invalid Email Form: {self.email}")
        
        Employee.total_employee += 1 
        Employee.employee_list.append(self)

        @property
        def name(self):
            return self._name
        
        @name.setter
        def name(self, new_name):
            self._name = new_name

        @property
        def email(self):
            return self._email
        
    

        @property
        def salary(self):
            return self._salary
        @salary.setter

        def salary(self, new_salary):
            self._salary = new_salary

    @classmethod
    def total_employee_count(cls):
        return cls.total_employee
    # class method to print all employees datail
    @classmethod
    def list_all_employees(cls):
        return [f"{emp._name} ({emp._email} - ${emp._salary})" for emp in cls.employee_list]
    
    # Method to validate email using regular expression
    def validate_email(self, email):
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.]+&"
        return re.match(pattern, email) is not None
        
    # Method to calculate Annual salary (full time and part time employees)
    def calculate_annual_salary(self):
        raise NotImplementedError("Subclass must implement this method.")


# Inherited calsss for Full Time Employees
class FullTimeEmployees(Employee):
    def __init__(self, name, email, salary):
        # Clalling the base class instructor
        super().__init__(name, email, salary)
    def calculate_annual_salary(self):
        return self.salary*12 # Full Toime meployee' salary is multiplied 12
    

# Inherited class for Part Time Emloyees
class PartTimeEmployee(Employee):
    def __init__(self, name, email, hourly_rate, hourly_work):
        super().__init__(name, email, hourly_rate*hourly_work)
        self.hourly_rate = hourly_rate
        self.hourly_work = hourly_work

    def calculate_annual_salary(self):
        return self.salary*52 # Weekly salary 52 weeks
    

# Demonstraring the Employee Management system

# Creating Full time and Part time Employees
emp1 = FullTimeEmployees("Alice Johnson", "alice.johnson@gmail.com", 5000)
emp2 = PartTimeEmployee("John Smith", "john.smith@gmail.com", 20, 30) # $20 per hour for 30 hours
emp3 = FullTimeEmployees("Bob Smith", "bob_smith@gmail.com", 6009 )

# List All Employees
print(f" Total Employees: {Employee.total_employee_count()}")
print(f"Employees List:")
print(f"\n".join(Employee.list_all_employees()))


# Calculate and Display Annual Salary
print(f"\n{emp1.name}\'s Annual Salary: {emp1.calculate_annual_salary()}")
print(f"{emp2.name}\'s Annual Salary: {emp2.calculate_annual_salary()}")
print(f"{emp3.name}\'s Annual Salary: {emp3.calculate_annual_salary()}")

