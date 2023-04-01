'''
Here's an example program in Python that uses a conditional statement to determine whether a given number is positive, negative, or zero:
'''

num = float(input("Enter a number: "))

if num > 0:
    print(num, "is positive")
elif num < 0:
    print(num, "is negative")
else:
    print(num, "is zero")

'''
In this program, the user is prompted to enter a number using the input() function, which is then converted to a float using the float() function and stored in the num variable.

The program then uses a conditional statement to determine whether num is positive, negative, or zero. 
The first if statement checks whether num is greater than 0. 
If it is, the program prints out that num is positive using the print() function. 
If num is not greater than 0, the program moves on to the next elif statement, which checks whether num is less than 0. 
If it is, the program prints out that num is negative using the print() function. 
If num is not less than 0, the program moves on to the final else statement, which prints out that num is zero using the print() function.

This program can be useful in various situations where you need to determine the sign of a given number.
'''