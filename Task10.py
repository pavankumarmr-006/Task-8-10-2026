'''10. Student CSV Analysis
• Create a small students.csv file with name, age and mark.
• Load it using Pandas.
• Display the first 5 rows.
• Find the average mark and students who scored above 80.'''

import pandas as pd
# Create students.csv
data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Emma", "Frank"],
    "age": [20, 21, 19, 22, 20, 21],
    "mark": [85, 72, 91, 68, 88, 79]
}

df = pd.DataFrame(data)
df.to_csv("students.csv", index=False)

# Load the CSV using Pandas
students = pd.read_csv("students.csv")

# Display the first 5 rows
print("First 5 rows:")
print(students.head())

# Find the average mark
average_mark = students["mark"].mean()
print("\nAverage mark:", average_mark)

# Find students who scored above 80
above_80 = students[students["mark"] > 80]
print("\nStudents who scored above 80:")
print(above_80)