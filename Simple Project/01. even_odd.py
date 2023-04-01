num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")

'''
In this program, the user is prompted to enter a number using the input() function, 
which is then converted to an integer using the int() function and stored in the num variable.

The program then uses a conditional statement to check whether num is even or odd. 
The % operator is used to calculate the remainder of dividing num by 2. 
If the remainder is 0, num is even and the program prints "num is even". Otherwise, 
if the remainder is 1, num is odd and the program prints "num is odd".
'''
