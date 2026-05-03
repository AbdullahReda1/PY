# ==========================================
# Python Class Methods
# ==========================================


# ------------------------------------------------
# What are Class Methods?
# Methods that operate on the class, not instances
# Defined using @classmethod
# First parameter is cls (not self)
# ------------------------------------------------


# ------------------------------------------------
# Basic Class Method
# ------------------------------------------------
class MyClass:
    x = 10

    @classmethod
    def show_class_value(cls):
        print("Class value:", cls.x)

MyClass.show_class_value()


# ------------------------------------------------
# Access Class Properties
# ------------------------------------------------
class Car:
    wheels = 4

    @classmethod
    def get_wheels(cls):
        return cls.wheels

print(Car.get_wheels())


# ------------------------------------------------
# Modify Class Property
# ------------------------------------------------
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def show_count(cls):
        print("Total objects:", cls.count)

c1 = Counter()
c2 = Counter()

Counter.show_count()


# ------------------------------------------------
# Class Method as Alternative Constructor
# ------------------------------------------------
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):
        name, age = data.split("-")
        return cls(name, int(age))

p = Person.from_string("Ali-25")
print(p.name, p.age)


# ------------------------------------------------
# Difference Between Instance Method and Class Method
# ------------------------------------------------
class Example:
    value = 100

    def instance_method(self):
        return self.value   # instance or class

    @classmethod
    def class_method(cls):
        return cls.value    # class only

e = Example()
print(e.instance_method())
print(Example.class_method())


# ------------------------------------------------
# Using Class Method with Inheritance
# ------------------------------------------------
class Animal:
    def __init__(self, name):
        self.name = name

    @classmethod
    def create(cls, name):
        return cls(name)

class Dog(Animal):
    pass

d = Dog.create("Buddy")
print(d.name)


# ------------------------------------------------
# Static Method vs Class Method
# ------------------------------------------------
class Math:
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def description(cls):
        return "Math class"

print(Math.add(2, 3))
print(Math.description())


# ==========================================
# Python Class Methods (Extended)
# ==========================================


# ------------------------------------------------
# What are Class Methods?
# Methods that operate on the class, not instances
# ------------------------------------------------


# ------------------------------------------------
# Basic Class Method
# ------------------------------------------------
class MyClass:
    x = 10

    @classmethod
    def show_class_value(cls):
        print("Class value:", cls.x)

MyClass.show_class_value()


# ------------------------------------------------
# Access and Modify Class Property
# ------------------------------------------------
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def show_count(cls):
        print("Total objects:", cls.count)

c1 = Counter()
c2 = Counter()

Counter.show_count()


# ------------------------------------------------
# Class Method as Alternative Constructor
# ------------------------------------------------
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):
        name, age = data.split("-")
        return cls(name, int(age))

p = Person.from_string("Ali-25")
print(p.name, p.age)


# ------------------------------------------------
# __str__() Method
# Controls string representation of object
# ------------------------------------------------
class Car:
    def __init__(self, brand):
        self.brand = brand

    def __str__(self):
        return f"Car brand: {self.brand}"

c = Car("Toyota")
print(c)


# ------------------------------------------------
# Multiple Methods in Class
# ------------------------------------------------
class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

    def show(self, a, b):
        print("Add:", self.add(a, b))
        print("Multiply:", self.multiply(a, b))

calc = Calculator()
calc.show(3, 4)


# ------------------------------------------------
# Delete Method (__del__)
# Called when object is destroyed
# ------------------------------------------------
class Example:
    def __init__(self, name):
        self.name = name
        print("Object created:", self.name)

    def __del__(self):
        print("Object deleted:", self.name)

e = Example("Test")

# Force deletion (not always immediate in real programs)
del e


# ------------------------------------------------
# Difference Recap
# instance method → uses self
# class method    → uses cls
# static method   → no self or cls
# ------------------------------------------------
class Demo:
    value = 100

    def instance_method(self):
        return self.value

    @classmethod
    def class_method(cls):
        return cls.value

    @staticmethod
    def static_method():
        return "No instance or class needed"

d = Demo()

print(d.instance_method())
print(Demo.class_method())
print(Demo.static_method())


# ------------------------------------------------
# When to Use
# - Access/modify class-level data
# - Factory methods (alternative constructors)
# - Work with inheritance
# - __str__() → readable output
# - multiple methods → organize logic
# - __del__() → cleanup (rarely used in practice)
# ------------------------------------------------