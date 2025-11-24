# Through the time module since we are only working with dates in the datetime.date module in the time module we are going to work with hours minutes and seconds.
# This was still a naive datetime cause it didn't have the timezone information.

import datetime

# Creating a new local time.
# my_time = datetime.time(hours, minutes, seconds, microseconds)
my_time = datetime.time(9, 30, 45, 928392)
print(my_time)

# Since it has some attributes which are -
print(
    my_time.hour,
    my_time.minute,
    my_time.second,
    my_time.microsecond,
    sep="\n"
)

# If you only need to deal with the time time module is useful otherwise if
# you have to deal with both date and time there is the datetime module. 