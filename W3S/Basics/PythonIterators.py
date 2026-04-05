# ==========================================
# Python Iterators
# ==========================================


# ------------------------------------------------
# What is an Iterator?
# An iterator is an object that can be iterated upon
# It implements __iter__() and __next__()
# ------------------------------------------------


# ------------------------------------------------
# Iterator vs Iterable
# Iterable → object that can return an iterator (__iter__)
# Iterator → object with __next__() to get next value
# ------------------------------------------------
my_list = [1, 2, 3]

iterator = iter(my_list)

print(next(iterator))
print(next(iterator))
print(next(iterator))


# ------------------------------------------------
# StopIteration
# Raised when there are no more items
# ------------------------------------------------
iterator = iter([1, 2])

try:
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))  # will raise error
except StopIteration:
    print("End of iterator")


# ------------------------------------------------
# Looping Through Iterator
# for loop handles StopIteration automatically
# ------------------------------------------------
for item in [10, 20, 30]:
    print(item)


# ------------------------------------------------
# Creating a Custom Iterator
# Using a class with __iter__() and __next__()
# ------------------------------------------------
class MyNumbers:
    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        if self.num <= 5:
            value = self.num
            self.num += 1
            return value
        else:
            raise StopIteration

my_iter = MyNumbers()

for x in my_iter:
    print(x)


# ------------------------------------------------
# Infinite Iterator
# Must be controlled manually
# ------------------------------------------------
class InfiniteCounter:
    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        value = self.num
        self.num += 1
        return value

counter = InfiniteCounter()

for i, val in enumerate(counter):
    if i == 5:
        break
    print(val)


# ------------------------------------------------
# Using iter() with callable
# iter(callable, sentinel)
# Calls function until sentinel value is returned
# ------------------------------------------------
def count():
    count.value += 1
    return count.value

count.value = 0

for x in iter(count, 5):
    print(x)


# ------------------------------------------------
# Relationship with Generators
# Generators are iterators automatically
# ------------------------------------------------
def simple_gen():
    yield 1
    yield 2

gen = simple_gen()

print(next(gen))
print(next(gen))


# ------------------------------------------------
# When to Use Iterators
# - Custom iteration logic
# - Large data streams
# - Lazy evaluation
# ------------------------------------------------


# ------------------------------------------------
# Advantages
# - Memory efficient
# - Full control over iteration
# ------------------------------------------------


# ------------------------------------------------
# Limitations
# - One-time use (usually)
# - Can be complex to implement manually
# ------------------------------------------------