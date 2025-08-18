# Methods which are came with the dict datatype:
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'

print(help(dict.clear))
# 1. clear() -> None(Return Type). Remove all items from D
data = {
    "one": 1,
    "two": 2
}
print(data)
data.clear()
print(data) # {}


# 2. copy() -> Returns a shallow copy of Dict.
# Shallow copy: It just copy the references of the dict but they too are pointing to the same data as of the old dict does.
print(help(dict.copy))

dict1 = {
    "data": {
        "more_data": {
            "hello": "world"
        }
    }
}

shallow_dict = dict1.copy()
# If we change the shallow dict then the original dict will also be changed.
shallow_dict["data"]["more_data"] = {"hello", "Kya hai be"}
print(dict1)

# 3. fromKeys(iterable, default_value) method - It will create a dictionary from a iterable(list) and set the value as None(By default) but you can change it too.
print(help(dict.fromkeys))
my_list = ["hello", "world"]
my_dict = {}
new_dict = my_dict.fromkeys(my_list, "helloworld")
print(new_dict)


student = {
    'name': 'aditya pawar',
    'age': 21
}

# 4. get(key) -> value. Accessing the item from the dictionary.
print(f"The age of {student.get('name')} is {student.get('age')}")

# 5. Updating the items of the list like here we have a student datatype and we want to change many things
# out of this then we can use the update method.
# update() method.
student.update({"name": "elon musk", "age": 43, "companies": ["spacex", "tesla"]}) # we can add new values to it.
print(student)

# 6. pop() method: D.pop(key) -> v, remove specified key and return the corresponding value.
print(help(dict.pop))
print(student.pop("companies")) # It will return its value.

# 7. popitem() - If you wants to remove the last key,value pair from the dictionary.
print(help(dict.popitem))
print(student.popitem())

# 8. keys() - listing the keys returns list.
print(student.keys()) # Type if dict_keys

# 9. values() - returns a list of values.
print(student.values())

# 10. items() - Returns a list of tuples having key and value.
print(student.items())

# 11. del is used for deleting an item from a dictionary
del student["name"]
print(student)

# 12. Iterating over a dictionary.
student = {
    "name": "aditya",
    "age": 21,
    "skill": "python"
}

for key, value in student.items():
    print(key, value)