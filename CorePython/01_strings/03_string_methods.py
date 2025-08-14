# str is a class in python so when we create a str we can use the class methods.
# Note: Method is the function associated with an object and function is just a normal function which performs
# some operations.

my_string = "aditya pawar"

# lower() - lowercase
print(my_string.lower())

# upper() - uppercase
print(my_string.upper())

# title() - titlecase
print(my_string.title())

# capatilize() - capatilize
print(my_string.capitalize()) # Only the first letter of the sentence is capital.

# count() - for counting a character or a string inside a string.
# one arity function expects a string as argument.
# If not exists returns 0 - not found
print(my_string.count("aditya")) # print 1
print(my_string.count("z")) # prints 4

# find() - Returns the index of the very first occurance of the character or the string.
# If not exists return -1
print(my_string.find("g"))

# replace() - If we want to replace some string to a string.
# It takes two arguments what you wanna replace by whom.
# first argument takes the actual word and next one is the new word.
# It replace all the occurance
some_str = "hello my name is aditya hello aditya"
some_str = some_str.replace("m", "z")
print(some_str)

# String concatination
greeting = "hello"
name = "aditya"
# Easiest way of doing that by using + sign.
message = greeting + ", " + name + ". Welcome!"
print(message)
# Another way of doing that by using the format function and placeholders.
message = "{}, {}. Welcome!".format(greeting, name)
print(message)
# Another way - f strings
print(f"{greeting}, {name}. Welcome!")