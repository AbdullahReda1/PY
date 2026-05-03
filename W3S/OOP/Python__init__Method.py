# ==========================================
# Python __init__() Method (Constructor)
# ==========================================


# ------------------------------------------------
# What is __init__()?
# A special method automatically called when an
# object is created (constructor)
# ------------------------------------------------


# ------------------------------------------------
# Basic Usage
# Initialize object attributes
# ------------------------------------------------
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Abdullah", 25)
print(p1.name, p1.age)


# ------------------------------------------------
# Default Values in __init__()
# ------------------------------------------------
class Car:
    def __init__(self, brand="Unknown"):
        self.brand = brand

c1 = Car()
c2 = Car("Toyota")

print(c1.brand)
print(c2.brand)


# ------------------------------------------------
# Multiple Attributes Initialization
# ------------------------------------------------
class Student:
    def __init__(self, name, grade, passed):
        self.name = name
        self.grade = grade
        self.passed = passed

s1 = Student("Ali", 90, True)
print(s1.name, s1.grade, s1.passed)


# ------------------------------------------------
# Using Methods with Initialized Data
# ------------------------------------------------
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

r = Rectangle(5, 3)
print("Area:", r.area())


# ------------------------------------------------
# Validation Inside __init__()
# ------------------------------------------------
class Product:
    def __init__(self, price):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.price = price

p = Product(100)
print("Price:", p.price)


# ------------------------------------------------
# Using None as Default
# ------------------------------------------------
class User:
    def __init__(self, name=None):
        if name is None:
            name = "Guest"
        self.name = name

u1 = User()
u2 = User("Abdullah")

print(u1.name)
print(u2.name)


# ------------------------------------------------
# Dynamic Attributes via __init__()
# ------------------------------------------------
class Dynamic:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

d = Dynamic(name="Ali", age=25, city="Cairo")
print(d.name, d.age, d.city)


# ------------------------------------------------
# __init__() Does NOT Return Anything
# It must return None implicitly
# ------------------------------------------------
class Example:
    def __init__(self):
        print("Object created")

e = Example()


# ------------------------------------------------
# Calling Another Method from __init__()
# ------------------------------------------------
class Logger:
    def __init__(self, message):
        self.message = message
        self.log()

    def log(self):
        print("Log:", self.message)

l = Logger("System started")


# ------------------------------------------------
# When to Use __init__()
# - Initialize object state
# - Validate input
# - Prepare object for use
# ------------------------------------------------