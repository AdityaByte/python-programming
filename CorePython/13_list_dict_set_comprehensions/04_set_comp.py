# Set comprehensions:

nums = [1,2,1,2,4,6,3,1,3,2]
my_set = set(nums)
print(my_set)

# Note: Set items are not indexable.

# Add items to a set.
my_set = set()
for n in nums:
    my_set.add(n)
print(my_set)

# We can do it like this too by set comprehensions.
my_set = {n for n in nums}
print(my_set)

# we can do it using map and lambda too.
my_set = set(map(lambda n: n, nums))
print(my_set)