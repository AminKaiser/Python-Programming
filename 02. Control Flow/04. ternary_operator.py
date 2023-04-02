'''
In Python, the ternary operator allows you to write a conditional expression 
in a single line of code. The syntax for the ternary operator is:

'''
# value_if_true if condition else value_if_false

x = 5
y = 10

max_value = x if x > y else y

print(max_value)  # Output: 10

'''
n this example, the condition is x > y. If this condition is true, then the value of x is assigned to max_value. 
Otherwise, the value of y is assigned to max_value.
This is also sometimes called the "conditional expression".
'''

number = int(input("Enter Your Number : "))
print(type(number))
if number % 2 == 0:
    print(f"{number} is an even number ")
else:
    print(f"{number} is a odd number ")

# Equvalent Ternary Expression

num = int(input("Enter Your Number Please :"))
message = "Even" if num % 2 == 0 else "Odd"
print(message)

age = 20

is_adult = True if age >= 18 else False

print(is_adult)  # Output: True
'''
In this example, the condition is age >= 18. 
If this condition is true (which it is, because age is 20), then the value True is assigned to is_adult.
Otherwise, the value False is assigned to is_adult. 
The end result is that is_adult is True, since age is greater than or equal to 18.
'''
