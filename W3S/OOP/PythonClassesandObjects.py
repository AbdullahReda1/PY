# ==========================================
# Python Classes and Objects
# ==========================================


# ------------------------------------------------
# What is a Class?
# A class is a blueprint for creating objects
# ------------------------------------------------
class MyClass:
    x = 5


# ------------------------------------------------
# What is an Object?
# An object is an instance of a class
# ------------------------------------------------
obj = MyClass()
print(obj.x)


# ------------------------------------------------
# The __init__() Function (Constructor)
# Automatically called when object is created
# ------------------------------------------------
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Abdullah", 25)
print(p1.name, p1.age)


# ------------------------------------------------
# The __str__() Function
# Controls what is printed when object is printed
# ------------------------------------------------
class Car:
    def __init__(self, brand):
        self.brand = brand

    def __str__(self):
        return f"Car brand: {self.brand}"

c1 = Car("Toyota")
print(c1)


# ------------------------------------------------
# Object Methods
# Functions defined inside a class
# ------------------------------------------------
class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello,", self.name)

s1 = Student("Ali")
s1.greet()


# ------------------------------------------------
# The self Parameter
# Refers to the current object instance
# ------------------------------------------------
class Example:
    def show(self):
        print("This is self:", self)

e = Example()
e.show()


# ------------------------------------------------
# Modify Object Properties
# ------------------------------------------------
p1.age = 30
print("Updated age:", p1.age)


# ------------------------------------------------
# Add Object Properties
# ------------------------------------------------
p1.city = "Cairo"
print("City:", p1.city)


# ------------------------------------------------
# Delete Object Properties
# ------------------------------------------------
del p1.city
# print(p1.city) → would raise error


# ------------------------------------------------
# Delete Object
# ------------------------------------------------
del p1
# print(p1) → would raise error


# ------------------------------------------------
# The pass Statement in Class
# Used for empty class definition
# ------------------------------------------------
class Empty:
    pass