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

# year = int(input("Enter a year: "))

# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print(year, "is a leap year")
# else:
#     print(year, "is not a leap year")
