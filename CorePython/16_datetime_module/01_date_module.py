# Please lookup in the datetime doc (datetime.md) first.
# In this file we are dealing with date class inside the datetime module.

"""Naive Datetime:
In this file we are dealing with the naive datetime code snippets
by which you can understand the syntax, how to use datetime in your
required case so let's start."""

# Firstly we have to import the module.
import datetime

# Creating a date via using datetime module.
my_date = datetime.date(2016, 4, 30)
print(my_date)

# Getting the current today's date.
today = datetime.date.today()
print(today)

# If we want to grab a year month or day from a date object then we can fetch the attributes like this.
print(today.year)
print(today.month)
print(today.day)

# If we want to print out the weekday like which day of the week.
# By two methods we can fetch that out.
# 1. weekday()
# 2. isoweekday()
# For weekday monday - 0 and sunday - 6
# For isoweekday monday - 1 and sunday - 7

print(today.weekday())
print(today.isoweekday())

# Time deltas -
# Time deltas is the difference between two dates and two times.
tdelta = datetime.timedelta(days=7)
# Now we have to know which date will lie 7 days apart from today then.
print(today + tdelta)
# We can also subtract time deltas then date 7 days ago.
print(today - tdelta)

# Bro if we have a have two dates and if we subtract two dates then we will gets the timedelta.
bday = datetime.date(2026, 3, 26)
tday = datetime.date.today()
till_bday = bday - tday
print(till_bday)
# If you wants to print out total seconds till my bday.
print(till_bday.total_seconds())