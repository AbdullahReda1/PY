# ==========================================
# Python Lambda Functions
# ==========================================


# ------------------------------------------------
# What is a Lambda Function?
# A lambda is a small anonymous function defined
# using the 'lambda' keyword (no name, one expression).
# Syntax: lambda arguments : expression
# ------------------------------------------------
add = lambda a, b: a + b
print("Lambda add:", add(5, 3))


# ------------------------------------------------
# Lambda with One Argument
# ------------------------------------------------
square = lambda x: x * x
print("Square:", square(4))


# ------------------------------------------------
# Lambda with Multiple Arguments
# ------------------------------------------------
multiply = lambda a, b, c: a * b * c
print("Multiply:", multiply(2, 3, 4))


# ------------------------------------------------
# Lambda Inside Another Function
# Used to create small function factories
# ------------------------------------------------
def make_multiplier(n):
    return lambda x: x * n

double = make_multiplier(2)
triple = make_multiplier(3)

print("Double:", double(5))
print("Triple:", triple(5))


# ------------------------------------------------
# Using Lambda with map()
# map(function, iterable) applies function to all items
# ------------------------------------------------
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x * x, numbers))
print("Squared with map:", squared)


# ------------------------------------------------
# Using Lambda with filter()
# filter(function, iterable) filters items based on condition
# ------------------------------------------------
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)


# ------------------------------------------------
# Using Lambda with sorted()
# key=lambda allows custom sorting logic
# ------------------------------------------------
pairs = [(1, 3), (2, 1), (4, 2)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print("Sorted by second element:", sorted_pairs)


# ------------------------------------------------
# Lambda with Conditional Expression
# (like inline if-else)
# ------------------------------------------------
check = lambda x: "Even" if x % 2 == 0 else "Odd"
print("Check 5:", check(5))
print("Check 6:", check(6))


# ------------------------------------------------
# Limitations of Lambda
# - Only one expression allowed
# - Cannot contain statements (e.g., loops, assignments)
# - Best for short, simple functions
# ------------------------------------------------


# ------------------------------------------------
# When to Use Lambda
# - Short, throwaway functions
# - Functional programming tools (map, filter, sorted)
# - Avoid overuse for complex logic
# ------------------------------------------------