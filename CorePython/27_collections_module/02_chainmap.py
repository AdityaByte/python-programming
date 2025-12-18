"""
ChainMap:
ChainMap is a class inside the collections module.
This class is mainly used for chaining dictionary like objects.

NOTE: Although ChainMap doesn't have any strict type checking that what we have passed here.
Since passing datatype different than dict is just a misuse and it may produces some sideeffects.

USE CASE:
ChainMap is mainly used for priority based lookups.
means we are looking up to the data based on their priority.

Example cases:
1. ChainMap is used in python interpreter for scoping - local, global, builtins.
"""



from collections import ChainMap


# Scope example :-
local_scope_var = {'name': "aditya"}
global_scope_var = {'name': "yeshank"}

# Priority - LocalScope -> GlobalScope
scope = ChainMap(local_scope_var, global_scope_var)
print(scope)

# Now If I wanna to access the name so as per the python it firstly searches in the local scope then
# in the global scope.
print(scope["name"])
print(scope.get("name")) # Returns = aditya.


# Methods in ChainMap:
# print(help(ChainMap))

# 1. items(): It returns a set like object with items.
print(scope.items()) # Returns - ItemView.
print("Items method result:", list(scope.items()))
# Note: As per when the items method calls it search for the keys so in the next dict it finds the same key
# so that it just prints out the first key.

# 2. keys(): Returns all keys.
print(scope.keys())
print("keys method result:", list(scope.keys()))

# 3. values(): Returns all values.
print(scope.values())
print("values method result:", list(scope.values()))

print(dir(ChainMap))

# 4. new_child() put a new child to the chainmap.
scope = scope.new_child({'name': 'abhi'})
print(scope)
print(scope.get("name"))

# 5. clear() method which clears the first mapping of the ChainMap.
scope.clear()
print(scope)

print(help(ChainMap.clear))

# You can check out other method too.