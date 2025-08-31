# Sorting List

li = [9,6,4,3,1,8,7,5,2]

# sorted() function: Doesn't alter the original list returns a new list.
s_li = sorted(li)
print("{}\t{}".format("Sorted List:", s_li))

print(f"Original List:\t{li}")

# sort() function: sort function is specific to list class and it alters the original list.
li.sort()
print("Altered original list:", li, sep="\t")

# If we have to reverse sort the list so.
# make `reverse=True`
r_s_li = sorted(li, reverse=True)
print(f"Reverse Sorted List:\t{r_s_li}")

# Altering the original list to reverse order.
li.sort(reverse=True)
print(f"Reverse Sorted altered original list:\t {li}")

# sorted() function is more flexible because it works on every iterable not only on list.
# Like we have a tuple and we have to sort it.
t = (1,3,5,2,9,0)
print(f"Sorted tuple:\t{sorted(t)}")

# sorted() function would work on complex scenerio in which we don't have to sort values in ascending or descending.
# key keyword argument.
# Example: Here we have a list of integers and we have to sort them based on their absolute value.
my_integers = [-5,-6,-4,3,1,2]
sorted_my_integers = sorted(my_integers, key=abs)
print(f"Sorted integers based on abs value:\t{sorted_my_integers}")

# Note: Understand 'key' as the function by which the each value would pass and after that they being sorted on the basis
# of that key.

