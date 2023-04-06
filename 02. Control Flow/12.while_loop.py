'''
In Python, a while loop is a control flow statement that allows you to repeatedly execute a block of code as long as a certain condition is true.

Here's the basic syntax of a while loop:

'''
# while condition:
#     # code to execute while the condition is true

'''
The condition is a Boolean expression that is evaluated before each iteration of the loop. 
If the condition is True, then the code block inside the loop is executed. 
This process continues until the condition becomes False.

Here's a simple example of a while loop that counts from 1 to 5:
'''
i = 1
while i <= 5:
    print(i)
    i += 1
'''
In this example, we initialize the variable i to 1. 
We then have a while loop that runs as long as i is less than or equal to 5. 
Inside the loop, we print the value of i, and then increment i by 1. 
This process continues until i becomes greater than 5.
'''
num = int(input("Enter a number: "))
factorial = 1
i = 1

while i <= num:
    factorial *= i
    i += 1

print("The factorial of", num, "is", factorial)

'''
In this example, we ask the user to enter a number using the input() function, and convert the input to an integer using the int() function. 
We then initialize two variables, factorial and i, to 1.

Inside the while loop, we multiply the current value of factorial by i, and then increment i by 1. 
This process continues until i is greater than num. 
The result is that factorial contains the factorial of num.

Finally, we use the print() function to display the result to the user.
'''

# Here's another example of a while loop that checks if a number is prime or not:
num = int(input("Enter a number: "))
is_prime = True
i = 2

while i <= num / 2:
    if num % i == 0:
        is_prime = False
        break
    i += 1

if is_prime:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")

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
