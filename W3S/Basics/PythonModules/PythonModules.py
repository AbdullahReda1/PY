# ==========================================
# Python Modules
# ==========================================


# ------------------------------------------------
# What is a Module?
# A module is a file containing Python code (.py)
# It can define functions, variables, and classes
# ------------------------------------------------


# ------------------------------------------------
# Import a Module
# Use import to include a module
# ------------------------------------------------
import math

print(math.sqrt(16))


# ------------------------------------------------
# Access Module Members
# Use dot notation
# ------------------------------------------------
print(math.pi)


# ------------------------------------------------
# Rename a Module (Alias)
# Use 'as' to give a shorter name
# ------------------------------------------------
import math as m

print(m.factorial(5))


# ------------------------------------------------
# Import Specific Items
# Use from ... import ...
# ------------------------------------------------
from math import sqrt, pi

print(sqrt(25))
print(pi)


# ------------------------------------------------
# Import All (*)  [Not Recommended]
# Imports everything into current namespace
# ------------------------------------------------
from math import *

print(sin(0))


# ------------------------------------------------
# Built-in Modules
# Python comes with many built-in modules
# ------------------------------------------------
import platform

print(platform.system())


# ------------------------------------------------
# Using dir()
# Lists all names defined in a module
# ------------------------------------------------
print(dir(math))


# ------------------------------------------------
# Import Custom Module
# (Assuming mymodule.py exists in same directory)
# ------------------------------------------------
import mymodule
print(mymodule.greet("Abdullah"))


# ------------------------------------------------
# Variables in Module
# Modules can also contain variables
# ------------------------------------------------
mymodule.person = {"name": "Ali", "age": 25}

# Access:
print(mymodule.person["name"])


# ------------------------------------------------
# Re-importing Modules
# Modules are loaded once and cached
# ------------------------------------------------
import sys

print("math" in sys.modules)


# ------------------------------------------------
# Module Search Path
# Python searches for modules in directories
# ------------------------------------------------
print(sys.path)


# ------------------------------------------------
# __name__ Variable
# "__main__" when file is run directly
# Module name when imported
# ------------------------------------------------
def test():
    print("Running test function")

if __name__ == "__main__":
    test()


# ------------------------------------------------
# When to Use Modules
# - Organize large programs
# - Reuse code
# - Separate concerns
# ------------------------------------------------