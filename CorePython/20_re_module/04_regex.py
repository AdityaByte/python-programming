# Substitution in re module like if we have to substitute the URL domain name so.

import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r"https?://(www\.)?(\w+)(\.\w+)")

# The backslash 2 and 3 are the group number whom we are willing to substitute.
subbed_urls = pattern.sub(r"\2\3", urls)

print(subbed_urls)