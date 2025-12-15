# Duck Typing and Asking Forgiveness, not Permission.

"""
DUCK TYPING:
-> Duck typing in Python is a programming concept where the type or class of an object is less important
   than the methods or attributes it defines.
"""

class Duck:
    def quack(self):
        print("Quack! Quack!")

    def fly(self):
        print("Duck is flying.")

class Person:
    def quack(self):
        print("Person is quacking..")

    def fly(self):
        print("Person is waving his hands and trying to fly.")

# Non pythonic way of doing things.
def quack_and_fly(thing):

    # Non Duck-Typed (Non - Pythonic)
    # if isinstance(thing, Duck):
    #     thing.quack()
    #     thing.fly()
    # else:
    #     print("Thing is not an instance of duck")

    # LBYL (Look before you leap) - Non-Pythonic
    # if hasattr(thing, 'quack'):
    #     if callable(thing.quack):
    #         thing.quack()
    # if hasattr(thing, 'fly'):
    #     if callable(thing.fly):
    #         thing.fly()
    # else:
    #     print("No attribute exists.")

    # Pythonic Way of doing that.
    try:
        thing.quack()
        thing.fly()
    except AttributeError as e:
        print(e)


duck = Duck()
quack_and_fly(duck)

person = Person()
quack_and_fly(person)