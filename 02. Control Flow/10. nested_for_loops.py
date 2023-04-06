'''
In Python, a nested for loop is a loop inside another loop. 
Here's an example of a nested for loop in Python:

'''

for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end=' ')
    print()
'''
In this example, we have a for loop that iterates over the numbers from 1 to 5. 
Inside this loop, we have another for loop that also iterates over the numbers from 1 to 5. 
For each value of i in the outer loop, we print the multiplication table for i by multiplying it with each value of j in the inner loop.

The end=' ' argument in the print function is used to specify that we want to separate each value with a space instead of a newline character.

This output shows the multiplication table from 1 to 5. 
The first row shows the multiplication of 1 with the numbers 1 to 5, the second row shows the multiplication of 2 with the numbers 1 to 5, and so on.
'''

for i in range(3):
    for j in range(3):
        print(f"({i}, {j})")

for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=' ')
    print()

'''
In this example, we have a for loop that iterates over the numbers from 1 to 5. 
Inside this loop, we have another for loop that iterates over the numbers from 1 to i. 
For each value of i in the outer loop, we print a pattern of numbers in increasing order from 1 to i.

The end=' ' argument in the print function is used to specify that we want to separate each value with a space instead of a newline character.
'''
