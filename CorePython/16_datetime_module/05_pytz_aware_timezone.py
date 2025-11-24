import pytz
from datetime import datetime

"""
UTC - Coordinated Universal Time
It is the primary world time standard used for global keeping.
- It does not change with seasons.
- It is same everywhere in the world.

So why we need UTC time?
1. No confusion
2. Easy to store and compare.

Note: Suppose you have been creating a software which is used worldwide. So having one timezone for each and every country.
Reduces conflict in timezone so that's why we use UTC timezones.

"""

dt = datetime(2025, 11, 24, 6, 0, 30, tzinfo=pytz.UTC)
print(dt) # It gave us the datetime object in this format +00:00

# Creating a aware datetime using pytz.
dt_now = datetime.now(tz=pytz.UTC)
print(dt_now)

# Another way of creating the UTC datetime.
dt_utcnow = datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_utcnow)

# Converting the UTC timezone to my local timezone of india.
# Search pytz timezone list over internet for finding timezones.
dt_india = dt_utcnow.astimezone(pytz.timezone("Asia/Kolkata"))
print(dt_india)

# Traversing over the list of the timezones avaiable in pytz
# for tz in pytz.all_timezones:
#     print(tz)

# Converting naive datetime to aware datetime.
naive_dt = datetime.now()
mtn_tz = pytz.timezone("US/Mountain")
# For converting we have to call the localize function of the mtn_tz (in our case) and passing the local datetime object as argument.
aware_dt = mtn_tz.localize(naive_dt)
print(aware_dt)

# Converting the aware_datetime in ISO format.
dt_usa = datetime.now(tz=pytz.timezone("US/Eastern"))
print(dt_usa.isoformat())

# Converting datetime object to a specific format.
# Go over the internet and find the format code.
# Check this - https://strftime.org/
# The below code won't work on windows but on mac or linux.
# print(dt_usa.strftime("%d %B %Y %-I %-M %-S %p"))
# For windows use `hashtag` in place of `hyphen`
print(dt_usa.strftime("%d %B %Y %#I %#M %#S %p"))

# Note: You can check the format_codes.md file for format codes.

# If we have a string date and we have to perform some operations of datetime.
# Firstly we have to convert it to the datetime object.
dt_str = "March 26, 2025"
# It takes two argument first the string date and in which format the date is.
dt = datetime.strptime(dt_str, "%B %d, %Y")
print(dt)

# strftime - datetime to string
# strptime - string to datetime
