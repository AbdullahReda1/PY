# ================================
# Python While Loop
# ================================


# The while Loop
# Repeats a block of code as long as the condition is True
count = 0

while count < 5:
    print("Count:", count)
    count += 1


# The break Statement
# Exits the loop immediately when a condition is met
number = 0

while number < 10:
    if number == 5:
        break
    print("Number:", number)
    number += 1


# The continue Statement
# Skips the current iteration and continues with the next one
i = 0

while i < 5:
    i += 1
    if i == 3:
        continue
    print("i:", i)


# The else Statement
# Executes after the loop ends normally (not stopped by break)
x = 0

while x < 3:
    print("x:", x)
    x += 1
else:
    print("Loop finished successfully")


# Nested while Loops
# A while loop inside another while loop
outer = 1
while outer <= 2:
    inner = 1
    while inner <= 3:
        print("Outer:", outer, "Inner:", inner)
        inner += 1
    outer += 1


# Infinite Loop
# A loop that runs forever unless stopped
# Uncomment the following lines to see it in action
# while True:
#     print("This will run forever")