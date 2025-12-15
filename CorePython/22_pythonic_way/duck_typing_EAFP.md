# Duck Typing
> Duck Typing is a concept in Python where an object's suitability is determined by the presence of certain methods or properties, rather than its actual type. The principle follows: <i>"If it walks like a duck and quacks like a duck, then it's a duck."</i> This means that if an object behaves like a certain type, it can be treated as that type, promoting flexibility and polymorphism.

- Focuses on behavior, not type.
- Avoids `isinstance()` checks.
- Encourages interface-based design.

# EAFP (Easier to Ask for Forgiveness than Permission)
> EAFP is a Python coding style that assumes an operation will succeed and handles exceptions if it fails. It uses try-except blocks to catch errors, making code cleaner and thread-safe.

```python
try:
    print(obj.some_method())
except AttributeError:
    print("Method not available")   
```

- Pythonic and preferred in Python.
- Reduces race conditions in multi-threaded code.
- Aligns well with duck typing

# LBYL (Look Before You Leap)
> LBYL is a programming style where conditions are explicitly checked before performing an operation, using if statements.

```python
if hasattr(obj, 'some_method'):
    print(obj.some_method())
else:
    print("Method not available")   
```

- Common in languages like C.
- Can lead to race conditions (e.g., in threading).
- Less preferred in Python due to verbosity and performance.