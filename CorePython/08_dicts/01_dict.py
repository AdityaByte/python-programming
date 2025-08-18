# Dictionary Datatype:
'''
Just like map python has dictionary which is a collection of key-value pairs.
Key Points:
1. Dictionary is also mutable.
2. Dictionary is being created inside {}.
3. Key must be in string.
'''

# Empty dictionary:
empty_dict = {}
print(type(empty_dict))
empty_dict = dict()
print(type(empty_dict))

student = {
    "name": "aditya",
    "age": 21,
    "lang": ["Java", "Golang", "Python"]
}

print(student)

# Accessing the items of the dictionary
# Two ways: By using get() method and by using [].
print(student["name"])
# There is a con of using [] if we put down a key which doesn't exists then it will throw error: KeyError.
print(student.get("name"))
print(student.get("phone")) # Phone key doesn't exists then it will throw default value which is None.
# Otherwise you can also specify the default value if the key doesn't exists in the dict in that case.
print(student.get("phone", "+1-123"))

# Adding an item to dictionary
student["phone"] = "+1-123"
print(student)

# Methods which came with the dictionary
print(dir(dict))
''' These are the methods which came with the dict datatype:
'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'
'''

print(help(dict.clear)) # You can also know what the function does by this.