# OS Module file operations.

"""
Opeartions that we do to this file:
1. Creating a file.
2. Writing data to it.
3. Renaming the file.
4. Removing the file.
5. Stating the file properties.
"""

import os
import time
from datetime import datetime

# Hardcoding the path.
os.chdir(f"{os.getcwd()}\\CorePython\\15_os_module")
print(os.getcwd())

# Firstly we are creating the file.
filename = "test.txt"

if not os.path.exists(filename):
    file = open(filename, "w+")
    file.write("Hello world")
    print("File created successfully")
else:
    print(f"File name: {filename} already exists")

# Then we have to rename the file.
try:
    global new_filename
    new_filename = "something.txt"
    os.rename(filename, new_filename)
    time.sleep(2)
    print("File renamed successfully")
except FileNotFoundError:
    print(f"Filename {filename} does not exist")
except PermissionError:
    os.remove(filename)
    print("No permission to rename the file maybe file opened somewhere")
else:
    # If everything goes correctly now we are finding the information of the file.
    stats = os.stat(new_filename)
    print(stats)
    # Result : os.stat_result(st_mode=33206, st_ino=3096224743953642, st_dev=3523246468, st_nlink=1, st_uid=0, st_gid=0, st_size=11, st_atime=1756791494, st_mtime=1756791494, st_ctime=1756791493)
    """
    1. st_mode: file type + permission, encoded as a number.
        # Wants to print the st_mode in a human readable format
        # DO:
            import stat
            print(stat.filemode(stat.st_mode))

    2. st_ino: unique id of a file on a disk.

    3. st_dev: device identifier which device the file is on.

    4. st_nlink: No of hard links pointing to the file.

    5. st_uid: User ID of the file owner (Unix systems, on Windows often 0).

    6. st_gid: Group ID of the file owner (Unix systems, on Windows often 0).

    7. st_size: File size in bytes (here, 11 means the file has 11 characters).

    8. st_atime: Last access time (in seconds since epoch).

    9. st_mtime: last modification time (when content last changed).

    10. st_ctime: on Linux = last metadata change, on Windows = creation time.
    """

    mode = os.stat(new_filename).st_mode # This is how we can access the attributes of the os.stat dictionary.
    print(mode)
    # For further knowing of how to convert the mode to human readable format this can be done by the stat module.

    # If we have to check the last modification time of the file we can do this
    mod_time = os.stat(new_filename).st_mtime

    last_mod_time = datetime.fromtimestamp(mod_time)
    print(last_mod_time)