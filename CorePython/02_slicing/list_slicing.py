# Slicing: It is the way of extracting certain elements.

list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#       0  1  2  3  4  5  6  7  8  9  - postive indices
#     -10 -9 -8 -7 -6 -5 -4 -3 -2 -1  - negative indices


# list[start:end:step]
# start index is inclusive.
# end index is non-inclusive/exclusive.
# step - size of step bydefault 1

# Note: If everything goes correctly as expected then no error will raised out.
# If something happens unexpected then AssertionError is raised.

# first two elements
assert list[0:2] == [0,1]

# from index 4 to 7
assert list[4:8] == [4,5,6,7]

# last two elements
assert list[len(list)-2:] == [8,9] # another way - list[-2:]
assert list[-2:] == [8,9]

# To last 3rd index
assert list[:-2] == [0,1,2,3,4,5,6,7]

# from 3 index to last
assert list[3:] == [3,4,5,6,7,8,9]

# Now we will learn about step
# If the step if of 2
print(list[0::2])
print(list[1::3])
print(list[1:9:-1]) # Empty list
# Reverse a list
print(list[-1::-1]) # Reverse a list
print(list[::-1])
print(list[::-2]) # Reverse order with negative step count.