def greet():
    print("Hello")


greet()

'''
In Python, a function is a named block of code that performs a specific task. 
Functions allow you to write reusable code, which can be called from other parts of your program. 
Here's an example of a simple function in Python:
'''


def greet(name):
    """
    This function takes a name as input and prints a greeting message.
    """
    print("Hello, " + name + "!")


'''
In this example, we define a function called greet that takes one parameter called name. 
The code inside the function body prints a greeting message to the console, using the name parameter.

To call the greet function and pass it a name, 
we simply write the function name followed by the argument(s) in parentheses:
'''
greet("Alice")  # Output: "Hello, Alice!"
greet("Bob")    # Output: "Hello, Bob!"

'''
When we call the greet function with the argument "Alice", 
the function prints the message "Hello, Alice!" to the console. 
Similarly, when we call the function with the argument "Bob", it prints "Hello, Bob!".
'''
