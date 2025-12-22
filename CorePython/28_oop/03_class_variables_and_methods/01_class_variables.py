"""
Class Variables:
- Class variables are shared across all instances of a class.
- Class variables are also known as static variables.
- Only one copy of a class variable exists, and it belongs to the class,
  not to individual objects.
"""

class Employee:

    # Monthly bonus is common for all employees (class variable)
    monthly_bonus = 1.04  # 4% increment

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    # __str__ method (similar to toString in Java)
    def __str__(self):
        return f"Employee Details[name={self.name}, age={self.age}, salary={self.salary}]"

    def apply_bonus(self):
        # Accessing class variable using class reference
        # self.salary = self.salary * Employee.monthly_bonus

        # Accessing class variable using instance reference
        self.salary = self.salary * self.monthly_bonus

        """
        Why class variables can be accessed via an instance:

        When an attribute is accessed using an instance, Python first looks
        in the instance namespace (__dict__). If the attribute is not found,
        Python then looks in the class namespace. If it exists there, the
        class variable is returned.

        This is why class variables can be accessed using instance references.
        """


# Creating an employee object
emp1 = Employee("Aditya", 21, 2_500_000)
print(emp1)  # __str__() is called automatically

# Accessing the class variable via class and instance
print(Employee.monthly_bonus)
print(emp1.monthly_bonus)

# Applying bonus (4% increment)
emp1.apply_bonus()
print(emp1)

# Printing namespaces
print(emp1.__dict__)
print(Employee.__dict__)

# Updating the class variable using an instance
emp1.monthly_bonus = 2  # 100% hike
emp1.apply_bonus()
print(emp1)

"""
Important Note:
Assigning a value to a class variable via an instance does NOT modify
the class variable. Instead, it creates a new instance variable with
the same name, which shadows the class variable for that instance only.
"""
