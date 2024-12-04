# Int
x, y, z = 5, 35656222554887711, -3255522
print("int: ", x, " or ", y, " or ", z)

print("---------------------------------------------")

# Float
x, y, z = 1.10, 1.0, -35.59
print("float: ", x, " or ", y, " or ", z)

print("---------------------------------------------")

# Scientific "e" Float
x, y, z = 35e3, 12E4, -87.7e100
print("float(e): ", x, " or ", y, " or ", z)

print("---------------------------------------------")

# Complex
x, y, z = 3+5j, 5j, -5j
print("complex: ", x, " or ", y, " or ", z)

print("---------------------------------------------")

# Type Conversion
x, y, z = 1, 2.3, 4j
a, b, c = float(x), int(y), complex(x)
print(a, "    -> its type is "   ,type(a))
print(b, "      -> its type is " ,type(b))
print(c, " -> its type is "      ,type(c))

print("---------------------------------------------")

# Random Number
import random
print("Random Number is ", random.randrange(1, 100))