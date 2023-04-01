'''
Here's an example program in Python that uses a conditional statement 
to determine the letter grade for a given score:
'''
score = int(input("Enter your score: "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Your grade is", grade)

'''
In this program, the user is prompted to enter a score using the input() function, 
which is then converted to an integer using the int() function and stored in the score variable.

The program then uses a conditional statement to determine the letter grade for the given score. 
The first if statement checks whether score is greater than or equal to 90. 
If it is, the grade variable is set to "A". 
If not, the program moves on to the next elif statement, which checks whether score is greater than or equal to 80. 
If it is, the grade variable is set to "B". This process repeats for the remaining elif statements, with each statement checking a lower score range than the previous statement. 
If none of the if or elif statements are true, the else statement sets the grade variable to "F".

Finally, the program prints out the resulting letter grade using the print() function.

'''