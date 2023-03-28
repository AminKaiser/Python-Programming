'''
In Python, the default input type is a string. 
When you use the input() function to get input from the user,
 the value returned is always a string.

For example:

'''
name = input("What is your name? ")
print("Hello, " + name + "!")

'''
In the above code, even if the user enters a number or any other type of
input, it will be treated as a string.
If you want to perform arithmetic operations on the input as a number,
you'll need to convert the string to a numeric type such as an integer or
a float using the appropriate conversion function (int() or float() or boo()).

For example:
'''
age = int(input("What is your age? "))
print(f"You were born in { 2023 - age}")

'''
Here, we are converting the string input to an integer using the int() function 
so that we can perform subtraction with the current year 2023.
'''

'''
In Python, type conversion is the process of converting a value of one data type to another data type. This is often necessary when performing operations that require a certain data type, or when working with data from different sources.

Python provides several built-in functions for type conversion. Some of the commonly used conversion functions are:

int() : Converts a value to an integer data type
float() : Converts a value to a floating-point data type
str() : Converts a value to a string data type
bool() : Converts a value to a Boolean data type
list() : Converts a value to a list data type
tuple() : Converts a value to a tuple data type
set() : Converts a value to a set data type
dict() : Converts a value to a dictionary data type
Here are some examples of how to use these conversion functions:
'''
# converting a string to an integer
age_str = "25"
age_int = int(age_str)

# converting an integer to a float
weight_int = 70
weight_float = float(weight_int)

# converting a number to a string
price = 9.99
price_str = str(price)

# converting a boolean to an integer
is_adult = True
is_adult_int = int(is_adult)

# converting a list to a set
numbers_list = [1, 2, 3, 2, 1]
numbers_set = set(numbers_list)

# converting a tuple to a list
fruits_tuple = ('apple', 'banana', 'orange')
fruits_list = list(fruits_tuple)

# converting a dictionary to a list
person = {'name': 'John', 'age': 30}
person_list = list(person.items())

'''
It's important to note that not all conversions are possible or sensible.
For example, converting a string that is not a valid number to an integer
will result in a ValueError. 
It's always a good idea to check if a conversion is possible and handle any
exceptions that may arise.

'''