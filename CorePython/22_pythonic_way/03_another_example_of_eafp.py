# Another example of accessing a file.
import os

# Suppose you are accessing a file and fetching the content so.

# Non pythonic-way of doing that: Firstly asking for permission then accessing it.
if os.access("test.txt", os.R_OK):
    with open("test.txt", "r") as file:
        print(file.read())
else:
    print("We cannot access the file content")

# Pythonic way of doing that: Accessing the file if something went wrong we can catch the error.
try:
    file = open("test.txt")
except FileNotFoundError as e:
    print("File doesn't exist")
else:
    print(file.read())
    file.close()