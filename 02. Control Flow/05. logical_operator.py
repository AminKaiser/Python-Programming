'''
In Python, logical operators are used to combine multiple conditions into a single expression. 
There are three logical operators in Python:

and: This operator returns True if both the conditions are true.
or: This operator returns True if either of the conditions is true.
not: This operator negates the result of the condition.
Here's an example:
'''
x = 5
y = 10

# using "and" operator
if x > 0 and y > 0:
    print("Both x and y are positive numbers.")

# using "or" operator
if x < 0 or y < 0:
    print("At least one of the numbers is negative.")

# using "not" operator
if not x == y:
    print("x is not equal to y.")

'''
In the above example, the and operator is used to check if both x and y are positive numbers, 
the or operator is used to check if at least one of the numbers is negative, 
and the not operator is used to check if x is not equal to y.
'''

'''
In Python, logical operators have the following precedence, in descending order:

not
and
or
This means that the not operator has the highest precedence, followed by and, and then or.

For example, in the expression not x > y and z == 10, the not operator is evaluated first, followed by and, and then ==. The expression is equivalent to (not (x > y)) and (z == 10).

If you want to change the order of evaluation, you can use parentheses to group the expressions. For example, if you want the or operator to be evaluated before the and operator, you can write (x > y) or (z == 10) and (a < b).

Remember, it's always a good idea to use parentheses to make your code more readable and to avoid confusion about the order of evaluation.

Here's an example program that demonstrates how logical operator precedence works in Python:
'''

x = 10
y = 5
z = 3
a = 2
b = 1

result = x > y and z == 3 or a < b

print(result)  # Output: False

'''
In this program, we have five variables x, y, z, a, and b, each assigned a different value. 
We then have a single logical expression that combines these variables using the and, or, and == operators.

According to the operator precedence rules, the and operator has higher precedence than the or operator, 
so x > y and z == 3 is evaluated first. 
This expression evaluates to True and True, which is True.

Next, the or operator is evaluated, which combines the result of the previous expression with the final condition a < b. 
This expression evaluates to True or False, which is True.

Therefore, the final value of the result variable is True.

'''
