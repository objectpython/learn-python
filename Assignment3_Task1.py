#Module 4: Functions & Modules in Python
#Task 1: Calculate Factorial Using a Function

'''
To Do:
Problem Statement: Write a Python program that:
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.

'''

def factorialRecursion(n: int):
    if n < 2:
        return 1
    else:
        return n * factorialRecursion(n-1)


def factorialLoop(n: int):
    fact = 1
    if n < 2:
        return fact
    else:
        while n >= 2:
            fact = fact * n
            n = n-1

    return fact


n = int(input("Enter a number : "))

print(f"Recursion way: factorial of {n} is ", factorialRecursion(n))

print(f"Loop way:  factorial of {n} is ", factorialLoop(n))
