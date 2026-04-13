# ==========================================
# Python User Input
# ==========================================


# ------------------------------------------------
# Getting User Input
# input() reads input from the user as a string
# ------------------------------------------------
name = input("Enter your name: ")
print("Hello,", name)


# ------------------------------------------------
# Input Always Returns String
# Must convert to other types if needed
# ------------------------------------------------
age = input("Enter your age: ")
print(type(age))   # <class 'str'>


# ------------------------------------------------
# Convert Input to Integer
# ------------------------------------------------
age = int(input("Enter your age: "))
print("Age next year:", age + 1)


# ------------------------------------------------
# Convert Input to Float
# ------------------------------------------------
price = float(input("Enter price: "))
print("Price with tax:", price * 1.1)


# ------------------------------------------------
# Multiple Inputs (Split)
# ------------------------------------------------
data = input("Enter numbers separated by space: ")
numbers = data.split()
print(numbers)


# ------------------------------------------------
# Convert Multiple Inputs to Integers
# ------------------------------------------------
numbers = list(map(int, input("Enter numbers: ").split()))
print(numbers)


# ------------------------------------------------
# Taking Multiple Variables in One Line
# ------------------------------------------------
x, y = input("Enter two values: ").split()
print("x:", x, "y:", y)


# ------------------------------------------------
# Convert Multiple Values to Integers
# ------------------------------------------------
x, y = map(int, input("Enter two numbers: ").split())
print("Sum:", x + y)


# ------------------------------------------------
# Handling Input Errors
# Using try/except to avoid crashes
# ------------------------------------------------
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Invalid input! Please enter a number.")


# ------------------------------------------------
# Using Prompt Messages
# Clear instructions improve usability
# ------------------------------------------------
city = input("Enter your city: ")
print("City:", city)


# ------------------------------------------------
# When to Use User Input
# - CLI programs
# - Simple tools
# - Testing logic interactively
# ------------------------------------------------