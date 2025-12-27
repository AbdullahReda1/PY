# =======================================
# Python Conditional if / else Statements
# =======================================


# Python If
# Executes a block of code if the condition is True
# sourcery skip: remove-redundant-pass
x = 10
if x > 5:
    print("x is greater than 5")


# Python Elif
# Checks another condition if the previous if condition is False
y = 10
if y < 5:
    print("y is less than 5")
elif y == 10:
    print("y is equal to 10")


# Python Else
# Executes when all previous conditions are False
z = 3
if z > 10:
    print("z is greater than 10")
else:
    print("z is 10 or less")


# Shorthand If
# One-line if statement for simple conditions
a = 15
if a > 10: print("a is greater than 10")


# Shorthand If...Else (Ternary Operator)
# One-line if-else expression
b = 7
result = "Even" if b % 2 == 0 else "Odd"
print(result)


# Logical Operators
# Used to combine multiple conditions (and, or, not)
age = 20
has_id = True

if age >= 18 and has_id:
    print("Access granted")

if age < 18 or not has_id:
    print("Access denied")


# Nested If
# An if statement inside another if statement
score = 85

if score >= 50:
    if score >= 80:
        print("Excellent")
    else:
        print("Passed")
else:
    print("Failed")


# Pass Statement
# Used as a placeholder when a statement is syntactically required
value = 5

if value > 0:
    print("The pass keyword works now...")
    pass