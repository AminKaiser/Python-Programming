'''
Python provides a rich set of string methods that you can use to manipulate strings. 
Here are some of the most commonly used string methods in Python:

len(string) - Returns the length of the string.

string.lower() - Converts all uppercase characters in the string to lowercase.

string.upper() - Converts all lowercase characters in the string to uppercase.

string.strip() - Removes any whitespace characters (spaces, tabs, newlines) from the beginning and end of the string.

string.startswith(substring) - Returns True if the string starts with the specified substring, otherwise False.

string.endswith(substring) - Returns True if the string ends with the specified substring, otherwise False.

string.find(substring) - Returns the index of the first occurrence of substring in the string, or -1 if substring is not found.

string.replace(old, new) - Replaces all occurrences of old in the string with new.

string.split(separator) - Splits the string into a list of substrings using separator as the delimiter.

string.join(iterable) - Joins the elements of iterable (such as a list) into a string using string as the separator.

Here is an example that demonstrates the use of some of these string methods:
'''

string = "  Hello, World!  "
print(len(string))         # output: 17
print(string.lower())      # output:   hello, world!
print(string.upper())      # output:   HELLO, WORLD!
print(string.strip())      # output: Hello, World!
print(string.startswith("Hello"))    # output: True
print(string.endswith("!"))          # output: True
print(string.find("World"))          # output: 8
print(string.replace("Hello", "Hi"))  # output:   Hi, World!
print(string.split(","))             # output: ['  Hello', ' World!  ']
print("-".join(["apple", "banana", "cherry"]))  # output: apple-banana-cherry


# Extra
name = "amin kaiser"
print(name.title())
print("amin" in name)
print("kaiser" not in name)

name = "    Amin Kaiser  "
print(name.strip())
print(name.lstrip())
print(name.rstrip())
