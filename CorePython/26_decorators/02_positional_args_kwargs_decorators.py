"""
Suppose our original function that we are passing as an argument to the decorator function
has some parameters, So in this file we are learning about how we can pass any number of arguments and
keyword arguments to the decorator wrapper function.
"""

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display():
    print("Hello Aditya")

@decorator_function
def display_info(name, age=0):
    # Name is the simple argument and age is the keyword argument.
    print(f"Hello, I'm {name} and my age is {age}")

display()
display_info("Aditya", 21)

# Under the hood this is what happened that's why
# display_info =  decorator_function(display_info)
# display_info("aditya", 23)