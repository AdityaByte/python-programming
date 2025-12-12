"""
CSV: CSV stands for comma separated value.
CSV used comma as a delimiter for separating the values.
"""

import csv

def main():
    with open("names.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)

        # Right now when we print out the lines it also prints the first line which is the
        # naming column if we have to skip that line we can use the generator.
        # Although we haven't studied them right now.
        # So, we can use the next() builtins function for skipping over the first line.

        next(csv_reader)

        for line in csv_reader:
            # The each line that we're printing out is the list of values that each line
            # contains separated by comma.
            print(f"My name is {line[0]} {line[1]} and my email is {line[2]}")


if __name__ == "__main__":
    main()