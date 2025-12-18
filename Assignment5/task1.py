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
