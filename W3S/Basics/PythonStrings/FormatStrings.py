# #!This code demonstrates how to format strings in Python using f-strings and the format method.
# Initializing a variable with a price
price = 50

# Using f-string to format the string
txt = f"the Price is {price} dollars"
print(txt)

# Using the format method to format the string
print("the Price is {} dollars".format(price))

# Initializing a new price variable with a different float value
price = 99.99

# Using f-string to format the new price
print(f"the Price is {price:.2f} dollars")

# Using the format method to format the new price
print("the Price is {:.2f} dollars".format(price))