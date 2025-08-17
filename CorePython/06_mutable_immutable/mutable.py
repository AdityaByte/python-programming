# Mutability : Mutability means data structure allows the change within it.
# List is mutable in python so taking it as an example.
list1 = ["aditya", "pawar"]
list2 = list1
# these two are pointing to same list.
list2.pop()
print(list1)
print(list2)
# Only one element will be left out.