
"""Create a class Countdown that takes a start number.

 Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0."""

class Countdown:
    def __init__(self, start):
        """Initialize the countdown with the given start number."""
        self.current = start

    def __iter__(self):
        """Return the iterator object itself."""
        return self

    def __next__(self):
        """Return the next number in the countdown, stopping at 0."""
        if self.current < 0:
            raise StopIteration  # Stop iteration when it goes below 0
        value = self.current
        self.current -= 1
        return value

# Example usage:
countdown = Countdown(5)
for number in countdown:
    print(number)


