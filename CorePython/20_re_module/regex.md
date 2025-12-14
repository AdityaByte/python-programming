# Regular expressions.
> Regular expressions are mainly used for pattern matching.
> Despite of the python specific format you can visit the regex folder ../regex. For in general 
> understanding of the metacharacters and literals that were used in pattern matching.

## re module in python.

### 1. Importing the re module.
```python
import re
```

### 2. `re.compile(pattern)` method in re module.
> This method is mainly used for creating a pattern in regex.
```python
import re

# multi-line string.
test_text = '''
Hello world
aditya@gmail.com
something.url
what are you doing
'''

# Throughout the upper texts if we have to search 
# aditya@gmail.com in this text we can use the.
# compile method for creating a pattern and 
# via the pattern object we can call the substitute method,
# finditer for finding any iteration in the text whom which we have to search.

pattern = re.compile(r"[a-z]+@{1}[a-z]+[.][a-z]+", flags=re.IGNORECASE) # Passing raw string to it so that python won't conclude anything for escape sequence characters.

# Now we can conclude the matches.
matches = pattern.finditer(test_text)

for match in matches:
    print(match) # Match gives us an object which contains a span function
    # which returns a tuple of indices in which the required string is caught.

# You can run this code freely and this would work.
```

#### check it out the other methods like 
Check it out the CLI documentation for these method use the `help()` function.

- `pattern.match()` > Only matches out the pattern if it occurs at the begining of the string otherwise it returns None.

- `pattern.search()` > It returns the first occurance through the whole string. 

- `pattern.findAll()` > Returns a list of string with the matches.
There is something interesting with the `re.findall() or the pattern.findall()` method 
This method has a design pattern, when we pass a pattern to it with containing no capturing groups.

1. **No groups**: returns a list of strings with all the matches with the given pattern.

2. **One group**: If the pattern has exactly one group, findall() returns a list containing only the content of that single group, ignoring the rest of the match.

3. **Multiple Groups**: If the pattern has multiple groups, findall() returns a list of tuples, where each tuple contains the content of all the groups in order for that match.

- `re.sub()` > This function is used for substitution returns a new result.
```python
# Example:
import re

my_str = "Good morning aditya"

def sub_function():
    pattern = re.compile(r"morning")
    # re.sub(pattern, repl, string, count=0, flags=0)
    new_string = re.sub(pattern, "Night", my_str)
    print(new_string)
```

- `re.split()` > This function is used for splitting the string on the basis of some pattern.
```python
import re

my_str = "hello my name is aditya pawar my work is something and i my do something what you do."

def split_function():
    # print(help(re.split))
    pattern = re.compile(r"m.")
    sub_strings = re.split(pattern, my_str)
    for sub_string in sub_strings:
        print(sub_string)
```

- `re.fullmatch() | pattern.fullmatch()` > This is used for fully matching the string.
```python
import re

search_text = input("Enter password: ")

def fullmatch_function():
    pattern = re.compile(r".{6}", flags=re.IGNORECASE)
    matches = pattern.fullmatch(search_text)
    print("Valid" if matches is not None else "Invalid")
```

#### Note: Something you might figure out after learning all these things:
> We can call the same methods by via the re module reference or with the 
> help of the pattern object.
> So just need to add up a point that these methods are functionally identical and you can prefer your own way of calling these methods.
