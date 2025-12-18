"""
NamedTuple:
namedtuple() is a factory function that creates tuple subclasses
with named fields.

Why do we need namedtuple when we already have tuple?
-> It improves code readability and self-documentation.
-> It allows accessing values by meaningful names instead of indexes.
-> This makes the code easier to understand and maintain.
"""

# Creating a color value using a normal tuple.
# RGB color format: (red, green, blue)
dodger_blue = (55, 155, 255)

print(dodger_blue[0])  # Red value (not very clear from the code itself)

# Someone reading this code cannot easily understand
# what each index represents.

from collections import namedtuple

Color = namedtuple('Color', ['red', 'green', 'blue'])

dodger_blue = Color(55, 155, 255)

print(dodger_blue[0])     # Still works like a tuple
print(dodger_blue.red)   # Much more readable and clear

# NOTE:
# Use namedtuple when positional values need clear meaning.
# It provides readability while remaining lightweight and immutable.
