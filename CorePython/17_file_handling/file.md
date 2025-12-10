# File Handling in Python

## Creating & Writing to a file object in python
> For creating a file object we use the builtins open() function which has two parameters filename and the open cmd whether you have to read, write or append.

Note: By default the `open()` function opens the file in the reading mode (`r`)

```python
file = open("name.txt", "w") # Then open() function gives the file object.
# File object has various method like write, read etc.
file.write("Hello world")
file.close() # we have to explicit close the file here.
```

> Despite of opening and closing resources manually we can use a context manager(resource manager) for that.

```python
# This is similar to try resource block in java.
# But in python we use the with keyword.
with open("file.txt", "w") as file:
    # Since the syntax is something like that we gets the object as file (name could be anything).
    file.write("Hello world")

    # Now we don't have to manually close the file the task would be done by the context manager.
```

## Reading content from the file.

> Creating a context manager and reading the content from the specified file.
```python
with open("file.txt", "r") as f:

    # If the file is small we can prefer this read() method for reading the file content.
    file_contents = f.read()
    print(file_contents)
```

> Although there were a couple of more method by which we can read the file content which are -

```python
with open("file.txt", "r") as f:
    # The readLines() function returns a list of line along with the newline character.
    f_contents = f.readlines()
    print(f_contents)
```

> If we have to read the first line of the file.
```python
with open("file.txt", "r") as f:
    first_line = f.readline()
    print(first_line)
```

> If we have to specify a particular amount of data for reading we can pass kwargs to the `read()` function.

```python
with open("file.txt", "r") as f:
    f_contents = f.read(10)
    print(f_contents) # Prints out the first 10 characters.

    # And the cursor will points to the 11 character if exists.
```

> Reading the current position of pointer.

```python
with open("file.txt", "r") as f:
    f_contents = f.read(10)
    print(f_contents)
    print(f.tell())
```

> If we want to change the pointer location we can use the seek() method for going backward or forward.

```python
with open("file.txt", "r") as f:
    size_to_read = 10
    content = f.read(size_to_read)
    print(content)

    f.seek(0) # start over from index 0.

    content = f.read(size_to_read)
    print(content)
```

Note: What happens when we are writing to a file that was opened in a read mode.

Answer: We gets an error `UnsupportedOperation: not writable`

## Writing to a file

> Before coding we need to know about the open() function in a writing mode.

a. If the file does exits in that particular location, it will override the file content.
b. If it doesn't exists then it will creates the file and write to it.
```python
with open("file.txt", "w") as f:
    f.write("Hello world")
```

> Writing binary coded files like image file.
```python
with open("norway.jpg", "rb") as rf:
    with open("norway_copy.jpg", "wb") as wf:
        for line in rf:
            wf.write(line)
```