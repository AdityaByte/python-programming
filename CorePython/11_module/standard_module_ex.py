# Why to use standard libraries when you can make your own?
'''
The answer often varies from person to person aspects:
Pros:
- If you're a senior engineer then doing things from scratch takes time and othen you have to
test it on different aspects so that it can withstand different scenories.
- So despite of giving your time there you can use the pre-built functionalities that are offered
by the standard libraries and often they are standards tested.
Cons:
- If you're a learner then it's always been adviced that not for all things but you have to know some
thing by your own otherwise you will become dependent to some tools.
'''

# These modules are python files themselves which are written by someone else.

# Random module in python
# This random module is just a part of the standard library.
import random

my_list = [1,2,3,4,5,6,7,8,9]
print(random.choice(my_list))

# Here we have more standard libraries like -
import math # If you wants to do complex mathematical operations.

print(math.sin(math.radians(90)))

# Datetime module
import datetime
# Calender module
import calendar

print(datetime.date.today())

print(calendar.isleap(2026))

# OS Module: This will give us the underlying operating system functions.
import os
print(os.getcwd())
print(os.__file__) # This will give the location of the os module.

import antigravity