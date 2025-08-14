# String formatting

# Basic Way - Through + operator
person = {"name": "aditya", "age": 21}
# The most simple and non-readable way of doing that
sentence = "hello i'm " + person["name"] + " and i'm " + str(person["age"]) + " years old."
print(sentence)

# Through came string formatting
# {} are the placeholders and they are in order first argument is to be passed into first placeholder as so on.
sentence = "hello i'm {} and i'm {} years old.".format(person["name"], person["age"])
print(sentence)

# Numbering the placeholders.
# 0 -> first value passed in the format and 1 -> second value passed in the format.
sentence = "hello i'm {0} and i'm {1} years old.".format(person["name"], person["age"])
print(sentence)

# The upper thing is more useful then the values need to be repeated like this below example
text = '''<{0}>
{1}
</{0}>'''.format("h1", "hello i'm aditya")
print(text)

# We can also do the following thing inside the placeholder
# like we have a dictionary
dict_data = {
    "username": "aditya-pawar",
    "password": "aditya123"
}
message = "Your username is {0[username]} and password is {1[password]}".format(dict_data, dict_data)
print(message)
# You can more simply it as
message = "Your username is {0[username]} and password is {0[password]}".format(dict_data)
print(message)

# We can also access the value of the list too inside the placeholder via index.
list_data = ["aditya", 21]
message = "My name is {0[0]} and my age is {0[1]}".format(list_data)
print(message)

# We can also access the attributes of a class in the similar way
class PersonClass:
    def __init__(self):
        self.firstname = "aditya"
        self.lastname = "pawar"

new_person = PersonClass()
message = "Hey my fullname is {0.firstname} {0.lastname}".format(new_person)
print(message)

# Accessing the keyword arguments to format.
sentence = "Somebody is calling me whose name is {name}".format(name="aditya")
print(sentence)

# Unpacking in list and dictionary
data = {"company": "couchbase", "type": "product-based"}
sentence = "The {company} is a {type} based company".format(**data)
print(sentence)

# How to format numbers in a string.
for i in range(1,11):
    # Number formatting is done through after a colon(:) like
    # For 2 digit padding -> :02
    # For 3 digit padding -> :03
    sentence = "The value is {:02}".format(i)
    print(sentence)

# Formatting the float values to decimal places.
# Like if we have to round it upto 2 decimal places.
pi = 3.14159265
sentence = "Pi is equal to {:.2f}".format(pi)
print(sentence)

# Print out a large number with comma seperator
print("1 MB is equal to {:,}".format(1000**2))

# How to format dates.
import datetime
my_date = datetime.datetime(2025, 8, 14, 7, 13, 12)
print(my_date)
# But we wants in this format Month Date, Year Note: Month like this March.
new_date = "{:%B %d, %Y}".format(my_date)
print(new_date)
print("{0:%B %d, %Y} is fell on {0:%A} and was the {0:%j} of the year".format(my_date))