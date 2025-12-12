"""
DISCLAIMER: Please check out the dict_reader where I have been successfully explained why we are using the DictReader and DictWriter.
In this file we are learning about the dict_writer how can we write to a csv file using the dict_writer.
Example is below:
"""

import csv

def main():
    with open("names.csv", "r") as rf:
        dict_reader = csv.DictReader(rf, delimiter=',')
        # Now we are opening another file where i am writing the data.
        with open("names_another_copy.csv", "w", newline="") as wf:
            # We can specify the field names exists in the file through this.
            field_names = ["first_name", "last_name", "email"]
            dict_writer = csv.DictWriter(wf, fieldnames=field_names, delimiter=",")
            # Now we have to call a function for adding the header.
            dict_writer.writeheader()
            # Now we have to write the other content.
            for line in dict_reader:
                dict_writer.writerow(line)

            print("The dict writer is done its task")


def not_including_some_fields():
    # Suppose in the names.csv file if i don't wanna to include the email field then we use the del keyword for that.
    with open("names.csv", "r") as rf:
        reader = csv.DictReader(rf)

        with open("names_another_copy.csv", "w", newline="") as wf:
            field_names = ["first_name", "last_name"]
            # Passing only two fields and passing colon as delimiter.
            writer = csv.DictWriter(wf, fieldnames=field_names, delimiter=":")
            writer.writeheader()
            for line in reader:
                del line["email"]
                writer.writerow(line)

if __name__ == '__main__':
    # main()
    not_including_some_fields()