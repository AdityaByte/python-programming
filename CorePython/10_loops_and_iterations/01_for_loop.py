# For Loop:
# When we know the termination condition of the loop.
# Or when we have to perform an iterative task over a definite time then we use for loop.

# Let we have a list of number and we have to loop through it.
nums = [1,2,3,4,5,6,7,8,9]
for num in nums:
    print(num)

# If we want to iterate over a range of numbers.
for i in range(10): # ByDefault it starts through 0 and go through 9
    print(i)

# print(help(range))

# If we go deep in the range function it gives a list of values based on the condition.
# range(start, stop, step)
for i in range(2, 12, 2): # Assume it as first one is the initialization case, condition from where the loop runs and third is the updating the iterator variable.
    print(f"i: {i}")

for index, value in enumerate(nums, 1):
    print(f"index: {index} value: {value}")