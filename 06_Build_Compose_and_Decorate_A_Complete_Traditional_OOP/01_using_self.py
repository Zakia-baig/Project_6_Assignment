"""Assignment:
Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. 
Add a method display() that prints student details."""



# Define the Student class
class Student:
    def __init__(self, name, marks):
        self.name = name    # initialize name
        self.marks = marks  # initialize marks

    def display(self):
        # method to display student details
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")

# Create objects of Student class
student1 = Student("Zakia", 88)
student2 = Student("Sara", 92)

# Call the display method for each student
student1.display()
 
print()  # blank line for better readability
student2.display()
