'''
n Python, the bool() function is used to convert a value to a Boolean data type. 
Boolean data type represents either True or False values.

The bool() function takes an argument and returns True or False depending on the value of the argument.
Here are some examples:

'''

print(bool(0))     # False
print(bool(1))     # True
print(bool(10))    # True
print(bool(-1))    # True
print(bool(""))    # False
print(bool("Hello"))   # True
print(bool([]))    # False
print(bool([1, 2, 3]))    # True
print(bool(None))  # False
print(bool(False))  # False
print(bool("False"))  # True

'''
In Python, the following values are considered False when converted to a Boolean data type:

False
None
0
0.0
"" (empty string)
[] (empty list)
{} (empty dictionary)
() (empty tuple)
set() (empty set)
All other values are considered True when converted to a Boolean data type.

The bool() function is often used in conditional statements to check if a value is True or False. For example
'''
