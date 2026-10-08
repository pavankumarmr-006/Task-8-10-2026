'''6. Simple Employee Class
• Create an Employee class.
• Add name, age and salary as attributes.
• Create a display_details() method.
• Create two employee objects and display their details.'''

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display_details(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Salary: ", self.salary)
        print() 

employee1 = Employee("Pavan", 25, 30000)
employee2 = Employee("Varun", 25, 80000)

print("Employee 1: ")
employee1.display_details()

print("Employee 2: ")
employee2.display_details()


