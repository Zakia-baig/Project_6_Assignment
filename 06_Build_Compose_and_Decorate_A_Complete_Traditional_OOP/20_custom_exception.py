

"""Create a custom exception InvalidAgeError.

 Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except."""


class InvalidAgeError(Exception):
    """Custom exception for invalid age."""
    def __init__(self, message="Age must be 18 or above."):
        self.message = message
        super().__init__(self.message)

def check_age(age):
    """Checks if age is valid and raises an exception if age is below 18."""
    if age < 18:
        raise InvalidAgeError(f"Invalid age: {age}. You must be at least 18 years old.")
    print(f"Age {age} is valid.")

# Handling the exception
try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except InvalidAgeError as e:
    print(f"Error: {e}")
except ValueError:
    print("Invalid input! Please enter a valid number.")
