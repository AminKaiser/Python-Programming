'''
In Python, numbers are a built-in data type that can be used to represent numeric values. There are three main types of numbers in Python:

Integers: Integers are whole numbers, such as -2, -1, 0, 1, 2, etc. In Python 3, integers have no size limit and can be as large as your system's memory allows.

Floats: Floats are real numbers with a decimal point, such as 3.14, -0.5, 1.0, etc. Floats are stored using a fixed amount of memory, which means that they have a limited precision.

Complex numbers: Complex numbers are numbers with a real part and an imaginary part, such as 1+2j, 2-3j, etc.

Python provides various built-in functions and operators that can be used to perform arithmetic operations with numbers. Here are some examples:
'''
# Integers
x = 5
y = -10
print(x + y)  # Output: -5

# Floating-point
a = 3.14
b = 2.5
print(a * b)  # Output: 7.85

# Complex
z = 2 + 3j
print(z.real)  # Output: 2.0
print(z.imag)  # Output: 3.0

# Addition
a = 5
b = 3
c = a + b
print(c)  # output: 8

# Subtraction
a = 5
b = 3
c = a - b
print(c)  # output: 2

# Multiplication
a = 5
b = 3
c = a * b
print(c)  # output: 15

# Division
a = 5
b = 3
c = a / b
print(c)  # output: 1.6666666666666667

# Exponentiation
a = 2
b = 3
c = a ** b
print(c)  # output: 8

# Modulo
a = 5
b = 3
c = a % b
print(c)  # output: 2

# // Floor Division Operation
'''
In Python, the double forward-slash symbol (//) is used as the floor division operator. 
It divides the left operand by the right operand and rounds down to the nearest integer.

Here's an example:
'''
a = 10
b = 3
result = a // b
print(result)   # Output: 3

'''
In the above code, a is divided by b using the floor division operator //. 
Since 3 goes into 10 three times with a remainder of 1, the result is 3.

Note that if both operands are integers, the result will also be an integer.
If one or both operands are floating-point numbers, the result will be a floating-point number after 
the division is performed.

'''

'''
Python also provides built-in functions such as abs(), round(), min(), and max() 
that you can use to perform various operations on numbers.
Here are some examples:
'''
