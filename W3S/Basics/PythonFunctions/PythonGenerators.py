# ==========================================
# Python Generators
# ==========================================


# ------------------------------------------------
# What is a Generator?
# A generator is a function that returns an iterator
# using 'yield' instead of 'return'
# It produces values one at a time (lazy evaluation)
# ------------------------------------------------


# ------------------------------------------------
# Generator Function with yield
# ------------------------------------------------
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()

print(next(gen))
print(next(gen))
print(next(gen))


# ------------------------------------------------
# Iterating Through a Generator
# ------------------------------------------------
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for num in count_up_to(5):
    print(num)


# ------------------------------------------------
# Generator vs Normal Function
# return → returns once and ends
# yield → pauses and resumes state
# ------------------------------------------------
def normal_function():
    return 1
    return 2   # never reached

def generator_function():
    yield 1
    yield 2


# ------------------------------------------------
# Generator Expression
# Similar to list comprehension but uses ()
# ------------------------------------------------
squares = (x * x for x in range(5))

for val in squares:
    print(val)


# ------------------------------------------------
# Using next() with Generators
# ------------------------------------------------
gen = count_up_to(3)

print(next(gen))
print(next(gen))
print(next(gen))
# next(gen) → would raise StopIteration


# ------------------------------------------------
# Handling StopIteration
# ------------------------------------------------
gen = count_up_to(2)

try:
    while True:
        print(next(gen))
except StopIteration:
    print("Generator exhausted")


# ------------------------------------------------
# Infinite Generator
# Generates values indefinitely (be careful)
# ------------------------------------------------
def infinite_counter():
    num = 1
    while True:
        yield num
        num += 1

gen = infinite_counter()

for _ in range(5):  # manual limit
    print(next(gen))


# ------------------------------------------------
# Fibonacci Sequence Generator
# Generates Fibonacci numbers lazily
# ------------------------------------------------
def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

for num in fibonacci(7):
    print(num)


# ------------------------------------------------
# Sending Values to Generators (send)
# ------------------------------------------------
def echo():
    while True:
        value = yield
        print("Received:", value)

gen = echo()
next(gen)           # Start generator
gen.send("Hello")   # Send value


# ------------------------------------------------
# yield from
# Delegates generation to another generator
# ------------------------------------------------
def sub_generator():
    yield 1
    yield 2

def main_generator():
    yield from sub_generator()
    yield 3

for val in main_generator():
    print(val)


# ------------------------------------------------
# Closing a Generator (close)
# Stops the generator execution manually
# ------------------------------------------------
def simple_gen():
    yield 1
    yield 2
    yield 3

gen = simple_gen()
print(next(gen))
gen.close()

# next(gen) would raise StopIteration after close()


# ------------------------------------------------
# yield vs return
# yield → pauses and resumes
# return → ends function completely
# ------------------------------------------------


# ------------------------------------------------
# When to Use Generators
# - Large datasets
# - Streaming data
# - Infinite sequences
# - Data pipelines
# ------------------------------------------------


# ------------------------------------------------
# Advantages
# - Memory efficient
# - Lazy evaluation
# - Cleaner iteration logic
# ------------------------------------------------


# ------------------------------------------------
# Limitations
# - Single iteration only
# - No indexing
# - Harder debugging sometimes
# ------------------------------------------------