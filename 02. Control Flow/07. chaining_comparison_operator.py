'''
In Python, you can chain comparison operators to form more complex conditions using the and and or operators.

Here's an example of how to chain comparison operators in Python:

'''
x = 5
y = 10

# if (x < y) and (y <= 15)
if x < y <= 15:
    print("x is less than y and y is less than or equal to 15")
else:
    print("Condition not satisfied")

'''
In this example, we define two variables x and y with values 5 and 10, respectively.
We then use the < and <= operators to chain the comparison conditions and check if x is less than y and if y is less than or equal to 15.

The expression x < y <= 15 is equivalent to (x < y) and (y <= 15). 
If both conditions are true, the if statement is executed and the output is x is less than y and y is less than or equal to 15. 
If either of the conditions is false, the else statement is executed and the output is Condition not satisfied.

Chaining comparison operators can make your code more concise and readable, 
especially when dealing with multiple conditions. 
However, it's important to use parentheses to explicitly group the conditions and ensure the intended order of evaluation.

'''

age = 25

# if (18 <= age) and (age < 65)
if 18 <= age < 65:
    print("You are of working age")
else:
    print("You are not of working age")

'''
In this example, we define a variable age with a value of 25. We then use the <= and < operators to chain the comparison conditions and check if age is greater than or equal to 18 and less than 65.

The expression 18 <= age < 65 is equivalent to (18 <= age) and (age < 65). If both conditions are true, the if statement is executed and the output is You are of working age. If either of the conditions is false, the else statement is executed and the output is You are not of working age.

In this case, the output of the program is You are of working age, since age is greater than or equal to 18 and less than 65.

This example demonstrates how chaining comparison operators can be used to check if a value meets multiple conditions, such as age requirements or other criteria, and can make your code more readable and concise.
'''
