# Regex: Regular expression
> A regular expression (often abbreviated as regex) is a sequence of characters that defines a search pattern. These patterns are used to match, search, edit, or manipulate text data. Think of regex as a powerful tool for quickly parsing through large quantities of text to find, validate, or extract information following certain rules or formats.

## Key uses of regex:

- **Searching Data**: Regex enables you to find information that matches a specific pattern within a dataset efficiently. Example use cases include searching for keywords, emails, phone numbers, or IDs in text or files.

- **Extracting Data**: You can pull out particular pieces of data that match a pattern, such as extracting all dates from a document or parsing structured data within logs or configuration files.

- **Validating Data**: Regex is widely used to verify if data conforms to a required format, such as checking if an email address, phone number, or postal code is valid.

## How Regex Works

> Regex patterns use a combination of literal characters (like letters and numbers) and special characters (called metacharacters) to define the rules for matching:


- .       - Any Character Except New Line
- \d      - Digit (0-9)
- \D      - Not a Digit (0-9)
- \w      - Word Character (a-z, A-Z, 0-9, _)
- \W      - Not a Word Character
- \s      - Whitespace (space, tab, newline)
- \S      - Not Whitespace (space, tab, newline)

> Some which are used for other aspects.

- \b      - Word Boundary
- \B      - Not a Word Boundary
- ^       - Beginning of a String
- $       - End of a String

> Useful one:

- []      - Matches Characters in brackets
- [^ ]    - Matches Characters NOT in brackets
- |       - Either Or
- ( )     - Group

> Quantifiers:

Note: Ignore the double quotes it is just for md formatting.
- "*"      - 0 or More
- "+"      - 1 or More
- "?"      - 0 or One
- {3}     - Exact Number
- {3,4}   - Range of Numbers (Minimum, Maximum)


#### Sample Regex for email: ####

[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+