# ==========================================
# Python Inheritance
# ==========================================


# ------------------------------------------------
# What is Inheritance?
# Allows a class (child) to inherit properties and
# methods from another class (parent)
# ------------------------------------------------


# ------------------------------------------------
# Basic Inheritance
# ------------------------------------------------
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello,", self.name)


class Student(Person):   # inherits from Person
    pass


s = Student("Ali")
s.greet()


# ------------------------------------------------
# Add New Methods in Child Class
# ------------------------------------------------
class Student(Person):
    def study(self):
        print(self.name, "is studying")

s = Student("Omar")
s.study()
s.greet()


# ------------------------------------------------
# Override Parent Method
# ------------------------------------------------
class Student(Person):
    def greet(self):
        print("Hi, I am student", self.name)

s = Student("Ahmed")
s.greet()


# ------------------------------------------------
# Use super() to Call Parent Constructor
# ------------------------------------------------
class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

s = Student("Ali", 90)
print(s.name, s.grade)


# ------------------------------------------------
# Use super() for Methods
# ------------------------------------------------
class Student(Person):
    def greet(self):
        super().greet()
        print("Welcome to class!")

s = Student("Mona")
s.greet()


# ------------------------------------------------
# Multiple Inheritance
# ------------------------------------------------
class A:
    def method_a(self):
        print("From class A")

class B:
    def method_b(self):
        print("From class B")

class C(A, B):
    pass

c = C()
c.method_a()
c.method_b()


# ------------------------------------------------
# Multilevel Inheritance
# ------------------------------------------------
class Animal:
    def speak(self):
        print("Animal makes sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Puppy(Dog):
    def cute(self):
        print("Puppy is cute")

p = Puppy()
p.speak()
p.bark()
p.cute()


# ------------------------------------------------
# Hierarchical Inheritance
# ------------------------------------------------
class Animal:
    def eat(self):
        print("Animal eats")

class Dog(Animal):
    pass

class Cat(Animal):
    pass

d = Dog()
c = Cat()

d.eat()
c.eat()


# ------------------------------------------------
# Check Inheritance
# ------------------------------------------------
print(isinstance(s, Student))   # True
print(isinstance(s, Person))    # True

print(issubclass(Student, Person))  # True


# ------------------------------------------------
# Method Resolution Order (MRO)
# Determines order of method lookup
# ------------------------------------------------
print(Student.__mro__)


# ------------------------------------------------
# When to Use Inheritance
# - Code reuse
# - Represent real-world relationships
# - Extend functionality
# ------------------------------------------------