
"""Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization.
 Access a method of the Engine class via the Car class."""

# Engine class
class Engine:
    def start(self):
        return "Engine has started."

# Car class using composition
class Car:
    def __init__(self, engine):
        self.engine = engine  # Engine object is part of Car

    def start_car(self):
        return self.engine.start()  # Accessing Engine's method through Car


# Example usage
engine = Engine()
my_car = Car(engine)

print(my_car.start_car())
