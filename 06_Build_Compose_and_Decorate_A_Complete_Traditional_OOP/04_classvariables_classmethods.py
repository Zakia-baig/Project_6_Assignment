

"""Assignment:
Create a class Bank with a class variable bank_name.
 Add a class method change_bank_name(cls, name) that allows changing the bank name.
 Show that it affects all instances.

"""

# Define the Bank class
class Bank:
    # Class variable
    bank_name = "Old Bank"

    @classmethod
    def change_bank_name(cls, name):
        # Class method to change the bank name
        cls.bank_name = name

    def display_bank_name(self):
        # Instance method to display current bank name
        print(f"Bank Name: {self.bank_name}")

# Create instances of Bank
customer1 = Bank()
customer2 = Bank()

# Display bank name before change
print("Before changing bank name:")
customer1.display_bank_name()
customer2.display_bank_name()

# Change the bank name using class method
Bank.change_bank_name("New Era Bank")

# Display bank name after change
print("\nAfter changing bank name:")
customer1.display_bank_name()
customer2.display_bank_name()
