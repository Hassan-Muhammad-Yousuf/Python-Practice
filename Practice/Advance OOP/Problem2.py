# Class to represent a Person
class Person:
    def __init__(self, name, age, address):
        # Initialize name, age, and address of the person
        self.name = name
        self.age = age
        self.address = address

    def display(self):
        # Display person's details
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Address: ", self.address)

# Class to represent a single Publication
class publications:
    def __init__(self, title, year):
        # Initialize the title and year of the publication
        self.title = title
        self.year = year

    def display(self):
        # Display publication details
        print("Title: ", self.title)
        print("Year: ", self.year)

# Faculty class inherits from Person
class Faculty(Person):
    def __init__(self, name, age, address, department):
        # Call the constructor of the Person class using super()
        super().__init__(name, age, address)
        # Initialize department name
        self.department = department
        # Initialize an empty list to store publications
        self.pub = []

    def add_publications(self, pub):
        # Add publication to the list if not already added
        if pub not in self.pub:
            self.pub.append(pub)

    def display(self):
        # First display the personal information from the Person class
        super().display()
        # Then display the department
        print("Department: ", self.department)
        # Then display all publications
        for publication in self.pub:
            publication.display()

# Creating two publication instances
pub1 = publications("R.paper 1", 2020)
pub2 = publications("R.paper 2", 2022)

# Creating a Faculty object (inherits from Person)
fac1 = Faculty("Dr.John", 35, "123 Street", "Agile Methodology")

# Adding publications to the faculty member
fac1.add_publications(pub1)
fac1.add_publications(pub2)

# Displaying the faculty member's complete details, including publications
fac1.display()
