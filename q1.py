# Step 1: Input - value x and y
# Step 2: Output - swap the value of x and y, or return -1 if not numeric
# Step 3: Condition - x and y must both be numeric types (int or float)
# Step 4: Method - use isinstance() to check numeric type, Use tuple unpacking (x, y = y, x) to swap values
# Step 5: Logic - If invalid input: return -1, else print swapped values

#Task 1
def swap(x, y):
    #check input type
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return -1

    (x,y) = y,x #swap value, use tuple unpacking
   
    return x, y #return swapped values


#Task 2: Testing the function (Input)
print(swap("Apple", 10)) #input value, x and y
print(swap(9, 17)) #input value, x and y
