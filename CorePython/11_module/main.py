# import my_module as mm
# from my_module import * # If we wants to import everything from the module.

import sys
sys.path.append(r"C:\Users\HP\OneDrive\Desktop\my_module")

from my_module import find_index as fi, test

courses = ['History', "Math", "Science"]

index = fi(courses, "Math")
print(index)

# Note: We didn't specify the location of the module then how do the python finds the module.
# Before importing the module to the file python checks for different file location.
# It checks the path inside a list called as sys.path

# Seeing the path of the list.
import sys
print(sys.path)
print(test)

# Like when we remove the module to the desktop folder we gets ModuleNotFoundError.
# So before we could import the module we could also add the directory path to the sys.path so that it can search the module there.
# Look above since this was not the best way of doing that although this would became system dependent.