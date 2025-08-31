# Sorting Objects.

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self) -> str:
        return f"[{self.name}, {self.age}, ${self.salary}]"

e1 = Employee("aditya", 21, 10000000)
e2 = Employee("yeshank", 25, 90000000000)
e3 = Employee("someone", 8, 50000)

employees = [e1, e2, e3]

"""Now you have to sort the employee based on some cases:
case1: sort employees based on age.
case2: sort employees based on their salary in decreasing order.
case3: sorting employees based on their name dict."""

# Case 1:
# Using User defined function
def sort_logic1(emp):
    return emp.age

s_emply1 = sorted(employees, key=sort_logic1)
print(s_emply1)

# Case 2:
# Using lambdas
s_emply2 = sorted(employees, key=lambda e: e.salary, reverse=True)
print(s_emply2)

# Case 3:
# Using the attrgetter function of operator module.
from operator import attrgetter
s_emply3 = sorted(employees, key=attrgetter("name"))
print(s_emply3)