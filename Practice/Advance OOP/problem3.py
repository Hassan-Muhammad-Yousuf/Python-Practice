# The base class for storing student details
class Person:
    Max_marks = 600  # Maximum marks that a student can obtain (constant)

    # Constructor to initialize name and roll number
    def __init__(self):
        self.name = input("Enter Student's Name: ")  # Taking student's name input
        self.roll_num = int(input("Enter Student's Roll Number: "))  # Taking student's roll number input

    # Method to display the student's basic details (name and roll number)
    def display(self):
        print("Name: ", self.name)
        print("Roll Number: ", self.roll_num)

# The class representing student-specific details and methods (inheriting from Person)
class Student(Person):
    def __init__(self, test_marks = 0, Activity_marks = 0):
        super().__init__()  # Calling the constructor of the Person class
        self.test_marks = test_marks  # Initialize test marks (default is 0)
        self.Activity_marks = Activity_marks  # Initialize activity marks (default is 0)
    
    # Method to input academic scores (Test and Activity Marks)
    def Input_Acadamic_Scores(self):
        self.test_marks = int(input("Enter Test Score: "))  # Taking input for test marks
        self.Activity_marks = int(input("Enter Activity Score: "))  # Taking input for activity marks
    
    # Method to display academic scores (Test and Activity Marks)
    def Display_Academic_score(self):
        print("Test Marks: ", self.test_marks)
        print("Acadamic Score: ", self.Activity_marks)

# The class representing sports scores (independent of the Person class)
class Sports:
    def __init__(self,sports_marks = 0):
        self.sports_marks = sports_marks  # Initialize sports marks (default is 0)
    
    # Method to input sports scores
    def Input_Sports_Scores(self):
        self.sports_marks = int(input("Enter Sports Score: "))  # Taking input for sports marks
    
    # Method to display sports scores
    def Display_Sports_score(self):
        print("Sports Score: ", self.sports_marks)

# The Result class is derived from both Student and Sports classes
# This class calculates and displays the final result (total marks, grade, etc.)
class Result(Student, Sports):
    def __init__(self):
        Student.__init__(self)  # Initialize the Student class
        Sports.__init__(self)  # Initialize the Sports class
        self.G_total = 0  # Initialize the total marks to 0
        self.grade = ""  # Initialize grade as an empty string
    
    # Method to calculate the final result (total marks, percentage, grade)
    def Calc_final_result(self):
        # Calculate total marks by adding test marks, activity marks, and sports marks
        self.G_total = self.Activity_marks + self.test_marks + self.sports_marks
        # Calculate percentage
        self.per = (self.G_total / self.Max_marks) * 100  # (Total marks / Max marks) * 100
        # Determine the grade based on the percentage
        self.grade = ""  # Reset grade before calculating
        if self.per > 90:
            self.grade = "A"
        elif self.per > 80:
            self.grade = "B"
        elif self.per > 70:
            self.grade = "C"
        elif self.per > 60:
            self.grade = "D"
        else:
            self.grade = "FAIL"
        
        return self.grade  # Return the final grade
    
    # Method to display the final result including student details, marks, and grade
    def display(self):
        self.Calc_final_result()  # Calculate the final result before displaying
        super().display()  # Display the student details using the Person class's display method
        print(f"Maximum Marks: {self.Max_marks} \nObtained Marks: {self.G_total}")  # Display max and obtained marks
        print("Percentage: ", self.per)  # Display percentage
        print("Final Grades: ", self.grade)  # Display the final grade

# Main program starts here
r = Result()  # Create an instance of Result class

r.Input_Acadamic_Scores()  # Call method to input academic scores
r.Input_Sports_Scores()  # Call method to input sports scores

r.display()  # Call method to display the final result (all details)
