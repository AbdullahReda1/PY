# ==========================================
# Python Class Properties (Attributes)
# ==========================================


# ------------------------------------------------
# What are Class Properties?
# Variables that belong to a class or its objects
# ------------------------------------------------


# ------------------------------------------------
# Instance Properties
# Unique for each object (defined using self)
# ------------------------------------------------
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Ali", 25)
p2 = Person("Omar", 30)

print(p1.name, p2.name)


# ------------------------------------------------
# Class Properties (Class Attributes)
# Shared among all objects
# ------------------------------------------------
class Car:
    wheels = 4   # class property

    def __init__(self, brand):
        self.brand = brand

c1 = Car("Toyota")
c2 = Car("BMW")

print(c1.wheels)
print(c2.wheels)


# ------------------------------------------------
# Access Class Property via Class
# ------------------------------------------------
print(Car.wheels)


# ------------------------------------------------
# Modify Class Property
# Affects all instances (unless overridden)
# ------------------------------------------------
Car.wheels = 6

print(c1.wheels)
print(c2.wheels)


# ------------------------------------------------
# Override Class Property in Instance
# ------------------------------------------------
c1.wheels = 8   # only for c1

print(c1.wheels)  # 8
print(c2.wheels)  # 6


# ------------------------------------------------
# Add New Instance Property
# ------------------------------------------------
p1.city = "Cairo"
print(p1.city)


# ------------------------------------------------
# Delete Properties
# ------------------------------------------------
del p1.city
# print(p1.city) → ERROR


# ------------------------------------------------
# Built-in Functions for Properties
# ------------------------------------------------
print(hasattr(p1, "name"))     # check existence
print(getattr(p1, "name"))     # get value

setattr(p1, "country", "Egypt")
print(p1.country)

delattr(p1, "country")


# ------------------------------------------------
# Property Decorator (@property)
# Allows method to be accessed like attribute
# ------------------------------------------------
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius   # protected-like

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273:
            raise ValueError("Below absolute zero!")
        self._celsius = value

t = Temperature(25)
print(t.celsius)

t.celsius = 30
print(t.celsius)


# ------------------------------------------------
# Read-Only Property
# ------------------------------------------------
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        return 3.14 * self._radius ** 2

c = Circle(5)
print(c.area)


# ------------------------------------------------
# When to Use Properties
# - Control access to attributes
# - Add validation
# - Hide internal implementation
# ------------------------------------------------