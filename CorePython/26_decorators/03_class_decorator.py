"""
Class Decorators:
Class decorators often provide the same functionality as the function decorators but some people
often do prefer class decorators.
"""

class decorator_class(object):
    def __init__(self, original_function):
        # Creating this so that the original_function being the part of an instance.
        self.original_function = original_function

    # For Creating the wrapper_function in class decorator
    # we need to make a __call__() function out there.
    def __call__(self, *args, **kwargs):
        print(f"Call method is executed before the execution of this function: {self.original_function.__name__}")
        return self.original_function(*args, **kwargs)

# We have to provide the annotation to it.

@decorator_class
def display():
    print("Hello world")

@decorator_class
def display_info(name, age):
    print(f"Hello, My name is {name} and mine age is {age}")

display()
print("-----------------")
display_info("Aditya", 21)