
"""Assignment:
Create a class MathUtils with a static method add(a, b) that returns the sum. 
No class or instance variables should be used.

"""

# Define the MathUtils class
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# Call the static method without creating an object
result = MathUtils.add(5, 7)

print("The sum is:", result)
