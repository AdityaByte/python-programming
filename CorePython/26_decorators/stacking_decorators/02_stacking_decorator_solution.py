"""
In this file we are taking the whole code of the 01 file and with some enhancement that how to properly
stack two decorators over one function.
"""

from functools import wraps # importing wraps function from functools.
import time
import logging

def logger(orig_func):
    logging.basicConfig(filename=f"{orig_func.__name__}.log", level=logging.INFO)

    # You need to wrap the wrapper function.
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(f"{orig_func.__name__} ran with args: {args} and kwargs: {kwargs}")
        return orig_func(*args, **kwargs)
    return wrapper

def timer(orig_func):

    # You need to wrap the wrapper function with original function.
    @wraps(orig_func)
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