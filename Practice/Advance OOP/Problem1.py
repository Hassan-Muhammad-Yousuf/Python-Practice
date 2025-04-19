# Department class to represent a department
class Dept:
    def __init__(self, Dept_name):
        # Initializes the department with a name and an empty list of courses
        self.Dept_name = Dept_name  # Department name
        self._courses = []  # List to store courses related to this department

    def add_courses(self, course):
        # Adds a course to the department's list of courses if it's not already present
        if course not in self._courses:
            self._courses.append(course)

    def list_courses(self):
        # Returns the list of courses in this department
        return self._courses


# Course class to represent a course offered by a department
class Course:
    def __init__(self, dept, course_name):
        # Initializes the course with the department it belongs to, and a name
        self.course_name = course_name  # Course name
        self.department = dept  # Department the course belongs to
        self.students = []  # List to store students enrolled in this course

    def enroll_student(self, student):
        # Adds a student to the course if they are not already enrolled
        if student not in self.students:
            self.students.append(student)

    def list_students(self):
        # Returns the list of students enrolled in this course
        return self.students

    def __str__(self):
        # Returns the course name when the course object is printed
        return self.course_name


# Student class to represent a student
class Student:
    def __init__(self, student_name):
        # Initializes the student's name and an empty list of courses they are enrolled in
        self.student_name = student_name  # Student's name
        self.enrolled_courses = []  # List of courses the student is enrolled in

    def enroll(self, course):
        # Enrolls the student in a course and adds the student to the course's student list
        self.enrolled_courses.append(course)
        course.enroll_student(self)

    def list_courses(self):
        # Returns the list of courses the student is enrolled in
        return self.enrolled_courses 


# Creating two departments
d = Dept("Computer Science")  # Department of Computer Science
d2 = Dept("Mathematics")  # Department of Mathematics

# Creating courses for each department
c1 = Course(d, "CS101")  # CS101 course in Computer Science
c2 = Course(d, "Data Structure")  # Data Structure course in Computer Science
c3 = Course(d2, "Statistics")  # Statistics course in Mathematics
c4 = Course(d2, "Linear Programming")  # Linear Programming course in Mathematics

# Adding courses to departments
d.add_courses(c1)  # Add CS101 to Computer Science department
d.add_courses(c2)  # Add Data Structure to Computer Science department
d2.add_courses(c3)  # Add Statistics to Mathematics department
d2.add_courses(c4)  # Add Linear Programming to Mathematics department

# Creating two students
s = Student("Student 1")  # Student 1
s2 = Student("Student 2")  # Student 2

# Enrolling students in courses
s.enroll(c1)  # Student 1 enrolls in CS101
s2.enroll(c2)  # Student 2 enrolls in Data Structure
s.enroll(c3)  # Student 1 enrolls in Statistics
s2.enroll(c4)  # Student 2 enrolls in Linear Programming

# Printing out the details of all departments, courses, and students
for dept in [d, d2]:  # Loop through all departments (d and d2)
    print(f"Department: {dept.Dept_name}")  # Print the department name
    
    for course in dept.list_courses():  # Loop through all courses in the department
        print(f"Course: {course.course_name}")  # Print the course name
        
        for student in course.list_students():  # Loop through all students in the course
            print(f"Student: {student.student_name}")  # Print the student name
