# Tuple datatype:
'''
Key points:
1. Orderered collection of items.
2. Immutable we cannot change the tuple once it was created.
3. Items are indexed.
4. Tuples are created with paranthesis - ()
'''

new_tuple = ("hello", "world")
print(type(new_tuple)) # <class 'tuple'>

# Accessing tuple items.
print(new_tuple[-1])

# Looping through tuple.
for item in new_tuple:
    print(item)

# We cannot change the items in a tuple it is something similar to constants.
new_tuple[0] = "new" # this will raise error - tuple object does not support item assignment.
