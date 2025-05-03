
"""Create a class Person with a constructor that sets the name. 
Inherit a class Teacher from it, add a subject field, and use super() 
to call the base class constructor."""

# Base class
class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person constructor called. Name: {self.name}")

# Derived class
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Call base class constructor
        self.subject = subject
        print(f"Teacher constructor called. Subject: {self.subject}")


# Example usage
t = Teacher("Mr. Smith", "Mathematics")
