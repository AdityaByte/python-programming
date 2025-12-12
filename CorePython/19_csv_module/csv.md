# CSV Module
> CSV stands for comma separated value, python standard library provides a builtin module for working with the csv file, like parsing, writing and reading the csv files.

This is how we can import the csv module in python.
```python
import csv
# It has a couple of method by which we can do our tasks.
```

## Methods of the csv module.

### 1. Reading from a CSV file.
> So for this task the csv module provides a `csv.reader()` method by which we can read the csv file content. Although we can pass a delimeter
to it, however the default delimiter is the "comma" for that.

```python
import csv 

with open("file.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    # So the csv reader contains a list so that we have
    # to iterate over it.
    for line in csv_reader:
        print(line)
```

In the above code we have seen how to read through the csv file
via the `csv.reader(csv_file_obj)` using that.

Now there is a problem with the above code like in the csv file
the first line is the column name if we have to skip that.
There were two ways by which we can skip the first line.
- By using the generator - But we haven't studied that right now.
- Using the builtins `next(csv_reader_obj)` function.

```python
# So the code will look like this if we have to skip the first line.
import csv

with open("names.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file) # Creating obj for the csv reader.
    next(csv_reader)  # It moves the pointer to the next line.
    for line in csv_reader:
        print(line)
```

### 2. Writing to a CSV File.
> For Writing to a csv file we gonna use the csv writer for that.
Just look at these methods the first is the `csv.writer(file_obj, delimiter=""` which gives the `csv_writer` 
object 

```python
import csv

# TASK: we have to read from the OLD csv file and we have to replace the 
# delimiter to - and write to the another csv file.

# Creating context manager and reading the csv file.
with open("names.csv", "r") as read_file:
    csv_reader = csv.reader(read_file)
    with open("names_copy.csv", "w") as write_file:
        csv_writer = csv.writer(write_file, delimiter="-")

        for line in csv_reader:
            csv_writer.writerow(line)
```

Note: Reading a CSV file with a wrong delimiter.
Like we have added a csv file with a tab delimiter.
```python
import csv

with open("names_copy.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter="\t")
    for line in csv_reader:
        print(line) 

# Output:
# we gets a single element per-line so.
# So for this situation we have to explicitly pass the delimiter.
```

### 3. DictReader.
> csv.reader() gives the list of values but the dictreader as the name suggests it gives 
a dictionary so it could be flexible for data manupulation and fetching data easily.

```python
import csv
with open('file.csv', 'r') as f:
    reader = csv.DictReader(f, delimiter=',')
    for line in reader:
        print(line)
        print(line['email'])
```

### 4. DictWriter.
> Although checkout the dict_writer.py file for better understanding here
I can just tell you like how we can change the column name using the dictwriter.

```python
import csv

def main():
    with open("names.csv", "r") as rf:
        reader = csv.DictReader(rf, delimiter=",")
        with open("names_copy.csv", "w") as wf:
            # Since here we can change the column name like this.
            new_headers = ["FirstName", "LastName", "Email"]
            # Original there were first_name, last_name and email
            # But now i want the new headers.
            writer = csv.DictWriter(wf, delimiter="&", fieldnames=new_headers)
            writer.writeheader()
    
            # But in the reader dict we have to form a new row 
            # with the new headers (column name) and insert that new row because 
            # we are dealing with dictionary in list it could be easier because there were no key exists.
            for row in reader:
                new_row = {
                    'FirstName': row['first_name'],
                    'LastName': row['last_name'],
                    'Email': row['email']
                }
                writer.writerow(new_row)

if __name__ == "__main__":
    main()
```

If you read all this during revision or something great you have great patience and consistency.