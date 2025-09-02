# OS module: It allows us to interact with the underlying operating system.

# OS Module is the part of the core python so we can use its methods simply by importing them.

import os
from time import sleep

# Printing out the methods and attributes inside the os module.
print(dir(os))

# 1. Get current working directory.
print(os.getcwd())

# 2. Navigating to another directory - os.chdir(path)
# print(help(os.chdir))
os.chdir(r"E:\program files")

print(os.getcwd())

# Note: For you're convenience give the path as raw string in python.

# 3. Listing the directories by default it list of the current working directory but you can explicitly tell the function.
print(os.listdir()) # It gives a list of directories.

print(os.listdir("{}\\{}".format(os.getcwd(), "Connect")))


# 4. Creating single directory - os.mkdir(dirname)
# mkdir only creates the single directory it doesn't create dir inside dir.
os.chdir(r"e:\PythonProgrammng\CorePython\15_os_module")

try:
    os.mkdir("test_dir")
except FileExistsError:
    pass # Don't do anyting.

sleep(3) # Waiting to see the directory is created or not.

# 5. Removing a single directory vice-versa function of mkdir is - rmdir(name/path)
os.rmdir("test_dir")

# 6. Creating multiple directories - os.makedirs(...dirnames)
# Makedirs are often useful in the case when we have to create the dir to a certain level deep.

try:
    os.makedirs("level_0_dir\level_1_dir")
except FileExistsError:
    pass

sleep(3)

# 7. Deleteing multiple directories - os.removedirs(dir_names)

os.removedirs("level_0_dir\level_1_dir")

# 8. Checking a file exists or not.
filename = "os_module.md" # This file exits in the current folder.
isFileExists = os.path.exists(filename)
assert isFileExists == True
# If the file don't exists it will return False and thus then we get the AssertionError.

# 9. Joining the paths: os.path.join(..str_args)
folder_name = "test"
file_name = "test.txt"
current_dir = os.getcwd()
new_path = os.path.join(current_dir, folder_name, file_name)
print(new_path)