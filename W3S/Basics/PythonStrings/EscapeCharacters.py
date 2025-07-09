# The escape characters in Python are used to insert special characters into strings.
# Escape characters are preceded by a backslash (\) and allow you to include characters that are otherwise difficult to type directly.
print("The place here is called \"SAFE\"")

# Using a backslash to escape a single quote
print('It\'s alright.')

# Using a backslash to escape a backslash
print("This will insert one \\ (backslash).")

# Using a backslash to insert a new line
print("After this down\na new line")

# Using a backslash to carriage return which moves the cursor to the beginning of the line
print("Hello\rCutted word you can't see")

# Using a backslash to insert a tab
print("Here\ta tab")

# Using a backslash to insert a backspace
print("Here using \bbackspace")

# Using a backslash to insert a form feed (page break)
print("This is page one\fThis is page two")

# Using a backslash to insert a unicode character omega
print("This is a unicode character: \u03A9 (Omega)")

# Using a backslash to insert a octal value of a character
print("\110\145\154\154\157 in octal values")

# Using a backslash to insert a hexadecimal value of a character
print("\x48\x65\x6c\x6c\x6f in hex values")