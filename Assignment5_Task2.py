#Module 6: Data Structures and Strings in Python

#Task 2: Demonstrate List Slicing

'''
To Do:
Problem Statement: Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list


'''

numbers = [i for i in range(1,11)]

print("Original list: ", numbers)
print("Extracted first five elements: ",numbers[0:5])
extracted_list = numbers[0:5]
extracted_list.reverse()
print("Reversed extracted elements : ",extracted_list)