# TASK 2 
# Write, Append, and Read a File in Python

Author: Annapurna Sahu  

This Python program demonstrates how to write data to a file, append additional data, and then read and display the contents of the file.

---

## Task: Write, Append, and Read a File

### Description:
The program allows the user to:
1. Write initial text to a file named `output.txt`.  
2. Append additional text to the same file.  
3. Read and display the final contents of the file.  

This program helps in understanding file handling in Python including write, append, and read operations.

---

## Code Explanation

### Steps:
1. **Write to a File:**  
   - Take user input and write it to `output.txt` using `"w"` mode.  
   - `"w"` mode creates the file if it does not exist or overwrites it if it does.  

2. **Append to the File:**  
   - Take additional input and append it to the same file using `"a"` mode.  
   - `"a"` mode adds data at the end of the file without overwriting existing content.  

3. **Read from the File:**  
   - Open the file in `"r"` mode and read its content line by line.  
   - Display the final content to the user.

---

## Example Output
Enter text to write to the file: Hello, Python!
Data successfully written to output.txt.
Enter additional text to append: Learning file handling in Python.
Data successfully appended.
Final content of output.txt:
Hello, Python!
Learning file handling in Python.
