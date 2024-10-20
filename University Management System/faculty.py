from person import Person

class Faculty(Person):
    def __init__(self, whatsapp_number, name, age, department):
        super().__init__(whatsapp_number, name, age)
        self.department = department
        self.courses = []

    def assign_course(self, course):
        self.courses.append(course)

    def __repr__(self):
        return f"Faculty(WhatsApp: {self.whatsapp_number}, Name: {self.name}, Age: {self.age}, Department: {self.department})"
