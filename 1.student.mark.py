def number_of_students():
    return int(input('Enter the number of students: '))

def student_information():
    student_id = input('Input student ID: ')
    name = input('Input name of student: ')
    dob = input('Input MM/DD/YYYY: ')
    return {'id': student_id, 'name': name, 'dob': dob, 'marks': {}}

def number_of_courses():
    return int(input('Enter the number of courses: '))

def course_information():
    course_id = input('Input course ID: ')
    name = input('Input course name: ')
    return {'id': course_id, 'name': name}

def select_course_input_marks(students, courses):
    course_id = input('Enter the course ID to input marks: ')
    for student in students:
        mark = float(input(f"Enter marks for {student['name']} in course {course_id}: "))
        student['marks'][course_id] = mark

def list_students(students):
    print("\nList of Students:")
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, DoB: {student['dob']}")

def list_courses(courses):
    print("\nList of Courses:")
    for course in courses:
        print(f"ID: {course['id']}, Name: {course['name']}")

def show_student_marks_for_course(students):
    course_id = input('Enter course ID to show student marks: ')
    print(f"\nStudent marks for Course {course_id}:")
    for student in students:
        marks = student['marks']
        if course_id in marks:
            print(f"Student: {student['name']}, Mark: {marks[course_id]}")

# Main program
students = []
courses = []

# Input information
num_students = number_of_students()
for _ in range(num_students):
    students.append(student_information())

num_courses = number_of_courses()
for _ in range(num_courses):
    courses.append(course_information())

select_course_input_marks(students, courses)

# List information
list_students(students)
list_courses(courses)
show_student_marks_for_course(students)



    
