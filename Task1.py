'''1. Student Marks Calculator
• Ask for the student's name and three marks.
• Calculate total and average marks.
• Display Pass if the average is 50 or above; otherwise display Fail.
• Use variables and if/else.'''


print("Enter Student Name: ")
name = str(input())

print("Enter marks 1: ")
m1 = int(input())

print("Enter marks 2: ")
m2 = int(input())

print("Enter marks 3: ")
m3 = int(input())

sum = m1 + m2 + m3 
avg = sum/3

print("\nStudent Name:", name)
print("Total Marks:", sum)
print("Average Marks:", avg)

if avg >= 50:
    print("Result: Pass")
else: 
    print("Result: Fail")     

