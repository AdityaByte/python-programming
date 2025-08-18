# Conditional Statement:
# Not going to tell you what is a conditional statement ok... you learnt 5 langs still doing that thing one more time.
# Python has if elif and else block and also switch statement but which was introduced in python 3.11 maybe.

language = "Java"

if language == "Python":
    print("Language is Python")
elif language == "Java":
    print("Language is Java")
else:
    print("Not found")

# Comparision Operators:
'''
1. == : equal to - compare the value.
2. >
3. <
4. >= : Greater than or equal to
5. <= : Smaller than or equal to
6. != : not equals
7. is : Object identity
'''

a = [1,2,3]
b = [1,2,3]
# The above list are equal in case of values but they both are different as they are stored in different memory blocks
print(id(a))
print(id(b))
print(a is b) # returns False
print(a == b) # returns True

c = b
print(id(c)) # Print the same id as of b
d = b.copy()
print(id(d)) # Different id
