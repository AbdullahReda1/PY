# ==========================================
# Python Try / Except (Exception Handling)
# ==========================================


# ------------------------------------------------
# What is Exception Handling?
# Used to handle runtime errors without crashing
# ------------------------------------------------


# ------------------------------------------------
# Basic Try / Except
# ------------------------------------------------
try:
    x = 10 / 0
except:
    print("An error occurred")


# ------------------------------------------------
# Catch Specific Exception
# ------------------------------------------------
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")


# ------------------------------------------------
# Multiple Exceptions
# ------------------------------------------------
try:
    num = int("abc")
except ValueError:
    print("Invalid conversion")
except ZeroDivisionError:
    print("Division error")


# ------------------------------------------------
# Multiple Exceptions in One Line
# ------------------------------------------------
try:
    x = int("abc")
except (ValueError, TypeError):
    print("Value or Type error")


# ------------------------------------------------
# Else Block
# Executes if no exception occurs
# ------------------------------------------------
try:
    x = 10 / 2
except:
    print("Error occurred")
else:
    print("Success:", x)


# ------------------------------------------------
# Finally Block
# Always executes (error or not)
# ------------------------------------------------
try:
    f = open("test.txt")
except:
    print("File not found")
finally:
    print("Execution finished")


# ------------------------------------------------
# Raising Exceptions
# ------------------------------------------------
x = -1

if x < 0:
    raise Exception("Negative value not allowed")


# ------------------------------------------------
# Raising Specific Exception
# ------------------------------------------------
age = -5

if age < 0:
    raise ValueError("Age cannot be negative")


# ------------------------------------------------
# Custom Exception
# ------------------------------------------------
class MyError(Exception):
    pass

try:
    raise MyError("Custom error occurred")
except MyError as e:
    print(e)


# ------------------------------------------------
# Exception Object
# Access error message using 'as'
# ------------------------------------------------
try:
    x = int("abc")
except ValueError as e:
    print("Error message:", e)


# ------------------------------------------------
# Using Finally to Close Resources
# ------------------------------------------------
try:
    file = open("test.txt", "r")
except:
    print("Error opening file")
finally:
    try:
        file.close()
        print("File closed")
    except:
        pass


# ------------------------------------------------
# Best Practices
# - Catch specific exceptions
# - Avoid bare except
# - Use finally for cleanup
# - Do not hide errors silently
# ------------------------------------------------