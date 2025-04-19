# Class for storing and managing personal details of a person
class Person:
    def __init__(self):
        # Prompt user to enter personal details
        self.name = input("Enter Name: ")  # Name of the person
        self.age = int(input("Enter Age: "))  # Age of the person
        self.adress = input("Enter Address: ")  # Address of the person
        self.gender = self.input_gender()  # Gender of the person, handled by the input_gender method

    # Method to validate and get the gender input
    def input_gender(self):
        while True:
            # Ask user to input gender and capitalize the first letter
            gender = input("Enter Gender (Male/Female/Other): ").capitalize()
            # Check if gender is valid
            if gender in ["Male", "Female", "Other"]:
                return gender  # Return valid gender
            else:
                print("Invalid Gender. Please enter Male, Female, or Other.")  # Error message if input is invalid
    
    # Method to display the personal details of the person
    def display_per_details(self):
        print(f"Name: {self.name} \nAge: {self.age} \nGender: {self.gender} \nAddress: {self.adress}")
        # Displays Name, Age, Gender, and Address

# Class for storing and managing employee details, inherits from Person class
class Employee(Person):
    def __init__(self):
        super().__init__()  # Call the constructor of the Person class to initialize personal details
        self.e_id = int(input("Enter Employee's ID: "))  # Employee ID
        self.e_dept = input("Enter Employee's Department: ")  # Employee's department
        self.e_sal = int(input("Enter Employee's Salary: "))  # Employee's salary

    # Method to display the employee's details
    def display_emp_details(self):
        print(f"Emp_ID: {self.e_id} \nEmp_Dept: {self.e_dept} \nEmp_sal: {self.e_sal}")
        # Displays Employee ID, Department, and Salary

# Main function to manage multiple employees
def main():
    employee = []  # List to store multiple employee objects
    for i in range(5):  # Loop to collect details for 5 employees
        print(f"\nEnter Details for Emp{i + 1}")  # Prompt for the employee number
        emp = Employee()  # Create an Employee object and initialize its data by calling Employee constructor
        employee.append(emp)  # Add the created employee object to the employee list

        # Display personal and employee details of the created employee
        emp.display_per_details()  # Display the personal details of the employee
        emp.display_emp_details()  # Display the employee-specific details

# Check if the script is being run as the main program
if __name__ == "__main__":
    main()  # Run the main function to execute the program
