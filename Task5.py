'''5. Student Management Program
• Create a list containing 3 student dictionaries.
• Each student should have id, name and age.
• Display all students.
• Ask for an ID and display the matching student.'''

students = [
    {"id" : 1, "name" : "Pavan", "age" : 24 },
    {"id" : 2, "name" : "Varun", "age" : 25 },
    {"id" : 3, "name" : "Abhi", "age" : 24}
]

print("All Students")
for std in students:
    print(std)

id = int(input("Enter the Student id: "))

found = False

for std in students:
    if std["id"] == id:
        print("\nStudent Found")
        print("ID:", std["id"])
        print("Name:", std["name"])
        print("Age:", std["age"])
        found = True
        break
if not found:
    print("Student not found")    