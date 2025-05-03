
"""Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!".

 Apply it to a class Person."""

# Define the class decorator
def add_greeting(cls):
    """Decorator that adds a greet() method to a class."""
    cls.greet = lambda self: "Hello from Decorator!"
    return cls

# Apply the decorator to the Person class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Example usage
p = Person("Alice")
print(p.greet())  # Output: Hello from Decorator!
