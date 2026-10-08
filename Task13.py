'''13. NumPy Marks Analysis
• Create a NumPy array containing 5–10 marks.
• Find the mean, maximum and minimum.
• Display marks greater than 80.
• Print the results clearly.'''

import numpy as np

# Create a NumPy array containing 8 marks
marks = np.array([75, 85, 92, 68, 88, 79, 95, 72])

# Calculate mean, maximum and minimum
mean_mark = np.mean(marks)
maximum_mark = np.max(marks)
minimum_mark = np.min(marks)

# Find marks greater than 80
above_80 = marks[marks > 80]

# Display results clearly
print("Marks:", marks)
print("Mean Mark:", mean_mark)
print("Maximum Mark:", maximum_mark)
print("Minimum Mark:", minimum_mark)
print("Marks Greater Than 80:", above_80)