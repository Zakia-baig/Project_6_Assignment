
"""Write a decorator function log_function_call that prints "Function is being called"

 before a function executes. Apply it to a function say_hello()."""

# Define the decorator function
def log_function_call(func):
    """Decorator that logs a message before a function executes."""
    def wrapper(*args, **kwargs):
        print("Function is being called")
        return func(*args, **kwargs)
    return wrapper

# Apply the decorator to say_hello function
@log_function_call
def say_hello():
    print("Hello, world!")

# Test the decorated function
say_hello()
