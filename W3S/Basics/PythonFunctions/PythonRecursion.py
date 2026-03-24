# ==========================================
# Python Recursion
# ==========================================


# ------------------------------------------------
# What is Recursion?
# Recursion is when a function calls itself to solve
# a problem by breaking it into smaller subproblems.
# ------------------------------------------------


# ------------------------------------------------
# Base Case (Stopping Condition)
# Prevents infinite recursion
# ------------------------------------------------
def countdown(n):
    if n == 0:   # Base case
        print("Done!")
        return
    print(n)
    countdown(n - 1)

countdown(5)


# ------------------------------------------------
# Recursive Case
# Function continues calling itself with smaller input
# ------------------------------------------------
def sum_numbers(n):
    if n == 0:
        return 0
    return n + sum_numbers(n - 1)

print("Sum:", sum_numbers(5))


# ------------------------------------------------
# Factorial Example
# n! = n * (n-1) * ... * 1
# ------------------------------------------------
def factorial(n):
    if n == 0 or n == 1:   # Base case
        return 1
    return n * factorial(n - 1)

print("Factorial:", factorial(5))


# ------------------------------------------------
# Recursion vs Iteration
# Same logic using loop (iteration)
# ------------------------------------------------
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print("Factorial (iterative):", factorial_iterative(5))


# ------------------------------------------------
# Recursive Tree Thinking
# Each call creates a new stack frame
# Example: Fibonacci sequence
# ------------------------------------------------
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci:", fibonacci(6))


# ------------------------------------------------
# Recursion Depth and Limit
# Python limits recursion depth to prevent crashes
# ------------------------------------------------
import sys
print("Recursion limit:", sys.getrecursionlimit())
# You can set a new limit (use with caution)
# sys.setrecursionlimit(2000)


# ------------------------------------------------
# Tail Recursion (Concept)
# Python does NOT optimize tail recursion
# (unlike some other languages)
# ------------------------------------------------
def tail_recursive(n, acc=0):
    if n == 0:
        return acc
    return tail_recursive(n - 1, acc + n)

print("Tail recursion result:", tail_recursive(5))


# ------------------------------------------------
# When to Use Recursion
# - Tree/graph problems
# - Divide and conquer (e.g., merge sort)
# - Problems that can be broken into similar subproblems
# ------------------------------------------------


# ------------------------------------------------
# Risks of Recursion
# - Infinite recursion if no base case
# - Stack overflow if too deep
# - Sometimes slower than iteration
# ------------------------------------------------