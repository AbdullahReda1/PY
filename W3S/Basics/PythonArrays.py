# ==========================================
# Python Arrays (Lists)
# ==========================================


# ------------------------------------------------
# What is an Array?
# In Python, arrays are implemented using lists
# Lists can store multiple items in a single variable
# ------------------------------------------------
cars = ["Ford", "BMW", "Volvo"]
print(cars)


# ------------------------------------------------
# Access Elements
# Access items using index (starting from 0)
# ------------------------------------------------
print(cars[0])
print(cars[1])


# ------------------------------------------------
# Modify Elements
# Change the value of a specific item
# ------------------------------------------------
cars[0] = "Toyota"
print(cars)


# ------------------------------------------------
# Length of Array
# Use len() to get number of items
# ------------------------------------------------
print(len(cars))


# ------------------------------------------------
# Loop Through an Array
# ------------------------------------------------
for car in cars:
    print(car)


# ------------------------------------------------
# Add Elements
# Using append() to add at the end
# ------------------------------------------------
cars.append("Honda")
print(cars)


# ------------------------------------------------
# Remove Elements
# Using remove() to delete specific item
# ------------------------------------------------
cars.remove("BMW")
print(cars)


# ------------------------------------------------
# Remove by Index
# Using pop()
# ------------------------------------------------
cars.pop(0)
print(cars)


# ------------------------------------------------
# Delete Entire Array
# Using del keyword
# ------------------------------------------------
temp = ["A", "B", "C"]
del temp


# ------------------------------------------------
# Clear Array
# Removes all items but keeps the list
# ------------------------------------------------
cars.clear()
print(cars)


# ------------------------------------------------
# Using List Methods (Array Methods)
# ------------------------------------------------
numbers = [3, 1, 4, 2]

numbers.append(5)       # add item
numbers.insert(1, 10)   # insert at index
numbers.sort()          # sort ascending
numbers.reverse()       # reverse order

print(numbers)


# ------------------------------------------------
# Copy Array
# ------------------------------------------------
copy1 = numbers.copy()
copy2 = list(numbers)

print(copy1)
print(copy2)


# ------------------------------------------------
# Join Arrays
# ------------------------------------------------
a = [1, 2]
b = [3, 4]

joined = a + b
print(joined)


# ------------------------------------------------
# Multi-Dimensional Arrays (Nested Lists)
# ------------------------------------------------
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0][1])  # access element


# ------------------------------------------------
# Real Array Module (Optional)
# Python has array module for typed arrays
# ------------------------------------------------
import array

arr = array.array('i', [1, 2, 3, 4])  # 'i' = integer
print(arr)


# ------------------------------------------------
# When to Use Lists vs array module
# list → flexible, can hold mixed types
# array → efficient, same data type only
# ------------------------------------------------