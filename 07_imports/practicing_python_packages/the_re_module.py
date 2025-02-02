import re

# Example: Searching for a pattern in a string
pattern = re.compile(r'\bword\b')
text = "This is a word in a sentence."
match = pattern.search(text)
if match:
    print("Found:", match.group())

# The `re` module functions:
# - `re.search(pattern, string)`: Searches for the first location where the regular expression pattern produces a match.
# - `re.match(pattern, string)`: Determines if the regular expression matches at the beginning of the string.
# - `re.findall(pattern, string)`: Finds all substrings where the regular expression pattern produces a match and returns them as a list.
# - `re.sub(pattern, repl, string)`: Replaces the matches with the replacement text.

# Example: Finding all occurrences of a pattern
pattern = re.compile(r'\b\w+\b')
text = "This is a word in a sentence."
matches = pattern.findall(text)
print("All words:", matches)

# Example: Replacing a pattern in a string
pattern = re.compile(r'\bword\b')
text = "This is a word in a sentence."
new_text = pattern.sub('replacement', text)
print("Replaced text:", new_text)

# Regular expressions use special characters to define patterns:
# - `.`: Matches any character except a newline.
# - `^`: Matches the start of the string.
# - `$`: Matches the end of the string.
# - `*`: Matches 0 or more repetitions of the preceding pattern.
# - `+`: Matches 1 or more repetitions of the preceding pattern.
# - `?`: Matches 0 or 1 repetition of the preceding pattern.
# - `{m,n}`: Matches from m to n repetitions of the preceding pattern.
# - `[]`: Matches any single character in the brackets.
# - `\`: Escapes special characters or signals a special sequence.

# Example: Using special characters in patterns
pattern = re.compile(r'\b\w{4}\b')
text = "This is a test of the re module."
matches = pattern.findall(text)
print("Four-letter words:", matches)

# The `re` module also supports groups and capturing:
# - `()`: Groups a pattern and captures the match.
# - `(?:)`: Groups a pattern without capturing the match.
# - `(?P<name>)`: Groups a pattern and captures the match with a name.

# Example: Using groups and capturing
pattern = re.compile(r'(\b\w+\b) (\b\w+\b)')
text = "This is a test."
match = pattern.search(text)
if match:
    print("Groups:", match.groups())
    print("First word:", match.group(1))
    print("Second word:", match.group(2))