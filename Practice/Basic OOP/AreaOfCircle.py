# Define a class called AreaOfCircle
class AreaOfCircle:
    # Define a constant 'p' for the value of pi (π)
    p = 3.14159

    # Method to calculate the area of a circle, takes radius 'r' as argument
    def circle(self, r):
        # Calculate the area of the circle using the formula: π * r^2
        area = self.p * r**2
        # Return the calculated area
        return area

# Take input from the user for the radius of the circle, and convert it to an integer
n = int(input("Enter Number: "))

# Create an instance of the AreaOfCircle class
obj = AreaOfCircle()

# Call the circle method on the object 'obj' to calculate the area of the circle
result = obj.circle(n)

# Print the result (the calculated area)
print(result)
