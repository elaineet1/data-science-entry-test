# Step 1: Input - A string s
# Step 2: Output - Return the string in reversed order
# Step 3: Condition - s must be a string, otherwise return an error message
# Step 4: Method - Use slicing with a negative step [::-1] to reverse the string
# Step 5: Logic - Check if input is a string; if not, return an error message. If valid, return the reversed string

#Task 1:
def string_reverse(s):
    # Check if s is a string
    if not isinstance(s, str):
        return "Input is not a string"

    # Return the reversed version of the string using slicing
    return s[::-1]


# Task 2: Testing the function (Input)
print(string_reverse("Hello World"))
# Expected: "dlroW olleH"

print(string_reverse("Python"))
# Expected: "nohtyP"
