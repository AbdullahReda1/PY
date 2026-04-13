# ==========================================
# Python String Formatting
# ==========================================


# ------------------------------------------------
# What is String Formatting?
# Used to insert variables into strings
# ------------------------------------------------


# ------------------------------------------------
# Old Style Formatting (% operator)
# ------------------------------------------------
name = "Abdullah"
age = 25

print("My name is %s and I am %d years old" % (name, age))


# ------------------------------------------------
# format() Method
# ------------------------------------------------
text = "My name is {} and I am {} years old".format(name, age)
print(text)


# ------------------------------------------------
# Positional Arguments
# ------------------------------------------------
print("First: {0}, Second: {1}".format("A", "B"))


# ------------------------------------------------
# Named Arguments
# ------------------------------------------------
print("Name: {n}, Age: {a}".format(n="Ali", a=22))


# ------------------------------------------------
# f-Strings (Recommended)
# Python 3.6+
# ------------------------------------------------
print(f"My name is {name} and I am {age} years old")


# ------------------------------------------------
# Expressions inside f-strings
# ------------------------------------------------
print(f"Next year age: {age + 1}")


# ------------------------------------------------
# Formatting Numbers
# ------------------------------------------------

# Float precision
pi = 3.1415926535
print(f"Pi (2 decimals): {pi:.2f}")

# Width and alignment
num = 42
print(f"{num:5}")     # right aligned
print(f"{num:<5}")    # left aligned
print(f"{num:^5}")    # center aligned


# ------------------------------------------------
# Padding and Zero Fill
# ------------------------------------------------
print(f"{num:05}")   # 00042


# ------------------------------------------------
# Thousands Separator
# ------------------------------------------------
large = 1000000
print(f"{large:,}")   # 1,000,000


# ------------------------------------------------
# Percentage Formatting
# ------------------------------------------------
value = 0.85
print(f"{value:.2%}")   # 85.00%


# ------------------------------------------------
# String Formatting (alignment)
# ------------------------------------------------
text = "Python"
print(f"{text:>10}")   # right
print(f"{text:<10}")   # left
print(f"{text:^10}")   # center


# ------------------------------------------------
# Escape Characters in f-strings
# ------------------------------------------------
quote = "Abdullah"
print(f"He said \"Hello {quote}\"")


# ------------------------------------------------
# Multiline f-strings
# ------------------------------------------------
info = f"""
Name: {name}
Age: {age}
"""
print(info)


# ------------------------------------------------
# When to Use Each Method
# % formatting → legacy code
# format()     → flexible, older style
# f-strings    → modern, fastest, most readable
# ------------------------------------------------