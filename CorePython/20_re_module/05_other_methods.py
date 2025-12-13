""" In the previous files we are only working with the finditer and compile method
discussing more methods of the re module."""

import re


text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = "End of beginning"

# 1. pattern.findall method: It returns a list of string with all the matches.
# Note: But the finditer() method has more functionality than this.
pattern = re.compile(r"\d{3}.\d{3}.\d{4}")

matches = pattern.findall(text_to_search)

for match in matches:
    print(match)


# 2. pattern.match(): It returns the first match, Only if the match is the start of the string.
pattern1 = re.compile(r"Beginning") # Returns None because Beginning is not at beginning.
matches1 = pattern1.match(sentence)

print(matches1) # It returns a match object having the span (index) and the match field.
# Note: If the match won't found then it simply returns None.

# 3. pattern.search(): It returns the first search.
pattern2 = re.compile(r"Mr")
matches2 = pattern2.search(text_to_search)
print(matches2)
# Note: NONE if nothing finds.

# 4. Creating pattern object along with flags.
# suppose in the sentence variable we have to search start despite of the case in which it has like
# in titlecase, uppercase or in the lowercase.
# So we can use the flags keyword in this.

pattern3 = re.compile("end", re.IGNORECASE) # re.I and re.IGNORECASE both for ignorecase.
matches3 = pattern3.search(sentence)
print(matches3)