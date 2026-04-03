# ==========================================
# Python range() Function
# ==========================================


# ------------------------------------------------
# What is range()?
# range() generates a sequence of numbers
# It is commonly used in loops
# ------------------------------------------------


# ------------------------------------------------
# range(stop)
# Starts from 0 up to (but not including) stop
# ------------------------------------------------
for i in range(5):
    print(i)   # 0, 1, 2, 3, 4


# ------------------------------------------------
# range(start, stop)
# Starts from 'start' up to (but not including) 'stop'
# ------------------------------------------------
for i in range(2, 6):
    print(i)   # 2, 3, 4, 5


# ------------------------------------------------
# range(start, stop, step)
# Increments by 'step'
# ------------------------------------------------
for i in range(0, 10, 2):
    print(i)   # 0, 2, 4, 6, 8


# ------------------------------------------------
# Negative Step
# Counts backward when step is negative
# ------------------------------------------------
for i in range(10, 0, -2):
    print(i)   # 10, 8, 6, 4, 2


# ------------------------------------------------
# Converting range to list
# ------------------------------------------------
numbers = list(range(5))
print(numbers)   # [0, 1, 2, 3, 4]


# ------------------------------------------------
# Using range() with len()
# Useful for indexing sequences
# ------------------------------------------------
items = ["A", "B", "C"]

for i in range(len(items)):
    print(i, items[i])


# ------------------------------------------------
# range() with sum()
# ------------------------------------------------
print(sum(range(5)))   # 0 + 1 + 2 + 3 + 4 = 10


# ------------------------------------------------
# Checking Membership
# range supports 'in'
# ------------------------------------------------
print(3 in range(5))   # True
print(10 in range(5))  # False


# ------------------------------------------------
# range() Object Properties
# It is immutable and memory efficient
# ------------------------------------------------
r = range(5)
print(type(r))         # <class 'range'>
print(r.start, r.stop, r.step)


# ------------------------------------------------
# Accessing Elements (Indexing)
# ------------------------------------------------
r = range(10)
print(r[0])   # first element
print(r[3])   # fourth element


# ------------------------------------------------
# Slicing range
# ------------------------------------------------
r = range(10)
print(r[2:8:2])   # range(2, 8, 2)


# ------------------------------------------------
# Comparing ranges
# Two ranges are equal if they produce same sequence
# ------------------------------------------------
print(range(0, 5, 2) == range(5))   # False


# ------------------------------------------------
# When to Use range()
# - Looping fixed number of times
# - Generating numeric sequences
# - Index-based iteration
# ------------------------------------------------