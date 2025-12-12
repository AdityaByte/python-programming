"""
In the previous files we do learn about how to read and write via the normal csv writer and reader.
Now a question will arise in our mind that why we need DictReader and DictReader when we have the normal ones.
So everything which is came after a particular solution is just an enhancement to the original solution.
So these things also add up some things which are being useful off in some context.

In this file we are just learning about the features of the DictReader.
-> As of the normal reader() reads the file and gives us a list of values based on delimiter.
But via the DictReader, it gives a dictionary so we can access the data despite of the index we can easily
access the data through the key so it could be more flexible and readable.

Check out the below example.
- Here we a csv file names.csv so if i want to access the first name and email of the person so this is how
we can easily access them.

NOTE: It automatically skips out the header text by default by the dict_reader.
"""

import csv

def main():
    with open("names.csv", "r") as file:
        dict_reader = csv.DictReader(file, delimiter=",")
        for line in dict_reader:
            # print(line) # Prints out each line in a key-value format.
            # print(line["email"]) # This is how we can access the email of the person.
            print(line["first_name"])

if __name__ == '__main__':
    main()