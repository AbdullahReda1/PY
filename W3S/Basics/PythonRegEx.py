# ==========================================
# Python Regular Expressions (RegEx)
# ==========================================


# ------------------------------------------------
# Import RegEx Module
# ------------------------------------------------
import re


# ------------------------------------------------
# What is RegEx?
# RegEx is used for pattern matching and searching
# in strings
# ------------------------------------------------


# ------------------------------------------------
# Basic Functions in re Module
# ------------------------------------------------
text = "The rain in Spain"

# findall() → returns all matches as a list
print(re.findall("ai", text))

# search() → returns first match object
match = re.search("Spain", text)
print(match)

# split() → splits string at matches
print(re.split(" ", text))

# sub() → replaces matches with given string
print(re.sub("Spain", "Italy", text))


# ------------------------------------------------
# Match Object
# Contains info about the match
# ------------------------------------------------
match = re.search("Spain", text)

if match:
    print("Match span:", match.span())
    print("Match string:", match.group())
    print("Start index:", match.start())
    print("End index:", match.end())


# ------------------------------------------------
# Metacharacters
# Special characters with meaning in RegEx
# ------------------------------------------------

# []  → set of characters
print(re.findall("[a-m]", text))

# \   → special sequence or escape
print(re.findall(r"\bS\w+", text))

# .   → any character except newline
print(re.findall("r..n", text))

# ^   → starts with
print(re.findall("^The", text))

# $   → ends with
print(re.findall("Spain$", text))

# *   → zero or more occurrences
print(re.findall("ai*", text))

# +   → one or more occurrences
print(re.findall("ai+", text))

# ?   → zero or one occurrence
print(re.findall("ai?", text))

# {}  → exactly specified occurrences
print(re.findall("ai{1}", text))

# |   → OR
print(re.findall("rain|Spain", text))

# ()  → capture group
print(re.findall("(Spain)", text))


# ------------------------------------------------
# Special Sequences
# ------------------------------------------------

# \d → digits
print(re.findall(r"\d", "Room 123"))

# \D → non-digits
print(re.findall(r"\D", "Room 123"))

# \s → whitespace
print(re.findall(r"\s", text))

# \S → non-whitespace
print(re.findall(r"\S", text))

# \w → word characters
print(re.findall(r"\w", text))

# \W → non-word characters
print(re.findall(r"\W", text))

# \b → word boundary
print(re.findall(r"\bSpain", text))

# \B → NOT word boundary
print(re.findall(r"\Bain", text))


# ------------------------------------------------
# Sets
# ------------------------------------------------

# [abc] → matches a, b, or c
print(re.findall("[abc]", text))

# [a-z] → lowercase letters
print(re.findall("[a-z]", text))

# [A-Z] → uppercase letters
print(re.findall("[A-Z]", text))

# [0-9] → digits
print(re.findall("[0-9]", "abc123"))

# [^abc] → NOT a, b, or c
print(re.findall("[^abc]", text))


# ------------------------------------------------
# Flags
# Modify RegEx behavior
# ------------------------------------------------

# re.IGNORECASE → ignore case
print(re.findall("spain", text, re.IGNORECASE))

# re.MULTILINE → affects ^ and $
multi_text = "Hello\nWorld"
print(re.findall("^World", multi_text, re.MULTILINE))

# re.DOTALL → '.' matches newline
print(re.findall("H.*d", "Hello\nWorld", re.DOTALL))


# ------------------------------------------------
# Using compile()
# Compiles a pattern into a reusable object
# ------------------------------------------------
pattern = re.compile(r"\bS\w+")

print(pattern.findall(text))


# ------------------------------------------------
# Groups and Capturing
# ------------------------------------------------
text2 = "My number is 123-456"

match = re.search(r"(\d{3})-(\d{3})", text2)

if match:
    print("Full match:", match.group(0))
    print("Group 1:", match.group(1))
    print("Group 2:", match.group(2))


# ------------------------------------------------
# Sub with Groups
# ------------------------------------------------
print(re.sub(r"(\d{3})-(\d{3})", r"\1 \2", text2))


# ------------------------------------------------
# When to Use RegEx
# - Validation (email, phone)
# - Searching text
# - Data extraction
# - Text processing
# ------------------------------------------------