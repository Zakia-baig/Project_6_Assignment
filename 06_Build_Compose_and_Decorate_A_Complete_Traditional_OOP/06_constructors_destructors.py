
"""Create a class Logger that prints a message when an object 
is created (constructor) and another message when it is destroyed (destructor)."""


class Logger:
    def __init__(self):
        print("Logger object has been created.")

    def __del__(self):
        print("Logger object has been destroyed.")


# Example usage
logger = Logger()

# You can manually delete the object to trigger the destructor
del logger

# Or let it go out of scope at the end of the program or function
