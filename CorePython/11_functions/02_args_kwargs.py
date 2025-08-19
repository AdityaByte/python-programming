# Arguments and Keyword Arguments in python.
# Let we have a function which accepts the args and kwargs as parameter.

'''
*args = variable number of positional arguments → tuple.
**kwargs = variable number of keyword arguments → dict.
'''

def func(*args, **kwargs):
    """ Args will print out the arguments which are passed
    like if we call this function like this func("helo", "world", name="aditya", age=21)
    so "hello" and "world" are the arguments
    and name="aditya" and age=21 are the keyword arguments.
    """
    print(args)
    print(kwargs)

# Here we simply passed the unpacked values across the function.
func("hello", "world", name="aditya", age=21)

# Think of we have a list of arguments and we have a mapping too then we can send that too.
arg1 = ["arg1", "arg2", "arg3"]
data = {"name": "aditya", "surname": "pawar"}
func(*arg1, **data) # unpacking them

# Let us take an example that we have a sum function which takes lot of values as argument and return their sum.
def sum(*args):
    sum = 0
    for val in args:
        sum += val
    return sum

print(sum(10,20,30,40)) # prints 100

# Note: By default if a function is not returning anything it returns None.