
"""Create a class Employee with:

a public variable name,

a protected variable _salary, and

a private variable __ssn.

Try accessing all three variables from an object of the class and document what happens."""

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # Public variable
        self._salary = salary     # Protected variable (by convention)
        self.__ssn = ssn          # Private variable (name mangled)


# Create an object of the class
emp = Employee("Alice", 50000, "123-45-6789")

# Accessing the public variable
print("Name:", emp.name)  # ✅ Works fine

# Accessing the protected variable
print("Salary:", emp._salary)  # ⚠️ Works, but not recommended (it's "protected" by convention)

# Accessing the private variable
try:
    print("SSN:", emp.__ssn)  # ❌ Will raise AttributeError
except AttributeError as e:
    print("Error accessing __ssn:", e)

# Accessing the private variable using name mangling
print("SSN (via name mangling):", emp._Employee__ssn)  # ✅ Works, but not recommended
