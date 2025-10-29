# Step 1: Input - A dictionary (dct), a key, and a value
# Step 2: Output - Return the updated dictionary after adding or updating a key-value pair
# Step 3: Condition - If the key already exists, print the original value
# Step 4: Method - Use "if key in dct" to check if key exists. Use dct[key] = value to add or update the dictionary
# Step 5: Logic - If key exists: print original value, then update it. Else: add a new key-value pair. Finally, return the updated dictionary

#Task 1
def update_dictionary(dct, key, value):
    # Check if key already exists
    if key in dct:
        print("Original value:", dct[key])

    # Add or update the value in the dictionary
    dct[key] = value

    # Return the updated dictionary
    return dct


# Task 2: Testing the function (Input)
print(update_dictionary({}, "name", "Alice"))
# Expected: {'name': 'Alice'}

print(update_dictionary({"age": 25}, "age", 26))
# Expected print: Original value: 25
# Expected return: {'age': 26}
