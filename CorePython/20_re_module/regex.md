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

- `pattern.match()` > Only matches out the pattern if it occurs at the begining of the string otherwise it returns None.

- `pattern.search()` > It returns the first occurance through the whole string. 

- `pattern.findAll()` > Returns a list of string with the matches.