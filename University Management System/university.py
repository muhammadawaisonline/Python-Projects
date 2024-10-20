from data_manager import save_students_to_file, load_students_from_file, save_faculty_to_file, load_faculty_from_file

class University:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.faculty = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)

    def add_faculty(self, faculty):
        self.faculty.append(faculty)

    def add_course(self, course):
        self.courses.append(course)

    # Saving data to CSV files
    def save_data(self):
        save_students_to_file(self.students, 'students.csv')
        save_faculty_to_file(self.faculty, 'faculty.csv')
        print("Data saved to files.")

    # Loading data from CSV files
    def load_data(self):
        self.students = load_students_from_file('students.csv')
        self.faculty = load_faculty_from_file('faculty.csv')
        print("Data loaded from files.")

    def __repr__(self):
        return f"University: {self.name}"
