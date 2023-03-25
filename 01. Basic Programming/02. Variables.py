'''
In Python, you don't need to explicitly declare variables before using them. 
When you assign a value to a variable, Python creates the variable for you.
However, there are some rules that you should follow when naming variables in Python:

1. Variable names must start with a letter or underscore (_), but not with a number.
2. Variable names can only contain letters, numbers, and underscores.
3. Variable names are case sensitive. For example, "myVar" and "myvar" are two different variables.
4. You cannot use reserved keywords as variable names, such as "if," "while," "for," "and," "or," "not," and "else."
5. It's a good practice to use descriptive and meaningful variable names, so it's easy to understand the purpose of the variable.

my_var = 5
myVar = 6
_myvar = 7

1var = 5 # variable name cannot start with a number
my-var = 6 # variable name cannot contain hyphen
if = 7 # variable name cannot be a reserved keyword

'''
student_count = 1000
grade = 3.69
is_passed = True
course_name = "Python Programming"
print(student_count)


'''
In Python, variables are used to store values in memory. 
Unlike other programming languages, Python does not require you to explicitly declare the data type of a variable.
When you assign a value to a variable, Python automatically assigns a data type based on the value.

For example, if you assign a string to a variable, Python will create a string variable. 
Similarly, if you assign an integer to a variable, Python will create an integer variable.
'''
# Assigning a string to a variable
name = "John"

# Assigning an integer to a variable
age = 30

# Assigning a floating-point number to a variable
salary = 1500.50


# You can also assign multiple values to multiple variables in a single line using the following syntax:

x, y, z = "Apple", "Banana", "Cherry"

'''In this case, the value "Apple" is assigned to the variable x, "Banana" is assigned to the variable y, 
and "Cherry" is assigned to the variable z.
'''

# Python variables are dynamic, which means you can reassign a variable to a new value of a different data type. For example:

# Assigning a string to a variable
name = "John"

# Reassigning the variable to an integer
name = 30

print(name)
# In this example, the variable "name" is first assigned a string value of "John". Later, it is reassigned to an integer value of 30.
