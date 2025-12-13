import re

emails = '''
CoreyMSchafer@gmail.com
corey-schafer@university.edu
corey-321-schafer@my-work.net
aditya@gmail.com
'''

pattern = re.compile(r"[Cc][a-z]{4}-?[a-zA-Z0-9-]+@\w+.\w{3}") # Explicitly for emails starting with C or c.
# Another more general pattern.
pattern1 = re.compile(r"[a-zA-Z0-9-.+_]+@[a-zA-Z-]+\.(com|edu|net)") # This is in general for each email.

matches = pattern1.finditer(emails)

for match in matches:
    print(match)