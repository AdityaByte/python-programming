 # Dealing with environment variables.

"""
os.environ - Class
-> It has various methods and attributes you can read them by dir(os.environ)

1. os.environ - If we print that this will give us a dictionary.
2. os.environ.keys() - give all the keys.
3. os.environ.get(key_name) - Give a specific environment variable.
"""
import os

# Printing all the environment variables. - os.environ.keys() method
# for key in os.environ.keys():
#     print(key, os.environ[key], sep=': ')

# Printing a specific environment variable - os.environ.get(name_of_key)
print(os.environ.get("JAVA_HOME"))

# Check this out if you're dealing with envionment variable.
print(dir(os.environ))
