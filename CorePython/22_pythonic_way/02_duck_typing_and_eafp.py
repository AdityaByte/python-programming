# Duck Typing and Asking forgiveness, Not Permission.

"""
EAFP (Easier to ask forgiveness than permission):
EAFP stands for Easier to Ask for Forgiveness than Permission,
a coding philosophy commonly used in Python.
It encourages writing code that assumes operations will succeed and handles exceptions if they fail,
rather than checking conditions beforehand.
"""

# Example.
# Suppose we have a dictionary which has some keys and we are accessing those keys.

# person = {"name": "aditya", "age": 21, "addr": "washington"}
person = {"name": "george bush", "age": 42}

# Non-Pythonic Way of doing that.
# Asking for permission that the keys that we were accessing are exists or not.
if "name" in person and "age" in person and "addr" in person:
    print(f"Hello my name is {person['name']}, I'm {person['age']} yrs old and I live in {person['addr']}")
else:
    print("Some keys are missing.")

# EAFP Priniciple:
# Assuming the person dict has all the attributes and we are just accessing them.
try:
    print(f"Hello my name is {person['name']}, I'm {person['age']} yrs old and I live in {person['addr']}")
except KeyError as e:
    print(f"{e} is missing")