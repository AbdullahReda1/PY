# ==========================================
# Python *args and **kwargs
# ==========================================


# ------------------------------------------------
# Arbitrary Arguments (*args)
# Used when the number of positional arguments is unknown
# Collected as a tuple
# ------------------------------------------------
def print_numbers(*args):
    print("Type of args:", type(args))
    print("Values:", args)

print_numbers(1, 2, 3, 4)


# ------------------------------------------------
# Accessing *args Values
# ------------------------------------------------
def show_second(*args):
    print("Second value:", args[1])

show_second("A", "B", "C")


# ------------------------------------------------
# Looping Through *args
# ------------------------------------------------
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print("Sum:", sum_all(5, 10, 15))


# ------------------------------------------------
# Mixing Normal Parameters with *args
# *args must come after regular parameters
# ------------------------------------------------
def multiply(multiplier, *numbers):
    for num in numbers:
        print(num * multiplier)

multiply(2, 3, 4, 5)



# ==========================================
# Arbitrary Keyword Arguments (**kwargs)
# ==========================================


# ------------------------------------------------
# **kwargs
# Used when the number of keyword arguments is unknown
# Collected as a dictionary
# ------------------------------------------------
def print_info(**kwargs):
    print("Type of kwargs:", type(kwargs))
    print("Values:", kwargs)

print_info(name="Ali", age=25, country="Egypt")


# ------------------------------------------------
# Accessing **kwargs Values
# ------------------------------------------------
def show_name(**kwargs):
    print("Name:", kwargs["name"])

show_name(name="Sara", age=22)


# ------------------------------------------------
# Looping Through **kwargs
# ------------------------------------------------
def display_user(**user):
    for key, value in user.items():
        print(key, ":", value)

display_user(username="admin", password="1234")


# ------------------------------------------------
# Mixing Normal Parameters with **kwargs
# **kwargs must come last
# ------------------------------------------------
def profile(role, **details):
    print("Role:", role)
    for key, value in details.items():
        print(key, ":", value)

profile("Developer", name="Abdullah", experience=3)



# ==========================================
# Using *args and **kwargs Together
# Order must be:
# 1. Normal parameters
# 2. *args
# 3. **kwargs
# ==========================================
def combined(a, b, *args, **kwargs):
    print("a:", a)
    print("b:", b)
    print("args:", args)
    print("kwargs:", kwargs)

combined(1, 2, 3, 4, x=10, y=20)