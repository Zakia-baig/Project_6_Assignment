
"""Use the abc module to create an abstract class Shape with an abstract method area(). 
Inherit a class Rectangle that implements area()."""

from abc import ABC, abstractmethod

# Abstract base class
class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass  # Abstract method with no implementation

# Derived class
class Rectangle(Shape):
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# Example usage
rect = Rectangle(7, 4)
print("Area of rectangle:", rect.area())
