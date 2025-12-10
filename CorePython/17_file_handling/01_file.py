# File
# Opening a file without a context manager.

# open() is a builtins function which takes two things.
# open("file_name", "mode")
f = open("test.txt", "r")

content = f.read()
print(content)

f.close() # crucial to close the resource.
