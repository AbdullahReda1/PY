# ================================
# Python For Loops
# ================================


# Python For Loops
# Used to iterate over a sequence (list, tuple, set, string, dict, range)
numbers = [1, 2, 3]

for num in numbers:
    print(num)


# Looping Through a String
# Iterates over each character in the string
text = "Python"

for char in text:
    print(char)


# The break Statement
# Stops the loop immediately when the condition is met
for i in range(10):
    if i == 5:
        break
    print("i:", i)


# The continue Statement
# Skips the current iteration and continues with the next one
for i in range(5):
    if i == 2:
        continue
    print("i:", i)


# The range() Function — stop only
# range(stop) starts from 0 and ends at stop - 1
for i in range(5):
    print(i)


# The range() Function — start and stop
# range(start, stop) starts from start and ends at stop - 1
for i in range(2, 6):
    print(i)


# The range() Function — start, stop, step
# range(start, stop, step) increments by step
for i in range(2, 10, 2):
    print(i)


# The range() Function — negative step
# Counts backward when step is negative
for i in range(10, 0, -2):
    print(i)


# Else in For Loop
# Executes when the loop finishes normally (not interrupted by break)
for i in range(3):
    print("Loop value:", i)
else:
    print("Loop completed successfully")


# Nested Loops
# A loop inside another loop
colors = ["red", "blue"]
sizes = ["S", "M", "L"]

for color in colors:
    for size in sizes:
        print(color, size)


# The pass Statement
# Used as a placeholder where a loop is required syntactically
for i in range(5):
    print("The pass keyword works now...")
    pass
