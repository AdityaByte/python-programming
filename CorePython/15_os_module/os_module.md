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

8. Renaming the file and the folder.