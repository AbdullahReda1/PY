# ==========================================
# Python Polymorphism
# ==========================================


# ------------------------------------------------
# What is Polymorphism?
# "Many forms" → same method name behaves differently
# depending on the object
# ------------------------------------------------


# ------------------------------------------------
# Polymorphism with Built-in Functions
# ------------------------------------------------
print(len("Hello"))        # string length
print(len([1, 2, 3]))     # list length


# ------------------------------------------------
# Polymorphism with Functions
# Same function works with different types
# ------------------------------------------------
def add(x, y):
    return x + y

print(add(2, 3))          # numbers
print(add("A", "B"))      # strings


# ------------------------------------------------
# Polymorphism with Class Methods (Method Overriding)
# ------------------------------------------------
class Animal:
    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):
    def speak(self):
        print("Dog barks")


class Cat(Animal):
    def speak(self):
        print("Cat meows")


animals = [Dog(), Cat(), Animal()]

for a in animals:
    a.speak()


# ------------------------------------------------
# Polymorphism with Inheritance (Same Interface)
# ------------------------------------------------
class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r ** 2


shapes = [Rectangle(3, 4), Circle(2)]

for s in shapes:
    print("Area:", s.area())


# ------------------------------------------------
# Polymorphism with Different Classes (Duck Typing)
# ------------------------------------------------
class Car:
    def move(self):
        print("Car drives")


class Boat:
    def move(self):
        print("Boat sails")


class Plane:
    def move(self):
        print("Plane flies")


vehicles = [Car(), Boat(), Plane()]

for v in vehicles:
    v.move()


# ------------------------------------------------
# Polymorphism with Operator Overloading
# ------------------------------------------------
print(1 + 2)           # addition
print("A" + "B")       # concatenation


# ------------------------------------------------
# Custom Operator Overloading
# ------------------------------------------------
class Vector:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return Vector(self.x + other.x)

    def __str__(self):
        return f"Vector({self.x})"

v1 = Vector(5)
v2 = Vector(10)

v3 = v1 + v2
print(v3)


# ------------------------------------------------
# Method Overloading (Python Style)
# Python does not support true overloading
# Use default arguments instead
# ------------------------------------------------
class Example:
    def greet(self, name=None):
        if name:
            print("Hello,", name)
        else:
            print("Hello")

e = Example()
e.greet()
e.greet("Ali")


# ------------------------------------------------
# When to Use Polymorphism
# - Write flexible and reusable code
# - Work with different object types uniformly
# - Simplify interfaces
# ------------------------------------------------