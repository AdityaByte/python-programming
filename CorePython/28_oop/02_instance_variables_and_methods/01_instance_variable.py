"""
Instance Variables:
Instance variables store data that is unique to each object.
Memory for instance variables is allocated when an object is created,
not when the class is defined.
"""

class Employee:
    """
    Employee class representing an employee with name, age, and salary.
    """

    # Constructor / Initialization method
    # self refers to the current object (similar to 'this' in Java)
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    # Instance method
    # Methods are shared across all instances but operate on instance data
    def get_salary(self):
        return self.salary


# Creating employee objects
emp1 = Employee("Aditya", 20, 30000)
emp2 = Employee("Rahul", 22, 35000)