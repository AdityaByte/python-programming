"""
# Logging is a real world use case of decorators in python.
-> Suppose you are debugging your code and you have to check what arguments and keyword arguments are
been passed to every function when it runs.
-> So Despite of logging out in each function you can maintain a separate function for logging and
without altering the pre-existed function actual code.
"""

def logging(orig_func):
    import logging
    logging.basicConfig(filename=f"{orig_func.__name__}.log", level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(
            f"Ran with args: {args} and kwargs: {kwargs}"
        )
        return orig_func(*args, **kwargs)

    return wrapper

# Here we have two functions
@logging
def display(name, age, course=None):
    print(f"Student name: {name} of age: {age} is pursuing this course: {course if not None else 'Engineering'}")

display("aditya", 21, course="Masters in astrophysics")

# Check it out the display.log file for logs.\

"""So from the above code you might understood that why decorators are one of the great design
pattern: Because it allows us to maintain or added functionality at one location and easily applied
anywhere to our code-base."""