"""Random Module:
This module is mainly around of random data.
For Example: If we have to select a number randomly we can use this module.
Although for security purpose data such as OTP Generation and all, python recommend secret module for that.

Random module is the part of standard library of python.

Methods:
    Note: For finding what the method do's we can use the help() builtin function.
    Note: For finding how many method does the module have we can use the dir() builtin function. (This was just for revision).

So the first method that we have been discussing is the random() method.

1. random.random()
-> It return value between 0 and 1 as of 0 is inclusive (means we can get zero) and 1 is
exclusive (means we cannot get exact 1 by any chance).

2. random.uniform(a, b)
-> If we want a floor value within a specified range of number we can use this method.

3. random.randint(a, b)
-> If we want a whole or integer value we can use this function.
-> It returns a random integer in range [a, b], including both end points. (means both are inclusive).
-> Although in many case we do want an integer number so this method is useful.

4. random.choice(list)
-> It is an another method of the random module.
-> It takes a list of values and returns a random value from the list.

5. random.choices(list)4
-> NOTE: IMPORTANT: With the choices function it can also grab a single items one or more item from a list.
    So if you want to select unique items from a list you can use the random.sample(list) method.
-> If we want a random list of choices we can use the choices function.
-> It takes usually three parameters which are,
    1. k=int : It takes how many choices we have to make, like we want 10 choices so k=10.
    2. weights=[]: It takes a list of weight something like if we have 100 total weight and we have three items
        out of which we have to select 10 choices then the weight of the first items is 50 that means.
        It has the highest possibility to come in the choices.
        Check out the function choices_function() for its detail implementation.

-> Note: If we just pass the list to the random.choices() function then it behaves like the choice function,
and returns out a single item randomly.

6. random.shuffle(list)
-> If we have to randomly shuffle a list (inplace: we don't need another variable it just mutate the
original list) we can use this function.

7. random.sample(list, k=int)
-> If we want to select unique values from a list we can use the sample function, although the choices
may select the same value one more time.

"""

# First for using the random module we have to import it.
import random


def random_function():
    value = random.random()
    print(value)  # It will give a floor value within a range of 0 to 1.


def uniform_function():
    value = random.uniform(10, 20)
    print(value)  # Here we get a random floating point value between 10 and 20.


def randint_function():
    # print(help(random.randint))
    # Suppose we want a random dice number.
    dice_num = random.randint(1, 6)
    print(dice_num)


def choice_function():
    greetings = ['hello', 'hola', 'hi', 'namaste', 'monjour']
    random_greet = random.choice(greetings)
    print(f"{random_greet.title()}, Aditya")


def choices_function():
    balls = ["red", "black", "blue"]
    # I want 10 successive choices.
    random_balls = random.choices(balls, k=10, weights=[50, 10, 40])  # possibility to come -> red > blue > black.
    print(random_balls)


def shuffle_function():
    # Suppose we had a deck of 52 cards and we have to shuffle them.
    deck = list(range(1, 53))
    print("Original deck", deck)
    random.shuffle(deck)
    print("Shuffled deck", deck)


def sample_function():
    deck = list(range(1, 52))  # we have a deck of 52 cards and we have to select 3 cards from it.
    three_cards = random.sample(deck, k=3)
    print(three_cards)


def main():
    sample_function()


if __name__ == "__main__":
    main()
