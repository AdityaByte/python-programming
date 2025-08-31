# If we have two list and we just want to zip out the values like same index values would be together.
# print(help(zip)) # Zip is a class.

a = [1,2,3,4]
b = ['a', 'b', 'c', 'd']
print(list(zip(a, b)))

# When the length of both the lists are not equal.
# Then the index which doesn't exists in one of them is not in the list.
a = [1,2,3,4,5]
print(tuple(zip(a, b))) # output: ((1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'))

# If we have a list of characters (string) and a range.
print(list(zip('abcd', range(4))))

# Note: The str class in python doesn't inherit the iterable but it do implement the iterable protocol(rules)
# simply understand it as the sequence of characters.