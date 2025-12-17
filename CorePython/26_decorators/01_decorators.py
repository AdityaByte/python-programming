"""
IMPORTANT: Thinking of you know about first class functions and closure as a general programming concept.

Decorator:
A decorator is a design pattern which allows the user to add additional functionality to the pre-existed object
without modifying its structure.

It is essentially a function that takes another function as an argument and returns a new function with enhanced or
altered behavior, without changing the original function's code.

So Question may arise in our mind why we need to enhance a pre-existed object without changing its code.
Example:
-> Think it of a scenario where you have a route /order which can only be accessed when you are logged in.
So You keep the /order route function has the order related data and place a decorator @login_required over it so that it
runs the login function first and then came back to the order.
"""

# Example 1:
def decorator_function(original_function):
    def wrapper_function():
        print(f"Wrapper executed this before: {original_function.__name__}")
        return original_function()
    return  wrapper_function

def display():
    print("Display Function Ran")

"""What we did here?
Here we pass the display function as an argument to the decorator function then the function returns the inner function by calling the
original function that was passed."""
decorated_display = decorator_function(display)
decorated_display()


print("------------------------------------------")
# Example 2:
# Now in this example we are coming forward to actually grasp what happens under the hood
# when we put an annotation like @decorator_name over a function.

def another_decorator_func(original_function):
    def wrapper_function():
        print("Doing some other tasks")
        return original_function()
    return wrapper_function

def greet():
    print("Hello world")

greet = another_decorator_func(greet)
greet()



print("-------------------------------------")
# Example 3: Using the decorator annoation - for clean code.

def outer_function(argument_function):
    def wrapper_function():
        print("I am doing some additional task here.")
        return argument_function()
    return wrapper_function

@outer_function # This annotation has the name of the name of the decorator function.
def say_namaste():
    print("Namaste World")

say_namaste()