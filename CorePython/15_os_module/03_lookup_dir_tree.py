# This file demonstrates lookup to a directory tree structure.

"""
os.walk():
 -> os.walk(path) function is a generator function which yields up a tuple of three values.
    1. Directory path
    2. Directories within that path
    3. Files within that path
 -> By default the os.walk(path) takes the current working directory as argument but you
 can explicit define that too.
"""

import os

path = os.path.join(os.getcwd(), "CorePython")

for dir_path, dir_names, file_names in os.walk(path):
    print(f"Current Path: {dir_path}\nDirectories: {dir_names}\nFiles: {file_names}\n")