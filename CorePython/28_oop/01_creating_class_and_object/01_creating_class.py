"""
Class

A class is a blueprint used to create multiple objects that share the same
attributes (properties) and methods (behaviors).

Example:

    class Car:
        def __init__(self, color, engine, fuel):
            self.color = color
            self.engine = engine
            self.fuel = fuel

        def gear(self, gear):
            pass

        def accelerate(self):
            pass

        def stop(self):
            pass

The Car class represents a blueprint of a car. It defines common attributes
such as color, engine, and fuel, along with methods like gear, accelerate,
and stop.

Objects:
Objects are instances created from a class. Each object has its own data
but follows the structure defined by the class.

Example:
    mustang = Car("black", "60hp", "petrol")
    endeavour = Car("white", "80hp", "diesel")

Object-Oriented Programming (OOP):
Object-Oriented Programming is a programming paradigm that organizes code
using classes and objects. It is similar to other paradigms such as
Procedural-Oriented Programming (POP) and Functional-Oriented Programming (FOP).

Like other paradigms, OOP has its own advantages and disadvantages.
"""

# In this file we are just tending to how to create a class in python.
# class keyword is used for creating a class in python.

class Car:

    """
    __init__() Method

    The __init__() method is a constructor that initializes an object.
    Its first parameter refers to the current instance being created,
    allowing the method to initialize that specific instance among
    multiple instances of the class.
    """

    def __init__(self, color, engine, fuel):
        self.color = color
        self.engine = engine
        self.fuel = fuel
        self.speedometer = 0
        self.gear = 1

    # Now For creating the instance method they have to take
    # first argument as self (by naming convention you can give any other name too)

    def accelerate(self):
        self.speedometer += 10 # Increasing the speed by 10.
        print(f"Speeding by {self.speedometer}")

    def brake(self):
        if self.speedometer != 0:
            self.speedometer -= 10
        print(f"Slowing by {self.speedometer}")

    def change_gear(self, gear):
        if gear in range(1,6):
            self.gear = gear
        print(f"Switch to gear {self.gear}")


# Now creating object of the class Car.
mustangGT = Car("Black", "70HP", "Petrol")
# Now question may arise to newcomers in python that the init method takes 4 argument the first is self
# but here we are only giving 3 argument so it doesn't make conflict.
# Answer: No as in internals the first argument is been passed automatically.

# Now we can call the instance method via the dot(.) operator.
mustangGT.accelerate()
mustangGT.change_gear(3)
mustangGT.brake()

# Now under the hood how these methods are calling.
# We can call the methods in the same way as by the Class reference too.
Car.accelerate(mustangGT)
Car.accelerate(mustangGT)
Car.change_gear(mustangGT, 5)


# Something like
# ClassReference.method(instance, any_arg_or_kwarg)
# Otherwise
# Instance.method(any_arg_or_kwarg)