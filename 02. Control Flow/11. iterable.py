'''
In Python, an iterable is any object that can be looped over using a for loop. 
An iterable is an object that defines the __iter__() method or the __getitem__() method. 
These methods return an iterator object that can be used to loop over the elements of the iterable.

Some examples of iterables in Python include lists, tuples, strings, dictionaries, sets, and even files. 
Here are some examples of using for loops to iterate over different types of iterables:

'''
# list
my_list = [1, 2, 3, 4, 5]
for num in my_list:
    print(num)

# tuple
my_tuple = ('apple', 'banana', 'cherry')
for fruit in my_tuple:
    print(fruit)

# string
my_string = 'hello'
for char in my_string:
    print(char)

# dictionary
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
for key, value in my_dict.items():
    print(key, value)

# set
my_set = {1, 2, 3, 4, 5}
for num in my_set:
    print(num)

# file
with open('myfile.txt', 'r') as f:
    for line in f:
        print(line)
