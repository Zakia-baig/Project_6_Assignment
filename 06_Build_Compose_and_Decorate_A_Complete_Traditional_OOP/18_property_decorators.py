
"""Create a class Product with a private attribute _price. Use @property to get the price,

 @price.setter to update it, and @price.deleter to delete it."""


class Product:
    def __init__(self, price):
        """Initialize the product with a private price attribute."""
        self._price = price

    @property
    def price(self):
        """Getter method to access the price."""
        return self._price

    @price.setter
    def price(self, new_price):
        """Setter method to update the price with validation."""
        if new_price < 0:
            raise ValueError("Price cannot be negative.")
        self._price = new_price

    @price.deleter
    def price(self):
        """Deleter method to remove the price."""
        print("Deleting price...")
        del self._price

# Example usage:
product = Product(100)
print(f"Initial Price: {product.price}")

product.price = 150  # Updating price
print(f"Updated Price: {product.price}")

del product.price  # Deleting price
