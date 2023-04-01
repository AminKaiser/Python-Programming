'''
In Python, a conditional statement is created using the if keyword,
followed by a condition that is evaluated, and optionally, 
one or more elif (short for "else if") statements and an else statement. 
The basic syntax for a conditional statement in Python is:

'''

# if condition1:
# code to be executed if the condition is true
# elif condition2:
# code to be executed if condition1 is false and condition2 is true
# else:
# code to be executed if both condition1 and condition2 are false

'''
Here's an example of a Python conditional statement that checks 
whether a number is positive, negative, or zero:
'''
num = 10

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

'''
In this example, the program checks whether the value of num is greater than zero. 
If it is, the program prints "The number is positive.
" If num is less than zero, the program prints "The number is negative.
" If num is equal to zero, the program prints "The number is zero."
'''

age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age")
elif age <= 12:
    print("You are a child")
elif age <= 19:
    print("You are a teenager")
elif age <= 59:
    print("You are an adult")
else:
    print("You are a senior citizen")

'''
In this program, the user's age is obtained using the input() function and 
stored in the age variable as an integer using the int() function. 
The program then checks the value of age using a series of elif statements to determine 
which age group the user falls into.

If age is less than 0, the program prints "Invalid age". 
If age is between 0 and 12 (inclusive), the program prints "You are a child". 
If age is between 13 and 19 (inclusive), the program prints "You are a teenager". 
If age is between 20 and 59 (inclusive), the program prints "You are an adult". 
If age is greater than 59, the program prints "You are a senior citizen".
'''
