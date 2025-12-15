"""
NOTE: More specific as you gain more experience with python programming you will know certain
specific exceptions that the code might throw.

Now,
Since error handling is crucial for surviving from failing over code abruptly.
So in python like in other language try except block is used for handling the errors.

In this file we gotta learn about try, except, else and finally block.
In python the else block is different we will learn more about these blocks.

Example: we are opening a file that doesn't exists that throws a FileNotFoundError so we are catching
and seeing what happened.
"""

try:
    print("Opening a file")
    file = open("file.txt")
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print("Writing to the file")
    file.write("Hello world")
    file.close()
finally:
    print("Finally block")

"""
So as in the above close you have seen something like different blocks.
So defining when to use which block and why.

1. Try Block: If you're writing some error and you think of that this code might throw some errors
as runtime then you can put that code to a try except block.

2. Except Block: This block is run when any exception might came up which we are catching. Note: More specific 
exceptions are at the top and more general exceptions are at the bottom. (Thinking of you know these things).

3. Else Block: This block is not similar to the conditional if,else block this block is mainly useful for doing
tasks when you think that the try block didn't raise any exception.

4. Finally Block: This block is mainly used for freeing resources such as closing db connection that's all.
"""