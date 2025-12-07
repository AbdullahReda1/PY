# -----------------------------------------
# PYTHON TUPLES
# -----------------------------------------

# WHAT IS A TUPLE?
# - Ordered, indexed, immutable collection. Allows duplicates.
fruits = ("apple", "banana", "cherry")
print("Tuple:", fruits)


# TUPLE ITEMS (MIXED TYPES)
# - Tuples can contain any data type.
mixed_tuple = ("text", 42, True, 3.14)
print("Mixed tuple:", mixed_tuple)


# TUPLE LENGTH
# - Use len() to get number of elements.
print("Length:", len(fruits))


# CREATE TUPLE WITH ONE ITEM
# - Must include a trailing comma (otherwise it's not a tuple).
single_item = ("apple",)
not_a_tuple = ("apple")    # string, not tuple
print("Single item type:", type(single_item), "Not a tuple type:", type(not_a_tuple))


# TYPE
print("Type of mixed_tuple:", type(mixed_tuple))


# ACCESS TUPLE ITEMS
# - Indexing (positive & negative) and slicing works.
print("First item:", fruits[0])
print("Last item:", fruits[-1])
print("Slice [0:2]:", fruits[:2])


# CHECK IF ITEM EXISTS
# - Use 'in' keyword.
if "banana" in fruits:
    print("banana found")


# IMMUTABILITY — CHANGE VALUES (WORKAROUND)
# - Convert to list, modify, convert back to tuple.
tmp_list = list(fruits)
tmp_list[1] = "blueberry"
fruits = tuple(tmp_list)
print("After change workaround:", fruits)


# ADD ITEMS (CONCATENATION)
# - Since tuples are immutable, create a new tuple by concatenation.
fruits = fruits + ("orange",)
print("After concatenation:", fruits)


# REMOVE ITEMS (WORKAROUND)
# - Convert to list, remove, then convert back.
tmp = list(fruits)
tmp.remove("blueberry")
fruits = tuple(tmp)
print("After remove workaround:", fruits)


# UNPACKING TUPLES (STANDARD)
# - Assign each element to variables (counts must match).
colors = ("red", "green", "blue")
r, g, b = colors
print("Unpacked r,g,b:", r, g, b)


# UNPACKING WITH ASTERISK - LEADING, MIDDLE, TRAILING
# - Leading star: captures the start into a list
seq = (1, 2, 3, 4, 5)
head, *tail = seq
print("Leading star -> head:", head, "tail:", tail)  # tail is list [2,3,4,5]

# - Trailing star: captures the end into a list
*head2, tail2 = seq
print("Trailing star -> head2:", head2, "tail2:", tail2)  # head2 is list [1,2,3,4]

# - MIDDLE star: captures the middle into a list (your requested case)
first, *middle, last = seq
print("Middle star -> first:", first, "middle:", middle, "last:", last)  # middle is [2,3,4]

# - More complex: two named ends and middle group
a, b, *middle2, y, z = (10, 20, 30, 40, 50, 60)
print("a,b:", a, b, "middle2:", middle2, "y,z:", y, z)  # middle2 is [30,40,50]


# LOOPING TUPLES
# - For loop, index loop, and while loop.
for item in fruits:
    print("For loop item:", item)

for i in range(len(fruits)):
    print("Index", i, "->", fruits[i])

i = 0
while i < len(fruits):
    print("While loop item:", fruits[i])
    i += 1


# JOIN TWO TUPLES
t1 = (1, 2, 3)
t2 = (4, 5)
joined = t1 + t2
print("Joined:", joined)


# MULTIPLY TUPLE
repeated = t1 * 3
print("Repeated:", repeated)


# TUPLE METHODS
# - count(value): number of occurrences
# - index(value): first index of value
demo = (1, 2, 3, 2, 2)
print("Count of 2:", demo.count(2))
print("Index of 3:", demo.index(3))