'''14. Simple Sales Chart
• Create data for 5 months and their sales values.
• Use Matplotlib to create a bar chart.
• Add a title, X-axis label and Y-axis label.
• Display the chart.'''

import matplotlib.pyplot as plt

# Data for 5 months
months = ["January", "February", "March", "April", "May"]
sales = [27000, 27500, 26000, 28000, 29000]

# Create bar chart
plt.bar(months, sales)

# Add title and labels
plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")

# Display the chart
plt.show()