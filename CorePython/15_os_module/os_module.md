# OS Module
> OS Module allows us to interact with the underlying opearting system in several different ways.

**For example**: we can navigate to the file system, get file information, lookup and change, moves file around, change the environment variables etc.

* Since the OS module is in the core python so we can simply work with it by importing the OS module.
    ```bash
    import os
    ```

## Interacting with the os module: some useful methods

> Note: For more info about these functions do: `print(help(os.function_name()))`

1. Get the current working directory.
   `os.getcwd()`

2. If you have to change the directory.
    `os.chdir(path)`
Note: For your convenience give the path if you're working in windows with raw string in python.

3. Listing directories. `os.listdir(path=getcwd())`

4. Creating directory (Single Level): `os.mkdir(dir_name)`

5. Deleting directory (Single level): `os.rmdir(dir_name)`

6. Creating multiple directories (Directory inside some directory): `os.makedirs("usr/bin/Test1/Test2")`

7. Removing the multiple directories (Directory inside some directory): `os.removedirs("usr/bin/Test1/Test2")`

8. Renaming the file and the folder. `os.rename(original_file_name, new_file_name)`
    Note: If the file is open it do throw the **PermissionError** and if the file is no found it throws the **FileNotFoundError**.

9. Retriving the information about a file: `os.stat(file_path)`.
    It gives the following information about the file:

    - **st_mode**: file type + permission, encoded as a number.
    ```bash
        # Wants to print the st_mode in a human readable format
        # DO:
        import stat
        # We will discuss about this module too in depth.
        print(stat.filemode(stat.st_mode))

    ```

    - **st_ino**: unique id of a file on a disk.

    - **st_dev**: device identifier which device the file is on.

    - **st_nlink**: No of hard links pointing to the file.

    - **st_uid**: User ID of the file owner (Unix systems, on Windows often 0).

    - **st_gid**: Group ID of the file owner (Unix systems, on Windows often 0).

    - **st_size**: File size in bytes (here, 11 means the file has 11 characters).

    - **st_atime**: Last access time (in seconds since epoch).

    - **st_mtime**: last modification time (when content last changed).

    - **st_ctime**: on Linux = last metadata change, on Windows = creation time.

10. Printing out the directory tree: `os.walk(path_of_directory)`.
    - The `os.walk(path)` gives three values and we loop through it. It will gives the three values.

        - Directory Path.
        - Directories within that path.
        - Files within that path.

11. Dealing with the environment variables: `os.environ`

    - `os.environ` is a class which has some methods for dealing with the environment variables.

        - If we want to print out all the environment variables then you can you this.
        ```bash
        print(os.environ)
        ```

        - If we want to print out a specific environment variable.
        ```bash
        print(os.environ("JAVA_HOME")) # for example
        ```

        - If we want to traverse all the environment variables.
        ```bash
        for key in os.environ.keys():
            print(key, os.environ[key])
        ```


## Submodule of OS module: os.path module

>  `os.path` for dealing with the path variables.

1. If we have to join the paths like we want to create a path variables we can do this via this method
```bash
os.path.joins(...args) # Pass the args in place of args
```

2. Reterive the filename from a path.
```bash
os.path.basename(path)
```

3. Reterive the dirname from a path.
```bash
os.path.dirname(path)
```

4. Reterive the filename and the dirname both. -> returns a tuple.
```bash
os.path.split(path)
```

5. Check the path is valid or not -> returns boolean.
```bash
os.path.exists(path)
```

6. Check the path points to a directory or a file. -> returns boolean.
```bash
os.path.isfile(path)
os.path.isdir(path)
```

7. Split up the extension -> returns tuple.
```bash
os.path.splitext(path)
```