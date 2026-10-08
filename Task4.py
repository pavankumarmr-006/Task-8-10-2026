'''4. Number List Analyzer
• Create a list containing 5 numbers.
• Use a loop to display each number.
• Find the largest and smallest number.
• Calculate the total of the numbers.'''

'''list = []
print("Enter the numbers in the list")
for i in range(5): 
    num = int(input())
    list.append(num)'''

list = [10, 20, 30, 40, 50]

print("Number in the list are: ")
for num in list:
    print(num)

largest = max(list)
smallest = min(list)
total = sum(list)

print("Largert number: ", largest)
print("Smallest number: ", smallest)
print("The total sum of the numbers in the list: ", total)    
