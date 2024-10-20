from student import Student
from course import Course
from faculty import Faculty
from university import University

def main():
    university = University("ABC University")

    # Load any existing data
    university.load_data()

    # Add courses
    course1 = Course("CS101", "Data Structures", 4)
    course2 = Course("CS102", "Algorithms", 4)
    university.add_course(course1)
    university.add_course(course2)

    # Add new student and faculty
    student1 = Student("+123456789", "Alice", 19, "Computer Science", 2)
    student2 = Student("+122456745", "john", 23, "Statistics", 3)
    faculty1 = Faculty("+987654321", "Dr. Williams", 45, "Computer Science")
    
    # Enroll student in a course
    student1.enroll_in_course(course1)
    student2.enroll_in_course(course2)
    faculty1.assign_course(course1)

    university.add_student(student1)
    university.add_faculty(faculty1)

    # Save data to file
    university.save_data()

    # Display current data
    print(university)
    print(university.students)
    print(university.faculty)

if __name__ == "__main__":
    main()
