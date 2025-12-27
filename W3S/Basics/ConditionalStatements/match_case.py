# ================================
# Python Match Statement
# ================================


# Python Match
# Matches a value against different patterns (similar to switch-case)
day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")


# Default Value
# The underscore (_) acts as a default case if no pattern matches
status = 404

match status:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case _:
        print("Unknown Status")


# Combine Values
# Multiple values can be handled in a single case using |
command = "start"

match command:
    case "start" | "run" | "begin":
        print("Command started")
    case "stop" | "end":
        print("Command stopped")
    case _:
        print("Invalid command")


# If Statements as Guards
# Guards add extra conditions using if inside a case
point = (2, -3)

match point:
    case (x, y) if x > 0 and y > 0:
        print("First quadrant")
    case (x, y) if x < 0 and y > 0:
        print("Second quadrant")
    case (x, y) if x < 0 and y < 0:
        print("Third quadrant")
    case (x, y) if x > 0 and y < 0:
        print("Fourth quadrant")
    case _:
        print("On an axis")