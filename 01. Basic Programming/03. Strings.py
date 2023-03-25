course = "Python Programming"
# Length: You can get the length of a string using the len() function.
print(len(course))

'''
Concatenation: You can concatenate (join) two or more strings 
using the + operator. For example:
'''
string1 = "Hello"
string2 = "World"
result = string1 + " " + string2
print(result)

'''
Indexing: You can access individual characters in a string using indexing.
Indexing starts at 0 for the first character and
goes up to n-1 for the nth character. For example:
'''
string = "Hello World"
# for first character
print(string[0])
# To get the last character
print(string[-1])

'''
Slicing: You can extract a substring from a string using slicing.
Slicing is done using the [] operator and specifying the start and
end indices of the substring. For example:
'''
string = "Hello World"
# For specific range [0 - n-1]
print(string[0:5])
print(string[:5])
# From starting to last
print(string[0:])
print(string[:])
