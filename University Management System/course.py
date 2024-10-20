class Course:
    def __init__(self, course_code, course_name, credits):
        self.course_code = course_code
        self.course_name = course_name
        self.credits = credits

    def __repr__(self):
        return f"Course(Code: {self.course_code}, Name: {self.course_name}, Credits: {self.credits})"
