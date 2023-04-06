'''
The for...else loop in Python is used to execute a block of code 
when the loop has finished iterating over all the items in a sequence. 
The else block will be executed if the loop completes all iterations without encountering a break statement.

Here's the basic syntax of a for...else loop in Python:

'''
# for variable in sequence:
#     # code to be executed inside the loop
#     if condition:
#         # code to be executed if condition is true
#         break
# else:
#     # code to be executed if the loop completes all iterations without encountering a 'break' statement

'''
In this syntax, variable is a variable that represents the current item being processed
in the loop, and sequence is the sequence of items to iterate over.

When the loop is executed, each item in the sequence is assigned to the variable, and the code inside the loop is executed. 
If the condition is true, the loop is terminated using the break statement. 
If the loop completes all iterations without encountering a break statement, the else block is executed.

Here's an example of using for...else loop in Python:

'''
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 6:
        print("Number found in list!")
        break
else:
    print("Number not found in list.")

'''
In this example, we are iterating over a list of numbers. 
If the number 6 is found in the list, we print a message and break out of the loop. 
Otherwise, if the loop completes all iterations without finding the number 6, 
    we print a message indicating that the number was not found.
'''

fruits = ['apple', 'banana', 'orange', 'kiwi']

for fruit in fruits:
    if 'a' not in fruit:
        print(fruit)
else:
    print("All fruits have the letter 'a'.")

'''
In this example, we are iterating over a list of fruits. For each fruit, 
we check if the letter 'a' is not present in it. 
If a fruit is found that does not contain the letter 'a', we print its name. 
If all fruits in the list have the letter 'a', we print a message indicating that all fruits have the letter 'a'.
'''

fruits = ['apple', 'banana', 'cherry', 'kiwi']

for fruit in fruits:
    if 'p' in fruit:
        print(fruit)
        break
else:
    print('No fruits with "p" found')
'''
In this example, we have a list of fruits and we are searching for the first fruit that contains the letter 'p'. 
We use a for loop to iterate through the list, and if we find a fruit with 'p', we print it and break out of the loop.

However, if we reach the end of the loop without finding any fruits with 'p', 
the else block is executed and we print a message indicating that no fruits with 'p' were found.

'''
numbers = [2, 4, 6, 8, 10]

for num in numbers:
    if num % 2 == 1:
        print('Odd number found')
        break
else:
    print('No odd numbers found')

"""
In this example, we have a list of even numbers and we are checking if there are any odd numbers in the list. We use a for loop to iterate through the list, and if we find an odd number, we print a message and break out of the loop.

However, if we reach the end of the loop without finding any odd numbers, the else block is executed and we print a message indicating that no odd numbers were found.
"""
