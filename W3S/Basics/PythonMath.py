# ==========================================
# Python Math
# ==========================================


# ------------------------------------------------
# Built-in Math Functions
# Python has some math functions without importing
# ------------------------------------------------

# Minimum and Maximum
print(min(5, 10, 25))
print(max(5, 10, 25))

# Absolute Value
print(abs(-7.25))

# Power
print(pow(4, 3))   # 4^3


# ------------------------------------------------
# The math Module
# Provides advanced mathematical functions
# ------------------------------------------------
import math


# ------------------------------------------------
# Math Constants
# ------------------------------------------------
print(math.pi)   # π
print(math.e)    # Euler's number


# ------------------------------------------------
# Rounding Functions
# ------------------------------------------------
print(math.ceil(1.4))   # Round up
print(math.floor(1.4))  # Round down


# ------------------------------------------------
# Square Root and Power
# ------------------------------------------------
print(math.sqrt(16))
print(math.pow(2, 3))   # returns float


# ------------------------------------------------
# Trigonometric Functions (angles in radians)
# ------------------------------------------------
print(math.sin(math.pi / 2))
print(math.cos(0))
print(math.tan(math.pi / 4))


# ------------------------------------------------
# Convert Degrees ↔ Radians
# ------------------------------------------------
print(math.radians(90))
print(math.degrees(math.pi / 2))


# ------------------------------------------------
# Logarithmic Functions
# ------------------------------------------------
print(math.log(10))        # natural log
print(math.log10(100))     # base-10 log
print(math.log2(8))        # base-2 log


# ------------------------------------------------
# Factorial
# ------------------------------------------------
print(math.factorial(5))


# ------------------------------------------------
# Greatest Common Divisor (GCD)
# ------------------------------------------------
print(math.gcd(12, 18))


# ------------------------------------------------
# When to Use math Module
# - Scientific calculations
# - Geometry / trigonometry
# - Engineering / robotics (important for you)
# ------------------------------------------------