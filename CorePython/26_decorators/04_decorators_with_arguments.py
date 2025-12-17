"""
Before following to what we are doing to this file you might have seen in the flask.
Something like this.

import flask

app = flask()

# Here we are passing positional argument to the decorator.
@app.route("/main")
def main():
    return "Hello world"

In this file we are learning how these things gonna work under the hood.
"""

import functools

def prefix_decorator(prefix):
    def decorator_function(original_function):
        @functools.wraps(original_function)
        def wrapper_function(*args, **kwargs):
            print(prefix, "Execution started.")
            result = original_function(*args, **kwargs)
            print(prefix, "Execution ended.")
            return result
        return wrapper_function
    return decorator_function

@prefix_decorator("LOG:")
def hello():
    print("Hello world")

hello()

# This is how we can pass arguments to decorator the original decorator function is just a
# higher order function it doesn't take any other argument despite of the original function.