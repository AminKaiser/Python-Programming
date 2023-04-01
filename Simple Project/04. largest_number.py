'''
Here's an example program in Python that uses a conditional statement to determine the largest of three numbers:
'''
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print("The largest number is", largest)

'''
In this program, the user is prompted to enter three numbers using the input() function, which are then converted to float using the float() function and stored in the variables num1, num2, and num3.

The program then uses a conditional statement to determine the largest of the three numbers. 
The first if statement checks whether num1 is greater than or equal to both num2 and num3. 
If it is, the largest variable is set to num1. 
If not, the program moves on to the next elif statement, which checks whether num2 is greater than or equal to both num1 and num3. 
If it is, the largest variable is set to num2. 
Otherwise, the else statement sets the largest variable to num3.

Finally, the program prints out the largest number using the print() function.
'''
