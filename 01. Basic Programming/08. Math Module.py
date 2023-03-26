'''
The Python math module provides a wide range of mathematical functions and constants that you can use in your Python programs.
Before you can use the functions in the math module, you must first import it using the import statement:
'''
import math

'''
Here are some of the most commonly used functions and constants in the math module:

math.pi: This constant represents the value of pi (3.141592653589793).

math.sqrt(x): This function returns the square root of x.

math.pow(x, y): This function returns x raised to the power of y.

math.floor(x): This function returns the largest integer less than or equal to x.

math.ceil(x): This function returns the smallest integer greater than or equal to x.

math.sin(x), math.cos(x), math.tan(x): These functions return the sine, cosine, and tangent of x, respectively.

math.degrees(x): This function converts x from radians to degrees.

math.radians(x): This function converts x from degrees to radians.

math.log(x, base): This function returns the logarithm of x with base base.

'''

import math

# Constants
print(math.pi)  # Output: 3.141592653589793

# Square root
print(math.sqrt(16))  # Output: 4.0

# Power
print(math.pow(2, 3))  # Output: 8.0

# Floor and ceiling
print(math.floor(3.7))  # Output: 3
print(math.ceil(3.2))  # Output: 4

# Trigonometric functions
print(math.sin(math.pi/2))  # Output: 1.0
print(math.cos(math.pi))  # Output: -1.0
print(math.tan(math.pi/4))  # Output: 0.9999999999999999

# Conversion functions
print(math.degrees(math.pi/2))  # Output: 90.0
print(math.radians(180))  # Output: 3.141592653589793

