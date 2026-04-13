# ==========================================
# Python None
# ==========================================


# ------------------------------------------------
# What is None?
# None represents the absence of a value
# It is a special constant of type NoneType
# ------------------------------------------------
x = None
print(x)
print(type(x))


# ------------------------------------------------
# None vs 0 vs False vs Empty
# None is NOT the same as other "empty" values
# ------------------------------------------------
print(None == 0)        # False
print(None == False)    # False
print(None == "")       # False


# ------------------------------------------------
# Checking for None (Best Practice)
# Use 'is' instead of '=='
# ------------------------------------------------
value = None

if value is None:
    print("Value is None")

if value is not None:
    print("Value exists")


# ------------------------------------------------
# Functions Returning None
# If no return statement → returns None
# ------------------------------------------------
def my_function():
    pass

result = my_function()
print(result)   # None


# ------------------------------------------------
# Explicit Return None
# ------------------------------------------------
def do_nothing():
    return None

print(do_nothing())


# ------------------------------------------------
# Using None as Default Value
# ------------------------------------------------
def greet(name=None):
    if name is None:
        print("Hello, Guest")
    else:
        print("Hello,", name)

greet()
greet("Abdullah")


# ------------------------------------------------
# None in Conditional Statements
# None is treated as False in boolean context
# ------------------------------------------------
if not None:
    print("None is False-like")


# ------------------------------------------------
# None in Data Structures
# Used as placeholder
# ------------------------------------------------
data = [1, None, 3]
print(data)


# ------------------------------------------------
# Removing None Values
# ------------------------------------------------
cleaned = [x for x in data if x is not None]
print(cleaned)


# ------------------------------------------------
# Common Use Cases
# - Default function arguments
# - Missing/optional values
# - Placeholder in data
# - Function returns when no result
# ------------------------------------------------