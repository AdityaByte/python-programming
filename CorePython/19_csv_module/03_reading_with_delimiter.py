# Suppose we have a file with a delimiter apart from the default delimiter.
import csv

def main():
    with open("names_copy.csv", "r") as file:
        csv_reader = csv.reader(file, delimiter="\t")
        for line in csv_reader:
            print(line)

if __name__ == '__main__':
    main()