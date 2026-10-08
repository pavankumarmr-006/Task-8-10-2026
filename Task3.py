'''3. Simple Shopping Bill
• Ask for product name, price and quantity.
• Calculate the total price.
• Create a small function to calculate the total.
• Display the product name, quantity and final amount.'''

def calculate_total(price, quantity):
    return price * quantity

name = str(input("Enter Product Name: "))

price = int(input("Enter Price: "))
quantity = int(input("Enter Quantity: "))

total = calculate_total(price, quantity)

print("Product Name: ",name)
print("Quantity: ",quantity)
print("Final Amount: ",total)


