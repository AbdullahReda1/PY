# ============================================================
# PYTHON SETS — COMPLETE W3SCHOOLS SUMMARY + CODE EXAMPLES
# ============================================================
# Characteristics:
# - Unordered, unindexed
# - Mutable (except frozenset)
# - No duplicate values
# ============================================================


# ------------------------------------------------------------
# WHAT IS A SET?
# Description: A set stores unique values and does not maintain order.
# ------------------------------------------------------------
fruits = {"apple", "banana", "cherry", "apple"}  # duplicate ignored
print("Set:", fruits)


# ------------------------------------------------------------
# SET ITEMS (DATA TYPES)
# Description: Set items can be of any immutable data type.
# ------------------------------------------------------------
mixed_set = {"text", 42, True, 3.14}
print("Mixed set:", mixed_set)


# ------------------------------------------------------------
# ACCESS SET ITEMS
# Description: Sets cannot be indexed; access via iteration or `in`.
# ------------------------------------------------------------
print("banana in set:", "banana" in fruits)


# ------------------------------------------------------------
# ADD SET ITEMS
# Description: add() adds one item; update() adds multiple.
# ------------------------------------------------------------
fruits.add("orange")
fruits.update({"mango", "grape"})
print("After add/update:", fruits)


# ------------------------------------------------------------
# REMOVE SET ITEMS
# Description:
# - remove(): error if not found
# - discard(): no error if not found
# - pop(): removes random item
# - clear(): removes all items
# - del: deletes the set
# ------------------------------------------------------------
fruits.remove("banana")
fruits.discard("kiwi")     # no error
removed_item = fruits.pop()
print("Random removed item:", removed_item)

temp_set = {1, 2, 3}
temp_set.clear()
print("Cleared set:", temp_set)


# ------------------------------------------------------------
# LOOP SETS
# Description: Loop using for loop (order not guaranteed).
# ------------------------------------------------------------
colors = {"red", "green", "blue"}
for color in colors:
    print("Color:", color)


# ------------------------------------------------------------
# JOIN SETS
# Description:
# - union() / |
# - update()
# - intersection() / &
# - intersection_update()
# - difference() / -
# - difference_update()
# - symmetric_difference() / ^
# - symmetric_difference_update()
# ------------------------------------------------------------
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print("Union:", set_a.union(set_b))
print("Union |:", set_a | set_b)

print("Intersection:", set_a.intersection(set_b))
print("Intersection &:", set_a & set_b)

print("Difference A-B:", set_a.difference(set_b))
print("Difference A-B -:", set_a - set_b)

print("Symmetric Difference:", set_a.symmetric_difference(set_b))
print("Symmetric Difference ^:", set_a ^ set_b)


# ------------------------------------------------------------
# UPDATE VARIANTS (IN-PLACE)
# Description: Modify the original set.
# ------------------------------------------------------------
temp = set_a.copy()
temp.update(set_b)
print("After update:", temp)

temp = set_a.copy()
temp.intersection_update(set_b)
print("After intersection_update:", temp)

temp = set_a.copy()
temp.difference_update(set_b)
print("After difference_update:", temp)

temp = set_a.copy()
temp.symmetric_difference_update(set_b)
print("After symmetric_difference_update:", temp)


# ------------------------------------------------------------
# FROZENSET
# Description:
# - Immutable version of a set
# - Unordered, unindexed, no duplicates
# - Cannot be modified after creation
# ------------------------------------------------------------
frozen = frozenset([1, 2, 3, 3])
print("Frozenset:", frozen)

# Type
# - frozenset has its own type
print("Type:", type(frozen))


# ------------------------------------------------------------
# FROZENSET ALLOWED OPERATIONS
# Description:
# - frozenset supports non-mutating set operations
# ------------------------------------------------------------
set_a = {2, 3, 4}

print("Union:", frozen.union(set_a))
print("Intersection:", frozen.intersection(set_a))
print("Difference:", frozen.difference(set_a))
print("Symmetric difference:", frozen.symmetric_difference(set_a))

print("Is subset:", frozen.issubset({1, 2, 3, 4}))
print("Is superset:", frozen.issuperset({1, 2}))
print("Is disjoint:", frozen.isdisjoint({5, 6}))


# ------------------------------------------------------------
# FROZENSET RESTRICTIONS
# Description:
# - No methods that modify data are allowed
# ------------------------------------------------------------
# frozen.add(4)            # ❌ AttributeError
# frozen.remove(1)         # ❌ AttributeError
# frozen.update({5})       # ❌ AttributeError
# frozen.clear()           # ❌ AttributeError


# ------------------------------------------------------------
# SET RELATION METHODS
# Description: Compare relationships between sets.
# ------------------------------------------------------------
set_x = {1, 2}
set_y = {1, 2, 3, 4}

print("Is subset:", set_x.issubset(set_y))
print("Is superset:", set_y.issuperset(set_x))
print("Is disjoint:", set_x.isdisjoint({5, 6}))


# ------------------------------------------------------------
# FULL SET METHODS OVERVIEW
# Description: Demonstration of all major built-in set methods.
# ------------------------------------------------------------
demo = {10, 20, 30}

demo.add(40)
demo.update({50, 60})
demo.remove(10)
demo.discard(999)             # no error
popped = demo.pop()
demo_copy = demo.copy()
demo.clear()

print("Popped item:", popped)
print("Copy after clear:", demo_copy)
print("Demo after clear:", demo)

del demo  # deletes the set
# print(demo)  # ❌ Error: demo is deleted