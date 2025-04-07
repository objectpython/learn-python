#Module 5: Files, Exceptions, and Errors in Python

#Task 2: Write and Append Data to a File


'''
To Do:
Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.


'''
try:
    with open("output.txt","w") as f:
        user_input = input("Enter text to write to the file: ")
        f.write(user_input+"\n")
        print("Data successfully written to output.txt.")

    with open("output.txt","a+") as f:
        user_input = input("Enter additional text to append: ")
        f.write(user_input)
        print("Data successfully appended.")
        f.seek(0)
        print("\nFinal content of output.txt")
        print(f.read())

except FileNotFoundError as f:
    print("Error: The file 'sample.txt' was not found")
except Exception as e:
    print(f"An error occurred: {e}")