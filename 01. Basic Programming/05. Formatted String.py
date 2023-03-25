'''
In Python, formatted strings (also known as f-strings) are a convenient way to 
embed expressions inside string literals. 
Formatted strings are prefixed with the letter "f" or "F" 
and contain expressions inside curly braces {}. 
The expressions are evaluated at runtime and 
the result is inserted into the string.

Here is an example of a formatted string:

'''
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")

'''
In the above example, the expressions {name} and {age} 
are evaluated and the values are inserted into the string.

You can also use expressions inside the curly braces. 
For example, you can perform arithmetic operations or call functions:
'''
x = 5
y = 7
print(f"The sum of {x} and {y} is {x+y}.")

student_name = "Amin Kaiser"
age = 25

print(f"Student Name is {student_name} and he is {age - 1} years old")
