# ==========================================
# Python Decorators
# ==========================================


# ------------------------------------------------
# What is a Decorator?
# A decorator is a function that takes another
# function and extends its behavior without
# modifying the original function.
# ------------------------------------------------


# ------------------------------------------------
# Functions as First-Class Objects
# Functions can be assigned to variables
# ------------------------------------------------
def greet():
    print("Hello!")

say_hello = greet
say_hello()


# ------------------------------------------------
# Functions Inside Functions (Nested Functions)
# ------------------------------------------------
def outer():
    print("Outer function")

    def inner():
        print("Inner function")

    inner()

outer()


# ------------------------------------------------
# Returning Functions from Functions
# ------------------------------------------------
def outer_function():
    def inner_function():
        print("Hello from inner function")
    return inner_function

my_func = outer_function()
my_func()


# ------------------------------------------------
# Creating a Simple Decorator
# ------------------------------------------------
def my_decorator(func):
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper


# Applying Decorator Manually
def say_hi():
    print("Hi!")

decorated_function = my_decorator(say_hi)
decorated_function()


# ------------------------------------------------
# Using the @ Decorator Syntax
# ------------------------------------------------
@my_decorator
def welcome():
    print("Welcome!")

welcome()


# ------------------------------------------------
# Decorator with Arguments
# Use *args and **kwargs to support any function
# ------------------------------------------------
def decorator_with_args(func):
    def wrapper(*args, **kwargs):
        print("Before execution")
        result = func(*args, **kwargs)
        print("After execution")
        return result
    return wrapper


@decorator_with_args
def add(a, b):
    return a + b

print("Result:", add(5, 3))


# ------------------------------------------------
# Multiple Decorators
# Decorators are applied from bottom to top
# ------------------------------------------------
def decorator_one(func):
    def wrapper():
        print("Decorator One")
        func()
    return wrapper


def decorator_two(func):
    def wrapper():
        print("Decorator Two")
        func()
    return wrapper


@decorator_one
@decorator_two
def greet_user():
    print("Hello User!")

greet_user()