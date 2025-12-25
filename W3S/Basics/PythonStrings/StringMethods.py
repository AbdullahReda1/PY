# 1	    capitalize():   Converts the first character to upper case.
txt = "hi there"
print(txt.capitalize())     #! Output: Hi there

# 2	    casefold():     Converts string into lower case.
txt = "HI THERE"
print(txt.casefold())       #! Output: hi there

# 3	    center():       Returns a centered string.
txt = "here centered string"
print(txt.center(50, '*'))      #! Output: *****************here centered string*****************

# 4	    count():        Returns the number of times a specified value occurs in a string.
txt = "abbcccddddeeeee"
print(txt.count('e'))       #! Output: 5

# 5	    encode():       Returns an encoded version of the string.
txt = "HAPPY"
print(txt.encode())     #! Output: b'HAPPY'
print(txt.encode().hex())     #! Output: 4841505059

# 6    endswith():     Returns true if the string ends with the specified value.
txt = "hello world"
print(txt.endswith("world"))  #! Output: True

# 7    expandtabs():   Sets the tab size of the string.
txt = "H\te\tl\tl\to"
print(txt.expandtabs(4))  #! Output: H   e   l   l   o

# 8    find():         Searches the string for a specified value and returns the position of where it was found.
txt = "hello world"
print(txt.find("world"))  #! Output: 6

# 9    format():       Formats specified values in a string.
txt = "My name is {name} and I am {age} years old."
print(txt.format(name="Alice", age=25))  #! Output: My name is Alice and I am 25 years old.

# 10   format_map():   Formats specified values in a string.
data = {"name": "Alice", "age": 25}
txt = "My name is {name} and I am {age} years old."
print(txt.format_map(data))  #! Output: My name is Alice and I am 25 years old.

# 11   index():        Searches the string for a specified value and returns the position of where it was found.
txt = "hello world"
print(txt.index("world"))  #! Output: 6

# 12   isalnum():      Returns True if all characters in the string are alphanumeric.
txt = "hello123"
print(txt.isalnum())  #! Output: True

# 13   isalpha():      Returns True if all characters in the string are in the alphabet.
txt = "hello"
print(txt.isalpha())  #! Output: True

# 14   isascii():      Returns True if all characters in the string are ascii characters.
txt = "hello"
print(txt.isascii())  #! Output: True

# 15   isdecimal():    Returns True if all characters in the string are decimals.
txt = "12345"
print(txt.isdecimal())  #! Output: True

# 16   isdigit():      Returns True if all characters in the string are digits.
txt = "12345"
print(txt.isdigit())  #! Output: True

# 17   isidentifier(): Returns True if the string is an identifier.
txt = "variable_name"
print(txt.isidentifier())  #! Output: True

# 18   islower():      Returns True if all characters in the string are lower case.
txt = "hello"
print(txt.islower())  #! Output: True

# 19   isnumeric():    Returns True if all characters in the string are numeric.
txt = "12345"
print(txt.isnumeric())  #! Output: True

# 20   isprintable():  Returns True if all characters in the string are printable.
txt = "hello world"
print(txt.isprintable())  #! Output: True

# 21   isspace():      Returns True if all characters in the string are whitespaces.
txt = "   "
print(txt.isspace())  #! Output: True

# 22   istitle():      Returns True if the string follows the rules of a title.
txt = "Hello World"
print(txt.istitle())  #! Output: True

# 23   isupper():      Returns True if all characters in the string are upper case.
txt = "HELLO"
print(txt.isupper())  #! Output: True

# 24   join():         Joins the elements of an iterable to the end of the string.
my_list = ["apple", "banana", "cherry"]
print(", ".join(my_list))  #! Output: apple, banana, cherry

# 25   ljust():        Returns a left justified version of the string.
txt = "hello"
print(txt.ljust(10, "-"))  #! Output: hello-----

# 26   lower():        Converts a string into lower case.
txt = "HELLO"
print(txt.lower())  #! Output: hello

# 27   lstrip():       Returns a left trim version of the string.
txt = "   hello"
print(txt.lstrip())  #! Output: hello

# 28   maketrans():    Returns a translation table to be used in translations.
trans = str.maketrans("abc", "123")
txt = "abc"
print(txt.translate(trans))  #! Output: 123

# 29   partition():    Returns a tuple where the string is parted into three parts.
txt = "hello world"
print(txt.partition("world"))  #! Output: ('hello ', 'world', '')

# 30   replace():      Returns a string where a specified value is replaced with a specified value.
txt = "I like apples"
print(txt.replace("apples", "bananas"))  #! Output: I like bananas

# 31   rfind():        Searches the string for a specified value and returns the last position of where it was found.
txt = "hello world world"
print(txt.rfind("world"))  #! Output: 12

# 32   rindex():       Searches the string for a specified value and returns the last position of where it was found.
txt = "hello world world"
print(txt.rindex("world"))  #! Output: 12

# 33   rjust():        Returns a right justified version of the string.
txt = "hello"
print(txt.rjust(10, "-"))  #! Output: -----hello

# 34   rpartition():   Returns a tuple where the string is parted into three parts.
txt = "hello world world"
print(txt.rpartition("world"))  #! Output: ('hello world ', 'world', '')

# 35   rsplit():       Splits the string at the specified separator, and returns a list.
txt = "apple, banana, cherry"
print(txt.rsplit(", "))  #! Output: ['apple', 'banana', 'cherry']

# 36   rstrip():       Returns a right trim version of the string.
txt = "hello   "
print(txt.rstrip())  #! Output: hello

# 37   split():        Splits the string at the specified separator, and returns a list.
txt = "apple, banana, cherry"
print(txt.split(", "))  #! Output: ['apple', 'banana', 'cherry']

# 38   splitlines():   Splits the string at line breaks and returns a list.
txt = "hello\nworld"
print(txt.splitlines())  #! Output: ['hello', 'world']

# 39   startswith():   Returns true if the string starts with the specified value.
txt = "hello world"
print(txt.startswith("hello"))  #! Output: True

# 40   strip():        Returns a trimmed version of the string.
txt = "   hello   "
print(txt.strip())  #! Output: hello

# 41   swapcase():     Swaps cases, lower case becomes upper case and vice versa.
txt = "Hello World"
print(txt.swapcase())  #! Output: hELLO wORLD

# 42   title():        Converts the first character of each word to upper case.
txt = "hello world"
print(txt.title())  #! Output: Hello World

# 43   translate():    Returns a translated string.
trans = str.maketrans("abc", "123")
txt = "abc"
print(txt.translate(trans))  #! Output: 123

# 44   upper():        Converts a string into upper case.
txt = "hello"
print(txt.upper())  #! Output: HELLO

# 45   zfill():        Fills the string with a specified number of 0 values at the beginning.
txt = "42"
print(txt.zfill(5))  #! Output: 00042