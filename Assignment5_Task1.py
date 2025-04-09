#Module 6: Data Structures and Strings in Python

#Task 1: Create a Dictionary of Student Marks

'''
To Do:
Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.

'''

students = {
    'Mick': 91,
    'Ria': 88,
    'Alice': 85
}

student = input("Enter the student's name: ")
if student in students:
    print(f"{student}'s marks: {students[student]}" )
else:
    print("Student not found.")