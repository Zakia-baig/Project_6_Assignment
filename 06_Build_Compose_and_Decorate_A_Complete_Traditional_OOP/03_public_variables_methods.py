
"""Assignment:
Create a class Car with a public variable brand and a public method start().
 Instantiate the class and access both from outside the class.

"""

# Define the Car class
class Car:
    def __init__(self, brand):
        # Public variable
        self.brand = brand

    # Public method
    def start(self):
        print(f"The {self.brand} car has started.")

# Instantiate (create object) the Car class
my_car = Car("Toyota")

# Access public variable from outside the class
print("Car brand:", my_car.brand)

# Access public method from outside the class
my_car.start()
