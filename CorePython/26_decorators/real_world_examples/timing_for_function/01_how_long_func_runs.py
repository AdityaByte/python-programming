"""
Timing How long the function is running for various function for performance report.
So rather than pasting out the logic for timing we can keep it as one place with the help of
decorators and also in some case we cannot change the function body too.
"""
import time

def my_timer(orig_func):

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print(f"{orig_func.__name__} ran in {t2} seconds")
        return result

    return wrapper

@my_timer
def display_info(name):
    time.sleep(1)
    print(f"Hi, I'm {name}")

display_info("Aditya")
