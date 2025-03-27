class RomanToInt:
    # Define the method to convert Roman numeral to integer
    def con_int(self, roman):
        # Step 1: Create a dictionary that maps Roman numerals to their respective integer values
        roman_val = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
        }
        
        # Step 2: Initialize total to store the final integer result
        # Step 3: prev_val is used to keep track of the previous Roman numeral's value for comparison
        total = 0
        prev_val = 0

        # Step 4: Iterate over each character (Roman numeral) in the input string
        for char in roman:
            # Step 5: Get the integer value corresponding to the Roman numeral character
            cur_val =  roman_val[char]

            # Step 6: Check if the current value (cur_val) is greater than the previous value (prev_val)
            # This indicates we are in a subtractive notation (e.g., "IV" or "IX")
            if cur_val > prev_val:
                # Step 7: Adjust total by subtracting twice the previous value
                # We subtract twice the previous value because we already added it once in the last iteration
                total = total - 2 * prev_val

            # Step 8: Add the current value to the total
            total = total + cur_val

            # Step 9: Update prev_val to the current value for the next iteration
            prev_val = cur_val

        # Step 10: Return the final computed total (integer value of the Roman numeral)
        return total
    
# Step 11: Take input from the user for the Roman numeral
roman = input("Enter a Roman Numeral: ")

# Step 12: Create an instance of the RomanToInt class
obj = RomanToInt()

# Step 13: Call the method `con_int()` to convert the Roman numeral to an integer
result = obj.con_int(roman)

# Step 14: Output the result
print(result)
