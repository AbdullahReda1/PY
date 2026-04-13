# ==========================================
# Python JSON
# ==========================================


# ------------------------------------------------
# What is JSON?
# JSON (JavaScript Object Notation) is a lightweight
# data format used for storing and exchanging data
# ------------------------------------------------


# ------------------------------------------------
# Import JSON Module
# ------------------------------------------------
import json


# ------------------------------------------------
# Convert Python → JSON (json.dumps)
# dumps() converts Python object into JSON string
# ------------------------------------------------
data = {
    "name": "Abdullah",
    "age": 25,
    "is_student": False
}

json_string = json.dumps(data)
print("JSON string:", json_string)


# ------------------------------------------------
# Convert JSON → Python (json.loads)
# loads() parses JSON string into Python object
# ------------------------------------------------
parsed_data = json.loads(json_string)
print("Parsed data:", parsed_data)
print("Type:", type(parsed_data))


# ------------------------------------------------
# Python → JSON Type Mapping
# dict  → object
# list  → array
# str   → string
# int   → number
# float → number
# bool  → true/false
# None  → null
# ------------------------------------------------


# ------------------------------------------------
# Pretty Printing (indent)
# Makes JSON easier to read
# ------------------------------------------------
pretty = json.dumps(data, indent=4)
print(pretty)


# ------------------------------------------------
# Sorting Keys
# ------------------------------------------------
sorted_json = json.dumps(data, indent=4, sort_keys=True)
print(sorted_json)


# ------------------------------------------------
# Writing JSON to File (dump)
# dump() writes JSON to a file
# ------------------------------------------------
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)


# ------------------------------------------------
# Reading JSON from File (load)
# load() reads JSON from a file
# ------------------------------------------------
with open("data.json", "r") as file:
    file_data = json.load(file)

print("Data from file:", file_data)


# ------------------------------------------------
# Custom Serialization
# Convert unsupported types manually
# ------------------------------------------------
import datetime

def convert(obj):
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()

data_with_time = {
    "name": "Ali",
    "time": datetime.datetime.now()
}

json_string = json.dumps(data_with_time, default=convert)
print(json_string)


# ------------------------------------------------
# Handling Errors
# Catch invalid JSON format
# ------------------------------------------------
invalid_json = '{"name": "Ali", age: 25}'  # missing quotes

try:
    json.loads(invalid_json)
except json.JSONDecodeError:
    print("Invalid JSON format")


# ------------------------------------------------
# When to Use JSON
# - APIs (REST communication)
# - Configuration files
# - Data storage and exchange
# ------------------------------------------------