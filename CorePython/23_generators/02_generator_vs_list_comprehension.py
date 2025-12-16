"""
In this file mainly look up at the syntax of creating a list via list comprehension
along with creating a generator.
"""

my_nums = [x*x for x in [1,2,3,4,5]]
for num in my_nums:
    print(num)

"""
Thinking of you have read the 01 file after you are there.
Since the above thing is same that we are doing in the square_numbers() functions.

Creating a generator function via generator comprehension.
-> Replace the square brackets [] with parenthesis ().
"""

my_nums_gen_edition = (x*x for x in [1,2,3,4,5])
print(my_nums_gen_edition) # Returns a generator object.
for num in my_nums_gen_edition:
    print(num)

# Note: If we convert the generator object to a list then we lose the advantages of generator.
print(list(my_nums_gen_edition)) # Empty we have consumed all the values.