#Module 4: Functions & Modules in Python
#Task 2: Using the Math Module for Calculations

'''
To Do:
Problem Statement: Write a Python program that:
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
o   Square root of the number
o   Natural logarithm (log base e) of the number
o   Sine of the number (in radians)
3.   Displays the calculated results.
'''

import math

n=int(input("Enter a number: "))

print(f"Square root : ",math.sqrt(n))
print(f"Logarithm : ",math.log(n))
print(f"Sine : ",math.sin(n))