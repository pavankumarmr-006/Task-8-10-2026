import pandas as pd
import matplotlib.pyplot as plt

# Load the employee data
df = pd.read_csv("employees.csv")

# Display the data
print("Employee Data:")
print(df)

# Calculate average salary
average_salary = df["salary"].mean()

# Find highest salary
highest_salary = df["salary"].max()

# Find highest-paid employee
highest_paid_employee = df.loc[df["salary"].idxmax(), "name"]

print(f"\nAverage Salary: ${average_salary:,.2f}")
print(f"Highest Salary: ${highest_salary:,.2f}")
print(f"Highest Paid Employee: {highest_paid_employee}")

# Create salary chart
plt.figure(figsize=(8, 5))
plt.bar(df["name"], df["salary"], color="steelblue")

plt.title("Employee Salaries")
plt.xlabel("Employee")
plt.ylabel("Salary ($)")
plt.xticks(rotation=45)
plt.tight_layout()

# Save the chart
plt.savefig("salary_chart.png")

# Display the chart
plt.show()