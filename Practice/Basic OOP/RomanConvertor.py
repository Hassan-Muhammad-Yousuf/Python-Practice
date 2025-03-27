class RomanConvertor:
    def con_rom(self, num):
        # List of tuples containing integer values and their corresponding Roman numerals
        roman_num = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]

        # Initialize an empty string to store the final Roman numeral
        roman_str = ""

        # Iterate through each (value, symbol) pair in the roman_num list
        for val, symbol in roman_num:
            count = num // val  # Find how many times 'val' fits into 'num' using floor division

            if count > 0:  # If val can be used at least once
                roman_str += symbol * count  # Append the corresponding Roman numeral count times
                num = num % val  # Update num to the remainder after using 'val'

                if num == 0:  # If num is fully converted, stop the loop early
                    break
        
        return roman_str  # Return the final Roman numeral string
    
# Prompt user for input and convert it to an integer
num = int(input("Enter an integer: "))

# Create an object of the RomanConvertor class
obj = RomanConvertor()

# Call the con_rom() method to convert the number and store the result
result = obj.con_rom(num)

# Print the final Roman numeral output
print(result)
