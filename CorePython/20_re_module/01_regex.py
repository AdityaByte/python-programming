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

sentence = "Start a sentence and then bring it to an end"

# pattern = re.compile(r"[a-zA-Z]+\.[a-z]{3}")  # Backslash is used for escaping those characters.
# pattern = re.compile(r"\BHa")
pattern = re.compile(r"end$")

matches = pattern.finditer(sentence)

for match in matches:
    # print(text_to_search[match.span()[0]:match.span()[1]])
    print(match)
# print(help(re))