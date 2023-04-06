'''
In this example, we ask the user to enter a number using the input() function, 
and convert the input to an integer using the int() function. 
We then initialize two variables, is_prime and i, to True and 2, respectively.

Inside the while loop, we check if num is divisible by i. 
If it is, we set is_prime to False and exit the loop using the break statement. 
If num is not divisible by i, we increment i by 1 and continue with the next iteration of the loop.

Finally, we use an if statement to check the value of is_prime. 
If it is True, we print a message saying that num is a prime number.
Otherwise, we print a message saying that num is not a prime number.

'''
import math
num = int(input("Enter a number: "))

# A number is prime if it is greater than 1 and has no positive divisors other than 1 and itself
if num > 1:
    # Check for factors up to the square root of the number
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")

'''
In this program, we ask the user to enter a number using the input() function, 
and convert the input to an integer using the int() function.

We then use an if statement to check if num is greater than 1, 
since prime numbers are defined as integers greater than 1. 
If num is greater than 1, we use a for loop to check if it has any factors other than 1 and itself. We only need to check factors up to the square root of num, since any factor larger than the square root will have a corresponding factor smaller than the square root. If we find a factor, we print a message saying that num is not a prime number and exit the loop using the break statement. If we don't find any factors, we print a message saying that num is a prime number.

If num is not greater than 1, we print a message saying that it is not a prime number.

For example, if the user enters 7, the output of the program will be:

'''

num = int(input("Enter a number: "))

# A number is prime if it is greater than 1 and has no positive divisors other than 1 and itself
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")

'''
In this program, we ask the user to enter a number using the input() function, 
and convert the input to an integer using the int() function.

We then use an if statement to check if num is greater than 1, 
since prime numbers are defined as integers greater than 1. 
If num is greater than 1, we use a for loop to check if it has any factors other than 1 and itself.
We iterate over a range of numbers from 2 to num - 1, and check if num is divisible by each number. 
If we find a factor, we print a message saying that num is not a prime number and exit the loop using the break statement. 
If we don't find any factors, we print a message saying that num is a prime number.

If num is not greater than 1, we print a message saying that it is not a prime number.

'''
# example program in Python to check if a number is prime or not using the square root optimization:


num = int(input("Enter a number: "))

# A number is prime if it is greater than 1 and has no positive divisors other than 1 and itself
if num > 1:
    # Check for factors up to the square root of the number
    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")

'''
In this program, we first import the math module to use the isqrt() function, which returns the integer square root of a number.

We then ask the user to enter a number using the input() function, and convert the input to an integer using the int() function.

We then use an if statement to check if num is greater than 1, since prime numbers are defined as integers greater than 1. If num is greater than 1, we use a for loop to check if it has any factors other than 1 and itself. We only need to check factors up to the square root of num, since any factor larger than the square root will have a corresponding factor smaller than the square root. We use the math.isqrt() function to compute the square root of num and convert it to an integer using the int() function. If we find a factor, we print a message saying that num is not a prime number and exit the loop using the break statement. If we don't find any factors, we print a message saying that num is a prime number.

If num is not greater than 1, we print a message saying that it is not a prime number.

'''
