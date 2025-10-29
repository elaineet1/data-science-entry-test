# Step 1: Input - Class with three attributes for each car: make, model, and year
# Step 2: Output - Print the car information in the format: "Year Make Model"
# Step 3: Condition - The car object must be created with make, model, and year inputs
# Step 4: Method - Use the __init__ method to store attributes. Use the describe_car() method to print the formatted information
# Step 5: Logic - When describe_car() is called, it will access the stored attributes and print them


#Task 1:
class Car:
    def __init__(self, make, model, year):
        # Store input data into the object using self
        self.make = make
        self.model = model
        self.year = year

    def describe_car(self):
        print(f"{self.year} {self.make} {self.model}")


# Task 2: Testing the class (Input)
c=Car("Toyota", "Corolla", 2020)
c.describe_car()
#Expected: 2020 Toyota Corolla
