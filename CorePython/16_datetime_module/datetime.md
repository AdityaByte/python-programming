# Datetime Module
> Datetime module is the main module if you have to work with date.
```python
import datetime
```

In the python Datetime module there are two types of date -

1. **Naive** datetime - A datetime object that does not contain any timezone information.
2. **Aware** datetime - A datetime object that does contain timezone information.

## Naive time
> A datetime object with no timezone information.

### datetime.date module:

* Creating a Date, there are couple of way by which you can create a date in python but there is a simplest way is by using the date class inside the datetime module.
```python
import datetime
# my_date = datetime.date(year, month, day)
# date is a class and we are passing the values to the constructor.
my_date = datetime.date(2025, 9, 11)
```
Note: Pass the argument dates as regular integer with no leading zeros otherwise it will treat it as invalid date (octal hope you know).

* If you wants to prints the today's / current date.
```python
# I'm not importing the module just writing the main code.
today = datetime.date.today()

# Now If we need to print out which weekday is we can print out the weekday by 2 ways.
# 1. By weekday() function.
# In weekday(): Monday - 0 and Sunday - 6

# 2. By isoweekday() function.
# In isoweekday(): Monday - 1 and Sunday - 7

print(today.weekday())
print(today.isoweekday())

```

* TimeDeltas - Timedeltas could be useful in the case when you have to work in date interval.
Like you know the todays date and have to find out the day and the date which lies after 50 days then in that case timedeltas would be useful.

```python
#This is how we can create a timedelta
import datetime
td = datetime.timedelta(days=7)
today = datetime.date.today()
print(f"Date after 7 days: {today+td}")
```

### datetime.time module
> If you're dealing with time like earlier we are only dealing with dates to this time module we can also deal with time.

* Creating a date with time.
```python
import datetime

# my_time = datetime.time(hours, minutes, seconds, microseconds)
my_time = datetime.time(0, 10, 0, 0) # Created time of 10 minutes.
my_new_time = datetime.time(9, 44, 45, 8374) # Note: Microseconds must be in this range -  0..999999
print(my_new_time)

# Since we are creating the time using the constructor of the time class.
# So this class has some attributes you can find them using the help(datetime.time) | dir(datetime.time) functions of builtins.

# so the attributes are hour, minute, second, microsecond.
print(my_new_time.hour, my_new_time.second, my_new_time.minute, my_new_time.microsecond, sep="\n")
```

Note: Since this module has many things to learn you can from the official documentation otherwise the things that i have written here are sufficient.

### datetime.datetime module
> If you have to work with both date and time, there is a datetime module.

Example:
```python
from datetime import datetime

def main():
    # If you wants to create a date then this is how you can create a date using the datetime module.

    # my_date = datetime(year, month, day, hour, minute, second, microsecond)
    # Although you can use the keyword arguments too.
    my_date = datetime(2016, 4, 12, 12, 9, 34)

    print(my_date)

    # Since it has all the attributes that the time and date sub-module both have.
    print(f'''
        Date:\t{my_date.day}
        Day:\t{find_weekday(my_date.isoweekday())}
        Month:\t{my_date.month}
        Year:\t{my_date.year}
        Hour:\t{my_date.hour}
        Minute:\t{my_date.minute}
        Second:\t{my_date.second}
          ''')
    working_with_timedelta()

# Working with timedeltas in datetime.
# It works the same as the date timedelta.
def working_with_timedelta():
    d = datetime.today() # todays date.
    # We have to find the time after 10 hours
    td = timedelta(hours=10)
    new_date = d + td
    print(new_date, new_date.hour, sep="\n")

# find_weekday(index) return the weekday.
def find_weekday(weekday_index):
    assert 1 <= weekday_index <= 7
    weekday_list = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
    return weekday_list[weekday_index - 1]

if __name__ == "__main__":
    main()
```

## Aware Time
> A datetime object with timezone information.

* Creating aware time using the datetime module.
```python
import datetime
aware_time = datetime.datetime.now(tz="you have to pass the timezone info")
print(aware_time)

# You need to install a python module for working with timezones
# although you can use the builtin timezone module too but the preferred way is by using the pytz module.
```
Install the `pytz` module using this command:
```python
pip install pytz
```

Before working with the UTC date we have to know about what is the UTC

### UTC
> Coordinated Universal Time

- In simple words, it is a universal time standard that does not depend on local time zones.
- Makes time comparison easy and consistent across systems.

---

Creating UTC time -

```python
# Using now function of the datetime.datetime module.
from datetime import datetime as dt
import pytz

# Way 1 -
my_utc_time = dt.now(tz=pytz.UTC)

# Way 2 -
my_utc_time2 = dt.utcnow().replace(tzinfo=pytz.UTC)

# Way 3 -
my_utc_time3 = dt(2016, 4, 23, tzinfo=pytz.UTC)
```

Datetime timezone specific -
```python
from datetime import datetime as dt
import pytz

# For india.
dt_india = dt.now(tz=pytz.timezone("Asia/Kolkata"))
print(dt_india)

# Converting UTC timezone datetime to another timezone.
dt_utc = dt.now(tz=pytz.UTC)
dt_usa = dt_utc.astimezone(pytz.timezone("US/Mountain"))
```

Converting Naive datetime to aware datetime
```python
# Skipping the import datetime.
# using the localize method
naive_dt = dt.now()
mtn_time = pytz.timezone("US/Mountain")
aware_dt = mtn_time.localize(naive_dt)
print(aware_dt)
```

Some important conversions.
1. Datetime to String
```python
from datetime import datetime as dt
import pytz

# Suppose we have a indian UTC timezone.
dt_india = dt.now(tz=pytz.timezone("Asia/Kolkata"))
my_friendly_format = dt_india.strftime("%d %B %Y")
print(my_friendly_format)
```

2. String to Datetime
```python
# Sometimes we get the datetime in string format so performing action on hard so better
# to convert them to datetime object.
from datetime import datetime as dt

dt_str = "20 July 2023"
dt_obj = dt.strptime(dt_str, "%d %B %Y")
print(dt_obj)
```