# Initializing two string variables to demonstrate string concatenation
# sourcery skip: use-fstring-for-concatenation
txt1 = "Hello"
txt2 = "World"

# Concatenation using + operator
print(txt1 + txt2)

# Concatenation with a space in between
print(txt1 + " " + txt2)

# Concatenation with a string literal all in one variable string
txt3 = txt1 + " " + txt2 + " " + "python"
print(txt3)