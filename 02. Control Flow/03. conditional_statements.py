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

number = int(input("Enter Your Number : "))
print(type(number))
if number % 2 == 0:
    print(f"{number} is an even number ")
else:
    print(f"{number} is a odd number ")


'''
Here's an example program in Python that uses a conditional statement to 
determine whether a given number is even or odd:
'''

num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")

'''
In this program, the user is prompted to enter a number using the input() function, which is then converted to an integer using the int() function and stored in the num variable.

The program then uses a conditional statement to check whether num is even or odd. 
The % operator is used to calculate the remainder of dividing num by 2. 
If the remainder is 0, num is even and the program prints "num is even". Otherwise, 
if the remainder is 1, num is odd and the program prints "num is odd".
'''
year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "is a leap year")
        else:
            print(year, "is not a leap year")
    else:
        print(year, "is a leap year")
else:
    print(year, "is not a leap year")

'''
In this program, the user is prompted to enter a year using the input() function, 
which is then converted to an integer using the int() function and stored in the year variable.

The program then uses a nested conditional statement to check whether year is a leap year. 
A leap year is a year that is divisible by 4, except for years that are divisible by 100 but not divisible by 400.

The first if statement checks whether year is divisible by 4. 
If it is, the program moves on to the next level of nesting to check whether year is divisible by 100. 
If it is, the program moves on to the next level of nesting to check whether year is divisible by 400. 
If it is, year is a leap year and the program prints "year is a leap year". 
If year is divisible by 100 but not by 400, year is not a leap year and the program prints "year is not a leap year". 
If year is not divisible by 100, but is divisible by 4, year is a leap year and the program prints "year is a leap year". 
If year is not divisible by 4, year is not a leap year and the program prints "year is not a leap year".
'''

year = int(input("Enter a year: "))

if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

'''
In this program, the user is prompted to enter a year using the input() function, 
which is then converted to an integer using the int() function and stored in the year variable.

The program then uses a conditional statement to check whether year is a leap year. 
A leap year is a year that is divisible by 4, except for years that are divisible by 100 but not divisible by 400.

The condition (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0) checks whether year is divisible by 4 and not divisible by 100, 
or if it is divisible by 400. 
If this condition is true, year is a leap year and the program prints "year is a leap year". 
Otherwise, if the condition is false, year is not a leap year and the program prints "year is not a leap year".






'''