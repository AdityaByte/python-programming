"""
Topic in this file -
a. context manager
b. reading from a file.
"""

# Rather than opening file and closing it maunually.
# We can prefer a context manager which automates all these tasks.
# So in python we can create a context manager with the with keyword.

with open("file.txt", "r") as f:
    ## Read whole content.
    # f_contents = f.read()
    # print(f_contents)

    ## Read all lines returns a list.
    # f_contents = f.readlines()
    # print(f_contents)

    ## Read one line.
    # first_line = f.readline()
    # print(first_line, end="")

    ## Iterate over lines in a file.
    # for line in f:
    #     print(line, end="")

    ## Reading specified characters.
    # size_to_read = 10

    # f_contents = f.read(size_to_read)
    # while (len(f_contents) > 0):
    #     print(f_contents, end="*")
    #     f_contents = f.read(size_to_read)

    # with open("file.txt", "r") as f:
    #     content = f.read(10)
    #     print(content)
    #     print(f.tell()) # The pointer is at the 10th index.

    with open("file.txt", "r") as f:
        size_to_read = 10
        content = f.read(size_to_read)
        print(content)

        f.seek(0) # start over from index 0.

        content = f.read(size_to_read)
        print(content)

    print()

# Outside of the block the f variable is now closed.
# We can check it through the f.closed variable value.
# print(f.closed) # Returns true
# print(f.read()) # ValueError: I/O operation on closed file.