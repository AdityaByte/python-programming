# Functions: Functions are the block of code which are used for performing a certain task.
# Functions takes some input and perform some computation and calculation as per your logic and generate some output.
# def - keyword is used for the defination of the function.

def hello_func():
    print("Hello world!")

hello_func()

# Parameters and arguments.
def another_func(name, age):
    return "Hello, {0} your age is {1}".format(name, age)

# Passing arguments to the function.
result = another_func("aditya", 21)
print(result)

# How to define a default value to a function parameter.
# and doc string.
def default_value_func(name="User"):
    """This is the doc-string for a functional block""" # This string will prints out if we perform the help() to this function.
    print(f"Hello, {name.title()}!")

print(help(default_value_func))

