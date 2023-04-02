'''
In Python, a for loop is used to iterate over a sequence of elements, such as a list, tuple, or string. The basic syntax of a for loop in Python is as follows:
'''
# for variable in sequence:
# code to be executed for each element in the sequence

'''
In this syntax, variable is a variable that takes on the value of each element in the sequence during each iteration of the loop. 
The code block inside the loop is executed once for each element in the sequence, with variable taking on the value of each element in turn.
'''
'''
In Python, the built-in range() function is commonly used in conjunction with for loops to iterate over a sequence of numbers. The range() function returns an immutable sequence of numbers, starting from 0 by default, and increments by 1 by default.

The basic syntax of range() function is as follows:
'''
for num in range(5):
    print(num)

for number in range(1, 5):
    print("Attempting", number, number * ".")

'''
In this example, we use the range() function with a single argument of 5, which returns a sequence of numbers from 0 to 4. 
During each iteration of the loop, the variable num takes on the value of each number in turn, and the code inside the loop (in this case, a print() statement) is executed.
'''
'''
Here's another example that demonstrates using range() with a for loop to iterate over a sequence of even numbers:
'''
print("*" * 20)
for num in range(0, 10, 2):
    print(num)

'''
In this example, we use the range() function with three arguments: 0 specifies the lower limit of the sequence, 10 specifies the upper limit of the sequence (not included), and 2 specifies the step size of the sequence. 
This returns a sequence of even numbers from 0 to 8. During each iteration of the loop, 
the variable num takes on the value of each even number in turn, and the code inside the loop (in this case, a print() statement) is executed.
'''
'''
These examples demonstrate how the range() function can be used with for loops in Python to iterate over a sequence of numbers, and how different arguments can be used to customize the range of numbers and the step size of the sequence.
'''
