# Define the class to calculate the perimeter of a rectangle
class ParameterOfRectangle:
    
    # Constructor method to initialize the length and width of the rectangle
    def __init__(self, l, w):
        self.l = l  # Store the length of the rectangle
        self.w = w  # Store the width of the rectangle

    # Method to calculate the perimeter of the rectangle
    def parameter(self):
        # Formula for perimeter of rectangle: P = 2 * (length + width)
        par = 2 * (self.l + self.w)
        return par  # Return the calculated perimeter
    
# Step 1: Take user input for the length of the rectangle
length = int(input("Enter Length of Rectangle: "))

# Step 2: Take user input for the width of the rectangle
Width = int(input("Enter width of Rectangle: "))

# Step 3: Create an instance of the ParameterOfRectangle class with the user inputs
obj = ParameterOfRectangle(length, Width)

# Step 4: Call the parameter method on the object to calculate the perimeter
result = obj.parameter()

# Step 5: Print the calculated perimeter of the rectangle
print("The perimeter of the rectangle is:", result)
