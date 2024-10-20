from person import Person

class Student(Person):
    def __init__(self, whatsapp_number, name, age, department, semester):
        super().__init__(whatsapp_number, name, age)
        self.department = department
        self.semester = semester
        self.courses = []

    def enroll_in_course(self, course):
        self.courses.append(course)

    def __repr__(self):
        return (f"Student(WhatsApp: {self.whatsapp_number}, Name: {self.name}, Age: {self.age}, "
                f"Department: {self.department}, Semester: {self.semester}, Courses: {self.courses})")
