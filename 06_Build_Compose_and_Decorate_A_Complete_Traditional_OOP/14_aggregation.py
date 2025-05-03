
"""Create a class Department and a class Employee. 
Use aggregation by having a Department object store a reference to an Employee object that exists independently of it."""

# Employee class
class Employee:
    def __init__(self, name):
        self.name = name

    def get_details(self):
        return f"Employee Name: {self.name}"


# Department class using aggregation
class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  # Aggregation: storing reference to an existing Employee

    def show_department_info(self):
        return f"Department: {self.dept_name}, {self.employee.get_details()}"


# Example usage
emp = Employee("Alice")
dept = Department("HR", emp)

print(dept.show_department_info())
