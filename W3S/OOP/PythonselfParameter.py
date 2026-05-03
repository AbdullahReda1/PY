# ==========================================
# Python self Parameter
# ==========================================


# ------------------------------------------------
# What is self?
# 'self' refers to the current instance (object)
# It is used to access variables and methods
# ------------------------------------------------


# ------------------------------------------------
# Basic Usage of self
# ------------------------------------------------
class Person:
    def __init__(self, name):
        self.name = name   # assign value to object

    def greet(self):
        print("Hello,", self.name)

p1 = Person("Abdullah")
p1.greet()


# ------------------------------------------------
# self is Required in Instance Methods
# It must be the first parameter
# ------------------------------------------------
class Example:
    def show(self):
        print("This is a method")

e = Example()
e.show()


# ------------------------------------------------
# self Refers to the Current Object
# ------------------------------------------------
class Test:
    def show(self):
        print(self)

t = Test()
t.show()      # prints object reference
print(t)      # same object


# ------------------------------------------------
# Using self to Access Attributes
# ------------------------------------------------
class Car:
    def __init__(self, brand):
        self.brand = brand

    def display(self):
        print("Brand:", self.brand)

c = Car("Toyota")
c.display()


# ------------------------------------------------
# Using self to Call Other Methods
# ------------------------------------------------
class Calculator:
    def square(self, x):
        return x * x

    def show_square(self, x):
        print("Square:", self.square(x))

calc = Calculator()
calc.show_square(5)


# ------------------------------------------------
# self is Just a Naming Convention
# You can use any name, but 'self' is standard
# ------------------------------------------------
class Demo:
    def __init__(this, value):  # sourcery skip: instance-method-first-arg-name
        this.value = value

    def show(this):  # sourcery skip: instance-method-first-arg-name
        print(this.value)

d = Demo(10)
d.show()


# ------------------------------------------------
# What Happens Internally
# obj.method() → Class.method(obj)
# ------------------------------------------------
class Sample:
    def greet(self):
        print("Hello")

s = Sample()

s.greet()             # normal call
Sample.greet(s)       # equivalent call


# ------------------------------------------------
# Common Mistake (Forgetting self)
# ------------------------------------------------
class Wrong:
    def greet():   # missing self
        print("Hello")

# w = Wrong()
# w.greet() → ERROR


# ------------------------------------------------
# Using self with Attributes Added Later
# ------------------------------------------------
class User:
    def set_name(self, name):
        self.name = name

    def show(self):
        print(self.name)

u = User()
u.set_name("Ali")
u.show()


# ------------------------------------------------
# When to Use self
# - Access instance variables
# - Call instance methods
# - Represent the current object
# ------------------------------------------------