'''
In Python, operator precedence determines the order in which operators are evaluated in an expression. The table below shows the order of precedence from highest to lowest:

Precedence	Operator	Description
1	**	Exponentiation
2	+x, -x	Positive, negative
3	*, /, //, %	Multiplication, division, floor division, modulo
4	+, -	Addition, subtraction
5	<, <=, >, >=	Comparison operators
6	==, !=	Equality, inequality
7	not	Logical NOT
8	and	Logical AND
9	or	Logical OR
Operators with higher precedence are evaluated before those with lower precedence. For example, in the expression 3 + 4 * 5, the multiplication is evaluated first because it has a higher precedence than addition, and the result is 23.

However, you can use parentheses () to override the default precedence and control the order of evaluation. For example, (3 + 4) * 5 evaluates to 35, because the addition inside the parentheses is evaluated first.

It's always a good practice to use parentheses in complex expressions to avoid confusion and ensure the intended order of evaluation.

'''

# example program to demonstrate operator precedence in Python

x = 10
y = 5

result = (x + y) * 2 / (x - y) ** 2

print("Result:", result)

'''
In this program, we have two variables x and y assigned the values 10 and 5, respectively. We then use these variables to calculate the value of result.

The expression (x + y) * 2 is evaluated first, because parentheses have the highest precedence. This results in the value 30.

Next, we have the division operator /, which has a higher precedence than multiplication, so the expression 30 / (x - y) ** 2 is evaluated next.

Finally, we have the exponentiation operator **, which has the highest precedence of all operators. The expression (x - y) ** 2 evaluates to 25.

Substituting the values back into the original expression, we get:

result = 30 / 25
result = 1.2


This program demonstrates how operator precedence works in Python and how it can affect the outcome of an expression.
'''

x = 5
y = 3

result = x + y * 2 ** 3 - 4 // 2

print(result)  # Output: 16

'''
In this example, we have defined two variables x and y with values 5 and 3, respectively. We then use these variables to perform a series of operations and store the result in the variable result.

According to the operator precedence rules in Python, the exponentiation operator ** has the highest precedence, followed by multiplication * and floor division //, then addition + and subtraction -.

So, the expression is evaluated in the following order:

2 ** 3 is evaluated first, resulting in 8.
y * 8 is evaluated next, resulting in 24.
4 // 2 is evaluated next, resulting in 2.
x + 24 - 2 is evaluated last, resulting in 16.
Therefore, the final value of result is 16.

This example demonstrates how operator precedence works in Python and how it can affect the outcome of an expression. It's important to keep the operator precedence in mind when writing complex expressions to ensure that the program behaves as intended.


'''
