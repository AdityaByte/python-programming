"""
First class function:
In python, functions are treated as first class object or first class citizen.
By means of the first class function we understand that function can be treated as other objects.

1. Functions can be assigned to a variable.
2. Functions can be passed as an argument to other function.
3. Functions can be returned from a function.
4. Functions can be stored in other data structures like list.
"""

"""
1. Assigning function reference to a variable.
"""

def greet(name: str): # the str is not type enforcement it is type hinting that It do expect a string argument.
    print(f"Hello, {name.title()}")

# First property ensures function can be assigned to variables like other objects in python like string, integer.
g = greet
print(g) # Prints out the reference of the greet function.
print(g.__name__) # Printing out the name.
g("aditya") # Using variable g for invoking the greet function.


"""
2. Passing function as an argument to another function.
In the below operation we are passing square and cube functions as a argument to the do_operation
function and in the do_operation is a generator function who is yielding the result from first operation.

NOTE: This capability enables powerful programming patterns that's why we are learning these.
"""

def do_operation(fn, list):
    for num in list:
        yield fn(num)

def square(x: int):
    return x*x

def cube(x: int):
    return x**3

squares = do_operation(square, [1,2,3,4,5])
cubes = do_operation(cube, [1,2,3,4,5])
for square in squares:
    print(square)
for cube in cubes:
    print(cube)

"""
3. Returning function from a function.
This allows to further expand it to the closure topic but right now we are only discussing the current topic.

In the below function we do have returned a function from an outer function.
"""
import math

def circle(radius: float):
    pi = math.pi
    def area():
        return pi * (radius ** 2)
    return area

area = circle(3.2)
result = area()
print(round(result, 2))


"""
4. Storing function as normal object to other data-types like in a list.

In the below function we are storing the reference of the function details in the dictionary.
"""

def details(name, major):
    print(f"Hi, I am {name} and I am doing {major}")

person = {
    "name": "aditya",
    "major": "ENGINEERING",
    "details": details
}

person_detail = person["details"]
person_detail(person["name"], person["major"])