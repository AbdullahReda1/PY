# Setting the Data Type (Built-in Data Types), and Getting the Data Type

x = "Hello World"                                  # str
print("x = ", x, " ->  its type is: ",type(x))
x = 20                                             # int
print("x = ", x, " ->  its type is: ",type(x))
x = 20.5                                           # float
print("x = ", x, " ->  its type is: ",type(x))
x = 1j                                             # complex
print("x = ", x, " ->  its type is: ",type(x))
x = ["apple", "banana", "cherry"]                  # list
print("x = ", x, " ->  its type is: ",type(x))
x = ("apple", "banana", "cherry")                  # tuple
print("x = ", x, " ->  its type is: ",type(x))
x = range(6)                                       # range
print("x = ", x, " ->  its type is: ",type(x))
x = {"name" : "John", "age" : 36}                  # dict
print("x = ", x, " ->  its type is: ",type(x))
x = {"apple", "banana", "cherry"}                  # set
print("x = ", x, " ->  its type is: ",type(x))
x = frozenset({"apple", "banana", "cherry"})       # frozenset
print("x = ", x, " ->  its type is: ",type(x))
x = True                                           # bool
print("x = ", x, " ->  its type is: ",type(x))
x = b"Hello"                                       # bytes
print("x = ", x, " ->  its type is: ",type(x))
x = bytearray(5)                                   # bytearray
print("x = ", x, " ->  its type is: ",type(x))
x = memoryview(bytes(5))                           # memoryview
print("x = ", x, " ->  its type is: ",type(x))
x = None                                           # NoneType
print("x = ", x, " ->  its type is: ",type(x))


# Setting the Specific Data Type (Casting)

x = str("Hello World")                              # str
x = int(20)                                         # int
x = float(20.5)                                     # float
x = complex(1j)                                     # complex
x = list(("apple", "banana", "cherry"))             # list
x = tuple(("apple", "banana", "cherry"))            # tuple
x = range(6)                                        # range
x = dict(name="John", age=36)                       # dict
x = set(("apple", "banana", "cherry"))              # set
x = frozenset(("apple", "banana", "cherry"))        # frozenset
x = bool(5)                                         # bool
x = bytes(5)                                        # bytes
x = bytearray(5)                                    # bytearray
x = memoryview(bytes(5))                            # memoryview