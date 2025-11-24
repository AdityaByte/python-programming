from datetime import datetime, timedelta

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

