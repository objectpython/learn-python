#Module 5: Files, Exceptions, and Errors in Python

#Task 1: Read a File and Handle Errors

'''
To Do:
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.

'''
#Method 1
print("Method 1: Reading file and manually closing it in finally block")
try:
    read_file = open("sample.txt",'r')
    line_num = 1
    while True:
        line = read_file.readline()
        if not line:
            break
        print(f"line {line_num}: {line.strip()}")
        line_num += 1
except FileNotFoundError as fnf:
    print("Error: The file 'sample.txt' was not found")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    read_file.close()



#Method 2 using with

print("\nMethod 2: Reading file using with")

try:
    with open("sample.txt","r") as f:
        line_num = 1
        while True:
            line = f.readline()
            if not line:
                break
            print(f"line {line_num}: {line.strip()}")
            line_num += 1
except FileNotFoundError as f:
    print("Error: The file 'sample.txt' was not found")
except Exception as e:
    print(f"An error occurred: {e}")