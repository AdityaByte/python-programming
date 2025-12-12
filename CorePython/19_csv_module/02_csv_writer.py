import csv

# How to write to a csv file.
# Suppose we have to write to another csv file and replace the delimiter as dash(-).

def main():
    with open("names.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        with open("names_copy.csv", "w", newline="") as new_csv_file:
            csv_writer = csv.writer(new_csv_file, delimiter="\t")

            for line in csv_reader:
                csv_writer.writerow(line)

            print("Successfully copied the name.csv file")

if __name__ == '__main__':
    main()