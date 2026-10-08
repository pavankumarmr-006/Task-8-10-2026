'''8. Safe Calculator
• Ask the user for two numbers.
• Perform division.
• Use try/except to handle invalid input.
• Also handle division by zero.'''
try:
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))

    div = num1 / num2
    print("Result: ", div)

except ValueError:
    print("Invalid input. Pleace enter numbers only")

except ZeroDivisionError:
    print("Cannot divide by Zero")