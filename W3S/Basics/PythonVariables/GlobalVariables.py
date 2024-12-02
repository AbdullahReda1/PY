# Global variables without `global` keyword
x = "global one"
y = "global two"

def my_func():
    x = "local one"
    # Global variable using `global` keyword
    global y
    y = "locally global two"
    print("this is " + x)
    print("this is " + y)
    

my_func()

print("this is " + x)
print("this is " + y)