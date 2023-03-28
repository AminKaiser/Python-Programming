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
