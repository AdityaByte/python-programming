"""In this file we are making random data from a list of value and putting that data to a file ok."""

import random

first_names = ['aditya', 'abhi', 'lakshya', 'sourabh', 'arjun', 'john']
last_names = ['pawar', 'rajput', 'singh', 'mangulkar', 'negi']
landmarks = ['Near NES', 'Near Baggudhana', 'Near ST street']
cities = ['washington', 'norway', 'los angles']

# Now the task is you have to create a file and first of all have to put the data with
# comma seperated in such a format - name, address, phonenumber.

with open("result.txt", "w") as f:
    for i in range(10):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        name = f"{first_name.title()} {last_name.title()}"
        landmark = random.choice(landmarks)
        city = random.choice(cities)
        address = f"{landmark} {city}"
        phone_number = f"+91-{random.randint(6, 9)}{round(random.random() * 1000000000)}"
        f.write(f"{name}, {address}, {phone_number}")
        if i != 9:
            f.write("\n")

print("File Operation has been done successfully")