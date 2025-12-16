"""
Closure: (Wikipedia definition)
In programming languages, a closure, also lexical closure or function closure,
is a technique for implementing lexically scoped name binding in a language with first-class-functions.
Operationally, a closure is a record storing a function together with an environment.

Lexical variables are known as free variables (Variables that are used locally defined in an enclosing scope).

Closure = function + lexical scope (Remembered State). (But keep in mind it is not a nested function) ok.

Simpler terms: A closure is a combination of a function and the lexical environment in which it was defined,
allowing the function to access of hold the variables even after the execution of the outer function has been done.

Python specific definition: A closure in Python is a callable that retains access to variables from its enclosing lexical scope,
even after the outer function has finished execution.
"""

# Example.
# Let us keep an example where we are defining two function outer_function and inner_function and inner function
# is access the lexical scope variables.

def outer_function(msg):
    message = msg
    def inner_function():
        print(f"Message is {message}")
    return inner_function # Returning the reference so that we can call it whenever its needed.

inner_func = outer_function("Hey there.")

# IMPORTANT: Must read.
# Now what is happening.
# A closure is formed when an inner function captures and retains access to variables from its enclosing lexical scope.
# Even after the outer function finishes execution and its stack frame is destroyed,
# the captured variables remain alive because they are referenced by the inner function.
# This combination of function behavior and preserved state is called a closure.

inner_func()
inner_func()
print(inner_func.__closure__) # Returns a cell object that shows the captured variable.