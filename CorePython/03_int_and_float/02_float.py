# Floating point numbers.

a = 3.14
print(type(a)) # <class 'float'>

# Same operations as of the integer.

# Methods:
print(round(a))
print(round(a, 1)) # Round upto 1 decimal place.

# Note: The floor and ceil method are in the math module.

# Formatting float with Python's mini format language.
import math

pi = math.pi
print(f"{pi:.3f}") # Round of to 3 decimal places.