'''9. Student File Program
• Create a text file named students.txt.
• Write at least 3 student names and marks into the file.
• Read the file and display its contents.
• Use with open(...) for file handling.'''

# Create and write to the file
with open("students.txt", "w") as file:
    file.write("Rahul - 85\n")
    file.write("Priya - 92\n")
    file.write("Arun - 78\n")

# Read and display the file contents
with open("students.txt", "r") as file:
    contents = file.read()

print("Student Details:")
print(contents)