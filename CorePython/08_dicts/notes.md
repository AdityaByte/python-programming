# Deep Copy, Shallow Copy and Simple Assignment

## Shallow Copy
- Shallow copy just copy the reference of an object.
- The reference still points to the same object.
```bash
# Like we have a dictionary and we need to shallow copy it.
dict1 = {name: "aditya", data: {"hello": "world"}}
# Shallow copying it.
shallow_copy = dict1.copy()
shallow_copy["data"]["hello"] = "no-world"
print(dict1) # The original dictionary will also be changed.
```

## Deep Copy
- Deep copy copies the actual value.
- The reference points to different object or value in memory.
```bash
# This is how we create a deep copy in python.
import copy
dict1 = {name: "aditya", data: {"hello": "world"}}
# Deep copying it.
deep_copy = copy.deepCopy(dict1)
deep_copy["data"]["hello"] = "no-world"
print(dict1) # The original dict doesn't changed.
```

## Simple Assignment
- When we do this ```a=10, b=a```
- Now if we talk about the objects in that case the both reference points to the same object.
```bash
# Think of it something like we have an obj1.
obj1 -> 101010 # memory address where the obj1 is stored.
obj2 = obj2
# Now obj2 also points to the same obj1 because it just copy the reference.

```