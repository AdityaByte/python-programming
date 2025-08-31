# Generator Expressions

# Note: range() is also a generator function as per in python3.
# Generator Expressions : Think of it like we generating things on the fly when we need it.
""" For example we have to loop through millions of values so there could be two case occurs in the list.

Case 1: If we have a list of million values and we have to loop through it until and unless we find that desired case.
    -> In that case the whole list would be loaded to the memory at once and afterwards we loop through it.

Case 2: If we have a generator function which is a special type of iterator and we have to loop through it since we
    gets the desired case.
    -> In that case the values are generated on the fly and gets allocated into the memory so if the case comes fast so
        less memory would be acquired and hence space complexity is reduced.
"""

# I want to yield n*n for each n in nums.

nums = [1,2,3,4,5,6,7,8,9]

# Iterative way:
def gen_func(nums):
    for n in nums:
        yield n*n

my_gen = gen_func(nums)

for i in my_gen:
    print(i)

# We can often reduced it via this expression
print("-------------------") # <class 'generator'>
my_gen = (n*n for n in nums)
print(type(my_gen))
for i in my_gen:
    print(i)