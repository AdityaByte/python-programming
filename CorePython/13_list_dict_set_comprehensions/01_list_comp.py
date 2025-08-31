# List comprehensions:

nums = range(1, 11)


# I want 'n' for each 'n' in nums

# Normal version:
# my_list = []
# for n in nums:
#     my_list.append(n)
# print(my_list)

# Another more readable and simple version of it.
# my_list = [n for n in nums] # Read it like that n is for each n in nums
# print(my_list)

# my_list.clear()

# I want 'n*n' for each 'n' in nums
# for n in nums:
#     my_list.append(n*n)
# print(my_list)

# More readable version
# my_list = [n*n for n in nums]
# print(my_list)

# my_list.clear()

# We can also do it via map and lambda
# my_list = map(lambda n: n*n, nums)
# print(list(my_list))

# I want 'n' for each 'n' in nums if 'n' is even
# Iterative version:
# my_list = []
# for n in nums:
#     if n%2 == 0:
#         my_list.append(n)

# print(my_list)

# Another version
# my_list = [n for n in nums if n%2 == 0]
# print(my_list)

# Another version by using filter and lambda
# my_list = list(filter(lambda n: n%2 == 0, nums))
# print(my_list)

# I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'
# my_list = []
# for letter in 'abcd':
#     for num in range(4):
#         my_list.append((letter, num))
# print(my_list)

# By using list comprehensions:
# my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
# print(my_list)

# Doing it via maps and lambda is complex like this-
# my_list = list(
#     map(lambda x: (x[0], x[1]),
#         [(letter, num) for letter in 'abcd' for num in range(4)])
# )
# print(my_list)