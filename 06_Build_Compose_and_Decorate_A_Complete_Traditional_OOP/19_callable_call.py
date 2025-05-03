
"""Create a class Multiplier with an __init__() to set a factor. 

Define a __call__() method that multiplies an input by the factor.

 Test it with callable() and by calling the object like a function."""

class Multiplier:
    def __init__(self, factor):
        """Initialize the multiplier with a given factor."""
        self.factor = factor

    def __call__(self, value):
        """Multiply the input value by the factor."""
        return value * self.factor

# Create an instance of Multiplier with a factor of 3
multiplier = Multiplier(3)

# Test if the object is callable
print(callable(multiplier))  # Output: True

# Call the object like a function
result = multiplier(5)
print(f"Multiplying 5 by factor 3 gives: {result}")  # Output: 15
