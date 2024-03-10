class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}

    def input_marks(self, course_id):
        mark = float(input(f"Enter marks for {self.name} in course {course_id}: "))
        self.marks[course_id] = mark

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, DoB: {self.dob}"

class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name

    def __str__(self):
        return f"ID: {self.course_id}, Name: {self.name}"

class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_information(self):
        num_students = self.number_of_students()
        for _ in range(num_students):
            self.students.append(self.student_information())

        num_courses = self.number_of_courses()
        for _ in range(num_courses):
            self.courses.append(self.course_information())

        self.select_course_input_marks()

    def number_of_students(self):
        return int(input('Enter the number of students: '))

    def student_information(self):
        student_id = input('Input student ID: ')
        name = input('Input name of student: ')
        dob = input('Input MM/DD/YYYY: ')
        return Student(student_id, name, dob)

    def number_of_courses(self):
        return int(input('Enter the number of courses: '))

    def course_information(self):
        course_id = input('Input course ID: ')
        name = input('Input course name: ')
        return Course(course_id, name)

    def select_course_input_marks(self):
        course_id = input('Enter the course ID to input marks: ')
        for student in self.students:
            student.input_marks(course_id)

    def list_students(self):
        print("\nList of Students:")
        for student in self.students:
            print(student)

    def list_courses(self):
        print("\nList of Courses:")
        for course in self.courses:
            print(course)

    def show_student_marks_for_course(self):
        course_id = input('Enter course ID to show student marks: ')
        print(f"\nStudent marks for Course {course_id}:")
        for student in self.students:
            marks = student.marks
            if course_id in marks:
                print(f"Student: {student.name}, Mark: {marks[course_id]}")

# Main program
student_system = StudentManagementSystem()
student_system.input_information()

# List information
student_system.list_students()
student_system.list_courses()
student_system.show_student_marks_for_course()
