"""
Before reading this file checkout out the real world example first because I am taking those examples for
defining what problem we are figuring out when we are stacking multiple decorators to a function.
"""

# Suppose we have two function one is for logging and one is for timer for checking how much time the function is taking.
import time
import logging

def logger(orig_func):
    logging.basicConfig(filename=f"{orig_func.__name__}.log", level=logging.INFO)
    def wrapper(*args, **kwargs):
        logging.info(f"{orig_func.__name__} ran with args: {args} and kwargs: {kwargs}")
        return orig_func(*args, **kwargs)
    return wrapper

def timer(orig_func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print(f"Time taken by {orig_func.__name__} is {t2} seconds.")
        return result
    return wrapper


# Stacking both the decorators above it.
@timer
@logger
def display(name):
    time.sleep(1)
    print(f"Hi, I'm {name}")

display("Aditya")

# But at the end you find something unsual.
# I can tell you why.
# Here firstly the logger has been runs and logs out in the log file and after that the result of it
# which is the reference of the wrapper function inside logger is passed to the timer function and then it
# logs something like that - Time taken by wrapper is 1.0127856731414795 seconds.

# The above thing in the paragraph is similar to this.
"""
display = timer(logger(display))
# logger returns wrapper reference which then passed to timer as original_function and then it run it ok.

To solve this issue or properly stack them without losing the property of the original function.
We use the functools and wraps() function for that.

Check out the 02_stacking_decorator_solution.py 
"""