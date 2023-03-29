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
x = 5
y = []
z = bool(x)
w = bool(y)

print("The Boolean value of x is:", z)
print("The Boolean value of y is:", w)

'''
In this example, we define two variables x and y, with the value 5 and an empty list [], respectively.
We then use the bool() function to get the Boolean value of each variable and assign it to the variables z and w.
Finally, we print the Boolean values of x and y using the print() function.
This is because x is a non-zero number and therefore truthy, while y is an empty list and therefore falsy.


'''
