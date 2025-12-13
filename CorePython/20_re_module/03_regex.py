"""
In this file we are learning about how to fetch data from a text of string through the help of regex.
# Group method - match.group(index).
"""

import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r"https?://(www\.)?(\w+)(\.\w+)")

matches = pattern.finditer(urls)

for match in matches:
    # print(match)

    # Now if we have to find the top level domain and the domain name we can
    # use the group method for finding them.
    # So in the pattern we do have created some groups by using the parentheses.

    # So the whole URL is the first group at index 0 and then other from left to right with increasing index.

    # print(match.group(0))
    # print(match.group(1))
    # print(match.group(2))
    print(match.group(3))
