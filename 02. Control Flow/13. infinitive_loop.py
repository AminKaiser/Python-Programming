'''
An infinite loop is a loop that never stops running. 
This can happen when the loop condition is always true, or when there is no condition at all. 
Here are a few examples of infinite loops:

While loop with a true condition:

'''

while True:
    print("This loop will run forever!")

"""
This loop will print "This loop will run forever!" repeatedly without stopping, because the condition True is always true.

While loop with a variable that never changes:

"""

count = 0

while count == 0:
    print("This loop will also run forever!")
