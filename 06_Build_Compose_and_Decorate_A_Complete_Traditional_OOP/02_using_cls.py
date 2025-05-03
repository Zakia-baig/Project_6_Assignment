
"""Assignment:
Create a class Counter that keeps track of how many objects have been created.
 Use a class variable and a class method with cls to manage and display the count.
"""

# Define the Counter class
class Counter:
    # Class variable to keep track of object count
    count = 0

    def __init__(self):
        # Jab bhi object banega, count ko 1 se increase karenge
        Counter.count += 1

    @classmethod
    def display_count(cls):
        # Class method to display total number of objects
        print(f"Total objects created: {cls.count}")

# Create some objects
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

# Display total count
Counter.display_count()
