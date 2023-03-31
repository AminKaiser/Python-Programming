'''
In Python, you can compare characters using their ASCII values.
The built-in ord() function in Python returns the integer representing the
Unicode code point of the given character.
The following example shows how to compare characters using their ASCII values:

'''
char1 = 'a'
char2 = 'b'

if ord(char1) < ord(char2):
    print(char1, "is less than", char2)
elif ord(char1) > ord(char2):
    print(char1, "is greater than", char2)
else:
    print(char1, "and", char2, "are equal")

'''
In this example, we use the ord() function to get the ASCII value of char1 and char2.
We then use the comparison operators < and > to compare their ASCII values and determine
which character is greater than or less than the other.

Note that this method compares the ASCII values of characters,
which may not always reflect the expected alphabetical order of characters in some languages.
'''

'''
ord() is a built-in Python function that returns the integer representing 
the Unicode character. It takes a string of length 1 as its parameter, 
and returns an integer representing the Unicode code point of the character.

For example
'''
print(ord('a'))
print(ord('A'))
print(ord('0'))
print(ord('$'))

'''
In this example, ord('a') returns 97, which is the Unicode code point of the character 'a'.
Similarly, ord('A') returns 65, which is the Unicode code point of the character 'A'. 
The function can be used in conjunction with comparison operators to compare characters based on 
their ASCII values.

Note that ord() function only works with single-character strings, 
and will raise a TypeError if it is passed a string of length greater than 1.

'''
