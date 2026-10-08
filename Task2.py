'''2. Even or Odd Number Checker
• Ask the user to enter a number.
• Check whether the number is even or odd.
• Display a clear message such as '10 is even'.
• Use if/else and the modulus (%) operator.'''

print("Enter a number: ")
num = int(input())

if num % 2 == 0:
    print(num,"is Even")
else: 
    print(num,"is Odd")