# Lists
x = [4, 5]
y = [4, 5]
z = x

# is - Checks if both variables point to the same object in memory
print(x is y)
print(x is z)

# == - Checks if the values of both variables are equal
print(x == y)


print(x is not y)
print(x is not z)
print(x != y)