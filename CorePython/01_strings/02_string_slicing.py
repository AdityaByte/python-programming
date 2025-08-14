# String Slicing
# It is the way of extracting certain elements from a string.
# String is just an array of character so we can access the elements with the help of index.

message = "hello world"
print(message[0]) # First character
print(message[len(message) -1]) # len() method returns the length of the string.

# Slicing
# string[inclusive_index:exclusive_index]
print(message[0:6]) # 0 is inclusive and 6 is exclusive.
# upper one can also be simplified as,
print(message[:6])

print(message[6:-1]) # -1 for last index and its exclude the last index.
print(message[6:])

