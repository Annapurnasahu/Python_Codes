# Task: Write, Append, and Read a File
# Author: Annapurna Sahu

# Write user input to the file
text = input("Enter text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(text + "\n")
print("Data successfully written to output.txt.")

# Append additional text to the same file
additional_text = input("Enter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(additional_text + "\n")
print("Data successfully appended.")

# Read and display the final content of the file
print("Final content of output.txt:")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())
