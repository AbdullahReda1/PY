# ============================================================
# PYTHON DICTIONARIES
# ============================================================
# Characteristics:
# - Ordered (Python 3.7+)
# - Mutable
# - No duplicate keys
# - Key-value pairs
# ============================================================


# ------------------------------------------------------------
# WHAT IS A DICTIONARY?
# Description: Stores data as key-value pairs.
# ------------------------------------------------------------
person = {
    "name": "Abdullah",
    "age": 25,
    "is_engineer": True
}
print("Original dictionary:", person)


# ------------------------------------------------------------
# DICTIONARY TYPE
# ------------------------------------------------------------
print("Type:", type(person))


# ------------------------------------------------------------
# DICTIONARY LENGTH
# Description: len() returns number of key-value pairs.
# ------------------------------------------------------------
print("Dictionary length:", len(person))


# ------------------------------------------------------------
# ACCESS ITEMS
# Description: Access values using keys or get().
# ------------------------------------------------------------
print("Name:", person["name"])
print("Age:", person.get("age"))


# ------------------------------------------------------------
# ACCESS KEYS, VALUES, ITEMS
# Description: keys(), values(), items().
# ------------------------------------------------------------
print("Keys:", person.keys())
print("Values:", person.values())
print("Items:", person.items())


# ------------------------------------------------------------
# CHECK IF KEY EXISTS
# Description: Use `in` keyword.
# ------------------------------------------------------------
if "age" in person:
    print("Age key exists")


# ------------------------------------------------------------
# CHANGE ITEMS
# Description: Assign new values using keys.
# ------------------------------------------------------------
person["age"] = 26
print("After age update:", person)


# ------------------------------------------------------------
# ADD ITEMS
# Description: Add new key-value pairs.
# ------------------------------------------------------------
person["country"] = "Egypt"
print("After adding country:", person)


# ------------------------------------------------------------
# UPDATE DICTIONARY
# Description: update() modifies or adds items.
# ------------------------------------------------------------
person.update({"age": 27, "city": "Cairo"})
print("After update:", person)


# ------------------------------------------------------------
# REMOVE ITEMS
# Description:
# - pop(key)
# - popitem()
# - del
# - clear()
# ------------------------------------------------------------
removed_age = person.pop("age")
print("Removed age:", removed_age)

last_item = person.popitem()   # Removes last inserted item
print("Removed last item:", last_item)

del person["is_engineer"]
print("After del:", person)

temp_dict = {"a": 1, "b": 2}
temp_dict.clear()
print("Cleared dictionary:", temp_dict)


# ------------------------------------------------------------
# LOOP DICTIONARIES
# Description: Loop through keys, values, or key-value pairs.
# ------------------------------------------------------------
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1969
}

print("Loop keys:")
for key in car:
    print(key)

print("Loop values:")
for value in car.values():
    print(value)

print("Loop items:")
for key, value in car.items():
    print(key, ":", value)


# ------------------------------------------------------------
# NESTED DICTIONARIES
# Description: Dictionaries inside dictionaries.
# ------------------------------------------------------------
family = {
    "child1": {
        "name": "Ali",
        "age": 12
    },
    "child2": {
        "name": "Sara",
        "age": 10
    }
}
print("Nested dictionary:", family)


# ------------------------------------------------------------
# LOOP INTO NESTED DICTIONARY
# Description: Access inner dictionaries using nested loops.
# ------------------------------------------------------------
for child, info in family.items():
    print(child)
    for key, value in info.items():
        print(" ", key, ":", value)


# ------------------------------------------------------------
# COPY DICTIONARIES
# Description: Use copy() or dict().
# ------------------------------------------------------------
copy_a = car.copy()
copy_b = dict(car)
print("Copied dictionaries:", copy_a, copy_b)


# ------------------------------------------------------------
# DICTIONARY CONSTRUCTOR
# Description: Create dictionaries using dict().
# ------------------------------------------------------------
person2 = dict(name="Ahmed", age=30, country="Egypt")
print("Constructed dictionary:", person2)


# ------------------------------------------------------------
# fromkeys()
# Description: Create dictionary from keys with a single value.
# ------------------------------------------------------------
keys = ("a", "b", "c")
default_dict = dict.fromkeys(keys, 0)
print("fromkeys result:", default_dict)


# ------------------------------------------------------------
# DICTIONARY METHODS — FULL OVERVIEW
# Description: Demonstration of major dictionary methods.
# ------------------------------------------------------------
demo = {"x": 1, "y": 2}

demo.get("x")
demo.keys()
demo.values()
demo.items()
demo.update({"z": 3})
demo.setdefault("w", 100)
demo.pop("y")
demo.copy()
demo.clear()

print("Dictionary methods demo:", demo)

del demo
# print(demo)  # This would raise an error since demo is deleted