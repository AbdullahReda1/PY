# ==========================================
# Python Inner Classes
# ==========================================


# ------------------------------------------------
# What is an Inner Class?
# A class defined inside another class
# Used to logically group related classes
# ------------------------------------------------


# ------------------------------------------------
# Basic Inner Class
# ------------------------------------------------
class Outer:
    class Inner:
        def show(self):
            print("Inside Inner Class")

# Create inner class object
inner_obj = Outer.Inner()
inner_obj.show()


# ------------------------------------------------
# Inner Class with Outer Class Object
# ------------------------------------------------
class Outer:
    def __init__(self):
        self.inner = self.Inner()   # create inner instance

    class Inner:
        def show(self):
            print("Inner class method")

o = Outer()
o.inner.show()


# ------------------------------------------------
# Access Outer Class from Inner Class
# ------------------------------------------------
class Outer:
    def __init__(self, name):
        self.name = name
        self.inner = self.Inner(self)

    class Inner:
        def __init__(self, outer):
            self.outer = outer   # reference to outer object

        def display(self):
            print("Outer name:", self.outer.name)

o = Outer("Abdullah")
o.inner.display()


# ------------------------------------------------
# Multiple Inner Classes
# ------------------------------------------------
class Computer:
    class CPU:
        def info(self):
            print("CPU: Intel")

    class RAM:
        def info(self):
            print("RAM: 16GB")

comp = Computer()

cpu = comp.CPU()
ram = comp.RAM()

cpu.info()
ram.info()


# ------------------------------------------------
# Inner Class for Encapsulation
# Hide internal logic
# ------------------------------------------------
class Car:
    def __init__(self):
        self._engine = self.Engine()

    class Engine:
        def start(self):
            print("Engine started")

    def start_car(self):
        self._engine.start()

c = Car()
c.start_car()


# ------------------------------------------------
# When to Use Inner Classes
# - Logical grouping
# - Hide helper classes
# - Tight relationship between classes
# ------------------------------------------------


# ------------------------------------------------
# Key Notes
# - Inner class does NOT automatically access outer class
# - Must pass outer instance explicitly if needed
# - Mainly used for structure and organization
# ------------------------------------------------