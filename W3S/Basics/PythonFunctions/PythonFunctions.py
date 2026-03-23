# ================================
# Python Functions
# ================================


# ------------------------------------------------
# Creating a Function
# A function is defined using the def keyword
# ------------------------------------------------
def greet():
    print("Hello from a function")

greet()


# ------------------------------------------------
# Python Arguments
# Information passed into a function
# ------------------------------------------------
def greet_person(name):
    print("Hello", name)

greet_person("Abdullah")


# ------------------------------------------------
# Multiple Arguments
# Functions can accept more than one parameter
# ------------------------------------------------
def full_name(first, last):
    print(first, last)

full_name("Abdullah", "Mohamed")


# ------------------------------------------------
# Keyword Arguments
# Arguments sent using key=value format
# ------------------------------------------------
def student(name, age):
    print(name, age)

student(name="Ali", age=20)


# ------------------------------------------------
# Default Parameter Value
# Provides a default value if no argument is passed
# ------------------------------------------------
def country(name="Egypt"):
    print("Country:", name)

country()
country("USA")


# ------------------------------------------------
# Passing a List as an Argument
# ------------------------------------------------
def print_list(items):
    for item in items:
        print(item)

print_list(["A", "B", "C"])


# ------------------------------------------------
# Return Values
# Functions can return data using return
# ------------------------------------------------
def add(a, b):
    return a + b

result = add(5, 3)
print("Sum:", result)


# ------------------------------------------------
# The pass Statement
# Placeholder for empty functions
# ------------------------------------------------
def future_function():
    pass



# ================================
# Python Scope
# ================================


# ------------------------------------------------
# Local Scope
# Variable created inside a function
# ------------------------------------------------
def my_function():
    x = 10  # local variable
    print("Local x:", x)

my_function()


# ------------------------------------------------
# Global Scope
# Variable created outside a function
# ------------------------------------------------
y = 20

def show_global():
    print("Global y:", y)

show_global()


# ------------------------------------------------
# Variable Shadowing
# Same variable name in different scopes
# ------------------------------------------------
z = 100

def test_scope():
    z = 50  # local variable
    print("Local z:", z)

test_scope()
print("Global z:", z)


# ------------------------------------------------
# The global Keyword
# Used to modify a global variable inside a function
# ------------------------------------------------
counter = 0

def increase():
    global counter
    counter += 1

increase()
print("Modified global counter:", counter)