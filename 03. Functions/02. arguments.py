def greet(first_name, last_name):
    print(f"Hello {first_name} {last_name}")


greet("Amin", "Kaiser")

'''
In Python, functions can take arguments, which are values passed to the function when it is called. 
Arguments can be used to provide input to the function, and can be used to customize the behavior of the function. 
There are several types of arguments that can be used in Python functions, including:

Positional arguments:
Positional arguments are the most common type of arguments in Python functions. 
They are called "positional" because their position in the argument list determines which parameter they are assigned to. 
For example, in the following function, the first argument (x) is assigned to the 
parameter a, and the second argument (y) is assigned to the parameter b:
'''


def add_numbers(a, b):
    """
    This function takes two numbers as input and returns their sum.
    """
    return a + b


'''
To call this function with positional arguments, 
we simply pass the arguments in the order they are defined in the function definition:
'''
result = add_numbers(2, 3)
print(result)  # Output: 5
