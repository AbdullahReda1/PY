# ==========================================
# Python Encapsulation
# ==========================================


# ------------------------------------------------
# What is Encapsulation?
# Wrapping data (attributes) and methods together
# and controlling access to them
# ------------------------------------------------


# ------------------------------------------------
# Public Attributes
# Accessible from anywhere
# ------------------------------------------------
class Person:
    def __init__(self, name):
        self.name = name   # public

p = Person("Ali")
print(p.name)


# ------------------------------------------------
# Protected Attributes (_single underscore)
# Convention: should not be accessed directly
# ------------------------------------------------
class Person:
    def __init__(self, name):
        self._name = name   # protected

p = Person("Omar")
print(p._name)   # still accessible, but not recommended


# ------------------------------------------------
# Private Attributes (__double underscore)
# Name mangling is applied
# ------------------------------------------------
class Person:
    def __init__(self, name):
        self.__name = name   # private

    def get_name(self):
        return self.__name

p = Person("Ahmed")

# print(p.__name) → ERROR
print(p.get_name())


# ------------------------------------------------
# Name Mangling (Internal Access)
# Python changes __name → _ClassName__name
# ------------------------------------------------
print(p._Person__name)   # not recommended, but possible


# ------------------------------------------------
# Getter and Setter Methods
# ------------------------------------------------
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount < 0:
            print("Invalid amount")
        else:
            self.__balance = amount

acc = BankAccount(1000)
print(acc.get_balance())

acc.set_balance(2000)
print(acc.get_balance())


# ------------------------------------------------
# Encapsulation Using @property
# Cleaner approach
# ------------------------------------------------
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

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
# Why Encapsulation?
# - Protect data from invalid changes
# - Control how data is accessed
# - Improve code maintainability
# ------------------------------------------------


# ------------------------------------------------
# Key Levels of Access
# public    → everywhere
# protected → internal use (convention)
# private   → class-only (name mangling)
# ------------------------------------------------