# ============================================================
# PYTHON LISTS — COMPLETE W3SCHOOLS SUMMARY + CODE EXAMPLES
# ============================================================


# ------------------------------------------------------------
# WHAT ARE LISTS?
# Description: Ordered, mutable collections that allow duplicate values.
# ------------------------------------------------------------
numbers = [1, 2, 3, 4, 5]
print("Original list:", numbers)


# ------------------------------------------------------------
# LIST ITEMS (MIXED TYPES)
# Description: Lists can contain any data type.
# ------------------------------------------------------------
mixed_items = ["apple", 42, True]
print("Mixed items:", mixed_items)


# ------------------------------------------------------------
# LIST LENGTH
# Description: len() returns number of elements.
# ------------------------------------------------------------
print("Length:", len(numbers))


# ------------------------------------------------------------
# ACCESS ITEMS
# Description: Use index, negative index, or slicing.
# ------------------------------------------------------------
print("First item:", numbers[0])
print("Last item:", numbers[-1])
print("Slice [1:4]:", numbers[1:4])
print("Negative slice:", numbers[-4:-1])


# ------------------------------------------------------------
# CHECK IF ITEM EXISTS
# Description: Use `in` keyword.
# ------------------------------------------------------------
if 3 in numbers:
    print("3 is in the list")


# ------------------------------------------------------------
# CHANGE ITEMS
# Description: Assign new values to indexes or slices.
# ------------------------------------------------------------
numbers[1] = 20
numbers[1:3] = [200, 300]
print("After modifications:", numbers)


# ------------------------------------------------------------
# INSERT ITEMS
# Description: insert(index, value) inserts without replacing.
# ------------------------------------------------------------
numbers.insert(2, 999)
print("After insert:", numbers)


# ------------------------------------------------------------
# ADD ITEMS
# Description: append() adds one item; extend() adds multiple.
# ------------------------------------------------------------
numbers.append(6)
numbers.extend([7, 8])
print("After additions:", numbers)


# ------------------------------------------------------------
# REMOVE ITEMS
# Description: remove(), pop(), del, clear().
# ------------------------------------------------------------
numbers.remove(999)         # Remove by value
popped = numbers.pop()      # Remove last item
del numbers[0]              # Remove by index
temp = [1, 2, 3]
temp.clear()                # Empty list
print("After remove/clear:", numbers)
print("Cleared temp list:", temp)


# ------------------------------------------------------------
# LOOP LISTS — FOR, INDEX, WHILE
# ------------------------------------------------------------
items = [10, 20, 30]

print("Loop with for:")
for item in items:
    print(item)

print("Loop with index:")
for i in range(len(items)):
    print(i, items[i])

print("Loop with while:")
i = 0
while i < len(items):
    print(items[i])
    i += 1


# ------------------------------------------------------------
# LIST COMPREHENSION
# Description: Compact syntax for creating lists.
# ------------------------------------------------------------
squares = [x * x for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
print("Squares:", squares)
print("Even numbers:", evens)


# ------------------------------------------------------------
# SORT LISTS
# Description: sort(), reverse, key functions.
# ------------------------------------------------------------
values = [5, 3, 8, 1, 9]
values.sort()
print("Sorted ascending:", values)

values.sort(reverse=True)
print("Sorted descending:", values)

words = ["banana", "Apple", "cherry", "mango"]
words.sort(key=len)
print("Sorted by length:", words)

words.sort(key=str.lower)
print("Case-insensitive sort:", words)

values.reverse()
print("Reversed list:", values)


# ------------------------------------------------------------
# COPY LISTS
# Description: copy() or list() creates independent copies.
# ------------------------------------------------------------
original = [1, 2, 3]
copy_a = original.copy()
copy_b = list(original)
print("Copies:", copy_a, copy_b)


# ------------------------------------------------------------
# JOIN LISTS
# Description: combine using + or extend().
# ------------------------------------------------------------
list_a = [1, 2, 3]
list_b = [4, 5, 6]

joined = list_a + list_b
print("Joined (+):", joined)

list_a.extend(list_b)
print("Extended:", list_a)


# ------------------------------------------------------------
# FULL LIST METHODS OVERVIEW
# Description: Quick demonstration of all major list methods.
# ------------------------------------------------------------
demo = [10, 20, 20, 30, 40]

demo.append(50)           # Add at end
copy_demo = demo.copy()   # Copy list
count_20 = demo.count(20) # Count occurrences
demo.extend([100, 200])   # Add multiple elements
index_30 = demo.index(30) # Get index
demo.insert(1, 999)       # Insert item
demo.pop()                # Remove last element
demo.remove(999)          # Remove by value
demo.reverse()            # Reverse order
demo.sort()               # Sort ascending

print("List methods output:", demo)
print("Count of 20:", count_20)
print("Index of 30:", index_30)