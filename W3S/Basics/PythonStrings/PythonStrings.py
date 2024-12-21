# Printing Quotes
print('Hi, "I am a Python Programmer"')         # Hi, "I am a Python Programmer"
print("Hi, 'I am a Python Programmer'")         # Hi, 'I am a Python Programmer'
print('''Hi, "I am a Python Programmer"''')     # Hi, "I am a Python Programmer"
print("""Hi, 'I am a Python Programmer'""")     # Hi, 'I am a Python Programmer'
print("Hi, \"I am a Python Programmer\"")       # Hi, "I am a Python Programmer"
print('Hi, \'I am a Python Programmer\'')       # Hi, 'I am a Python Programmer'

# Assign a string to a variable
a = "Hello, World!"
print(a)    # Hello, World!

# Multiline Strings
a = """Hi, 
I am a Python Programmer.
dont you know that?"""
print(a)
a = '''Hi,
I am a Python Programmer.
dont you know that?'''
print(a)    # Both will print the same output

# Strings are Arrays
a = "Hello, World!"
print(a[1]) # e (index starts from 0)  # 0:H, 1:e, 2:l, 3:l, 4:o, 5:, 6:W, 7:o, 8:r, 9:l, 10:d, 11:!

# Looping through a string
for x in "banana":
    print(x)    # b a n a n a (each character in a new line)

# String Length
a = "Hello, World!"
print(len(a))   # 13    (including space)

# Check String
txt = "The best things in life are free!"
print("free" in txt)    # True  (free is present inside txt)

if "free" in txt:
    print("Yes, 'free' is present in the txt")  # Yes, 'free' is present inside the txt

# Check if NOT
txt = "The best things in life are free!"
print("expensive" not in txt)   # True  (expensive is not present inside txt)

if "expensive" not in txt:
    print("Yes, 'expensive' is not present in the txt")  # Yes, 'expensive' is not present inside the txt