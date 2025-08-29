"""
Scope:
Python follows the LEGB rule:
Local, Enclosing, Global, Builtins

Means: It firstly search the variable at the local scope then at the enclosing scope
then at the global scope if it didn't find in the global scope then it search it in the builtins.

Note: Builtins module is always loaded automatically to every python file.
"""

global_var = "aditya"

def main():
    local_var = "aditya1"
    print(local_var)
    print(global_var)

main()
print(global_var)
# print(local_var) # We cannot use the local variable of main function here.

# Learning more about scope and all.

# This is the global var
name = "aditya"

def func():
    name = "yeshank"
    def another_func():
        nonlocal name
        name = "something"
        print(name)

    another_func()
    print(name)

func()
print(name)

# Assumption:
"""
Expected output:
something
something
something
"""

# The above thing was just a practice for learning things.

"""Conclusion:
-> `global` keyword :-
    * When we put the global keyword to any variable then it could be accessed globally and can also we modified globally.
    * If the variable defination is not in the global scope and you had directly define it inside the function then python
        creates the definition of it.

-> `nonlocal` keyword :-
    * NonLocal keyword refers the enclosing scope variables like an example of this case is if we define another function
        inside a function and if we want to access the same variable which was defined in the parent function so in that case
        nonlocal keyword was usually used.
"""

# Builtins
# print(dir(__builtins__))
# Like here we have a min and max function which gives the minimum and maximum element of a list.
# print(help(min))

# Let we have a list of elements.

# We have overrided the min function of builtins.
def min():
    pass

nums = [1,28,9,21,90]
print(min(nums))

# Note: In the above example we have created the same name function which was existed in the builtins
# so the python interpreter search first the function in the local -> enclosing -> global scope then if it
# didn't find it then it search its in the builtins.