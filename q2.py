# Step 1: Input - A list, a value to find, and a replacement value
# Step 2: Output - Modified list with all occurrences of the find_val replaced by replace_val
# Step 3: Condition - The list must be a list type
# Step 4: Method - Use a for loop with an index to check the list. If the item in the list equals find_val, replace it with replace_val
# Step 5: Logic - Loop through the list, then return the modified list

#Task 1
def find_and_replace(lst, find_val, replace_val):
    # Check input type
    if not isinstance(lst, list):
        return "Input must be a list"

    # Loop through the list using index
    for i in range(len(lst)):
        if lst[i] == find_val:  # Check if value matches
            lst[i] = replace_val  # Replace with new value

    return lst  # Return the modified list


# Task 2: Testing the function (Input)
print(find_and_replace([2, 1, 3, 4, 2, 2], 2, 5))
# Expected: [5, 1, 3, 4, 5, 5]

print(find_and_replace(["apple", "banana", "apple"], "apple", "orange"))
# Expected: ['orange', 'banana', 'orange']
