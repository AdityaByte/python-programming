'''
Current context: Creating a function which produces a square of the values that we have passed to it.
'''

def square_numbers(nums):
    result = []
    for num in nums:
        result.append(num**2)
    return result

my_nums = square_numbers([1,2,3,4,5])
print(my_nums)

'''
Generator: Generator function is a special type of function that returns an iterator 
object, producing a sequence of value one at a time on demand rather than storing them all in memory at once.

- Generator functions follows lazy loading principle.
- Generators don't hold the entire result in the memory it yield one result at a time.
- Another alternative phrase for `generating values on demand` is the `it generator values on the fly`
HINDI : Jab zarurat pdengi values ki tab generate krenga otherwise nhi krenga.

Advantages of using generator function:
- Better code readability.
- Performance optimization.
- Memory optimization.
'''

# Now the thing is that how can we create a generator function.
def square_numbers_gen_edition(nums: list):
    for num in nums:
        yield num**2

"""
Before explaining you further, A question may arise to you mind.

What is the meaning of yield keyword?
Proper definition: In programming, the yield keyword is used to pause the execution of a function 
and return a value to the caller while preserving the function's state for later resumption.

After reading the definition you can assume the meaning but for better understanding I can simply that -
-> For example, In the particular context we are generating a list of square values ok, so yield just stops the 
execution of the function and returns a generator function state which takes care of the state of the function and 
also the task that it was doing it.
-> So for the next time when we ask the reference to do something it will returns out the value and update the state.
-> This behavior of the function makes it better optimized.
"""

"""
Generator function:
-> range() is a generator function, which generator the value on the fly rather than storing all the values in memory.
-> We can use for loop directly to the generator function.
"""

# Calling the generator function
gen = square_numbers_gen_edition([1,2,3,4])
print(gen) # Prints out the reference of the generator object.
# For accessing the values we have to call the next method of builtins.
print(next(gen)) # 1
print(next(gen)) # 4
for num in gen:
    print(num)

"""
Output:
1
4
9
16
Since the thing you observed like we have accessed the 1 and 4 earlier by the next() method.
So when i applied the for loop the generator function didn't reset out the old state it maintains the 
old state and thus generates out the new values.

NOTE: If you are still trying to access the values out of the context or index by generator object using
the next() method.
Then it throws out the - StopIteration exception, (Means generator has been exhausted stop the iteration).
"""