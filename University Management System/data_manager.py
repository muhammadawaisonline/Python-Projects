import csv

# Save student data to CSV

def save_students_to_file(students, filename='students.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['WhatsApp Number', 'Name', 'Age', 'Department', 'Semester'])
        for student in students:
            writer.writerow([student.whatsapp_number, student.name, student.age, student.department, student.semester])

# Load student data from CSV
def load_students_from_file(filename='students.csv'):
    students = []
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                student = Student(
                    whatsapp_number=row['WhatsApp Number'],
                    name=row['Name'],
                    age=int(row['Age']),
                    department=row['Department'],
                    semester=int(row['Semester'])
                )
                students.append(student)
    except FileNotFoundError:
        print(f"{filename} not found. Starting with an empty list.")
    return students

# Save faculty data to CSV
def save_faculty_to_file(faculty_members, filename='faculty.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['WhatsApp Number', 'Name', 'Age', 'Department'])
        for faculty in faculty_members:
            writer.writerow([faculty.whatsapp_number, faculty.name, faculty.age, faculty.department])

# Load faculty data from CSV
def load_faculty_from_file(filename='faculty.csv'):
    faculty_members = []
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                faculty = Faculty(
                    whatsapp_number=row['WhatsApp Number'],
                    name=row['Name'],
                    age=int(row['Age']),
                    department=row['Department']
                )
                faculty_members.append(faculty)
    except FileNotFoundError:
        print(f"{filename} not found. Starting with an empty list.")
    return faculty_members
