# TASK 1
# Read a File and Handle Errors

Author: Annapurna Sahu  

This Python program reads the contents of a file and handles errors if the file does not exist.

---

## Task: Read a File and Handle Errors

### Description:
The program attempts to open and read a file named `sample.txt`.  
It prints each line of the file.  
If the file is not found, it displays an appropriate error message instead of crashing.

---

## Code Explanation

### Steps:
1. Use a `try` block to attempt opening the file in read mode.  
2. Use a `with` statement to ensure the file is properly closed after reading.  
3. Loop through each line of the file and print it using `print(line.strip())` to remove extra spaces and newline characters.  
4. Use an `except FileNotFoundError` block to catch the error if the file does not exist and print a friendly error message.

---

## Example Output

**If `sample.txt` exists:**

This is line 1.
This is line 2.
This is line 3.


**If `sample.txt` does not exist:**
Error: The file "sample.txt" was not found.
