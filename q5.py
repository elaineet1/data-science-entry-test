# Step 1: Input - num and divisor
# Step 2: Output - Return True if num is divisible by divisor, else False. Return an error message if the inputs are not numeric
# Step 3: Condition - num and divisor must be numeric types (int or float)
# Step 4: Method - Use isinstance() to validate numeric type. Use the modulo operator (%) to check divisibility
# Step 5: Logic - (1) If inputs are not numeric: return error message (2) If num % divisor equals zero: return True, else return False

#Task 1:
def check_divisibility(num, divisor):
    # Check if both values have the correct type
    if not isinstance(num, (int, float)) or not isinstance(divisor, (int, float)):
        return "Input must be numeric" #return error message

        # Check divisibility using the modulo operator
    if num % divisor == 0:
        return True
    else:
        return False


# Task 2: Testing the function(Input)
print(check_divisibility(10, 2))  # Expected output: True
print(check_divisibility(7, 3))   # Expected output: False
