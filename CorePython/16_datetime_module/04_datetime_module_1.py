import datetime

# datetime.today() gives the datetime according to the system's timezone.
dt_today = datetime.datetime.today()

# datetime.now(): It is similar to the today() function but it gaves us an option by which we can pass the timezone.
# datetime.datetime.now(tz=None)
dt_now = datetime.datetime.now()

# datetime.utcnow() is deprecated now but its returns a naive datetime object with no timezone awareness.
# It gives the current date and time in UTC.
dt_utc_now = datetime.datetime.utcnow()

print(dt_today, dt_now, dt_utc_now, sep="\n")

# That's why we use pytz module for learning the aware timezones.