# Task 1
# Author: Annapurna Sahu
# Task: Create a Dictionary of Student Marks

# Step 1: Create a dictionary of student marks with mixed names
student_marks = {
    "Alice": 85,
    "Rohan": 78,
    "Priya": 92,
    "Amit": 88
}

# Step 2: Ask the user to input a student's name
student_name = input("Enter the student's name: ")

# Step 3: Retrieve and display the marks
if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    # Step 4: If student not found
    print("** Student not found **")
README.md
markdown
Copy code
# Student Marks Dictionary

Author: Annapurna Sahu  

This Python program creates a dictionary of student names (including Alice and Indian names) and their marks.  
It allows the user to input a student's name and displays the corresponding marks.  
If the student does not exist in the dictionary, it shows a “student not found” message.

---

## Task: Create a Dictionary of Student Marks

### Description:
1. The program has a predefined dictionary with student names as keys and their marks as values.  
   - Names include **Alice** and Indian names like **Rohan, Priya, Amit**.  
2. The user enters the name of a student.  
3. The program checks if the student exists in the dictionary:  
   - If yes, it prints the student’s marks.  
   - If no, it prints "** Student not found **".

---

## Example Output

**Case 1: Student exists**
Enter the student's name: Alice
Alice's marks: 85

Copy code
Enter the student's name: Rohan
Rohan's marks: 78

markdown
Copy code

**Case 2: Student does not exist**
Enter the student's name: Karan
** Student not found **

# TASK 2
# Write and Append Data to a File in Python

Author: Annapurna Sahu  

This Python program demonstrates how to write data to a file, append additional data, and then read and display the contents of the file.

---

## Task: Write and Append Data to a File

### Description:
1. The program takes input from the user and writes it to a file named `output.txt`.  
2. It then takes additional input and appends it to the same file.  
3. Finally, it reads and displays all the contents of the file.

---

## Code Explanation

### Steps:
1. **Write to the File:**  
   - Take input from the user and write it to `output.txt` using `"w"` mode.  
   - `"w"` mode creates the file if it doesn't exist or overwrites it if it does.

2. **Append to the File:**  
   - Take additional input and append it to the file using `"a"` mode.  
   - `"a"` mode adds data at the end without overwriting existing content.

3. **Read and Display File Content:**  
   - Open the file in `"r"` mode and read each line.  
   - Print all lines to show the final content.

---

## Example Output
Enter text to write to the file: Hello, python!
Data successfully written to output.txt.
Enter additional text to append: Learning file handling in python.
Data successfully appended.
Final content of output.txt:
Hello, python!
Learning file handling in python.


