# Step 1: Input - A list of numbers (lst)
# Step 2: Output - Return the first negative number found in the list. If no negative number is found, return "No negatives"
# Step 3: Condition - A negative number is any number less than 0, use < 0
# Step 4: Method - Use a while loop to check each element in the list
# Step 5: Logic - Start from index 0. While index is within the list:
# (1) If the number is negative, return that number
# (2) Else continue to the next index
# (3) If no negative found, return "No negatives"

#Task 1:
def find_first_negative(lst):
    index = 0  # Check from the first element

    # Loop until the end of the list
    while index < len(lst):
        # Check if the current number is negative
        if lst[index] < 0:
            return lst[index]  # Return the first negative number

        index += 1  # Move to the next index

    # If no negative value found
    return "No negatives"


# Task 2: Testing the function (Input)
print(find_first_negative([-3, 5, -1, 7, -2, 8]))
# Expected: -3

print(find_first_negative([2, 10, 7, 0]))
# Expected: "No negatives"
