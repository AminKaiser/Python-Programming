'''
Escape sequences are special characters that are used to represent certain characters in a string literal.
In Python, escape sequences start with a backslash (\) followed by one or more characters.
Here are some commonly used escape sequences in Python:

\n - Newline character: inserts a new line in the string.
\t - Tab character: inserts a tab in the string.
\\ - Backslash character: inserts a backslash in the string.
\' - Single quote character: inserts a single quote in the string.
\" - Double quote character: inserts a double quote in the string.
Here is an example of using escape sequences in a string:

'''
# Newline
print("Hello\nWorld!")

'''
In the above example, \n is used to insert a new line after "Hello".
You can also use escape sequences in combination with other string 
operations like concatenation, slicing, and formatting. 
Here are some examples:

'''
# Concatenation:
string1 = "Hello"
string2 = "World"
result = string1 + "\n" + string2
print(result)
