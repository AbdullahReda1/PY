# INitializing a numerical string and an alphabetical string
num_txt = "0123456789"
str_txt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Slicing the string to get a limited substring
print(num_txt[2:5])        # Output: 234

# Slicing the string to get a substring from starting index to the end
print(num_txt[2:])         # Output: 23456789

# Slicing the string to get a substring from the start to a specific index
print(num_txt[:5])         # Output: 01234

# Show whole string using only ":"
print(num_txt[:])          # Output: 0123456789

# Slicing the string to get a substring swapped
print(num_txt[-5:-2])      # Output: 567

# Slicing the string to get a substring with a step
print(str_txt[2:5:2])      # Output: CE

# Slicing the string to get a substring from starting index to the end with step
print(str_txt[2::3])       # Output: CFILORUX

# Slicing the string to get a substring from the start to a specific index with step
print(str_txt[:19:4])      # Output: AEIMQ

# Slicing the string to get a substring with negative step
print(str_txt[19:2:-2])    # Output: TRPNLJHFD
print(str_txt[-2:-19:-3])  # Output: YVSPMJ