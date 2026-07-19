# Name: Udita Pudasaini
# Week 3 Assignment
# Question 3 - Inventory Restock Alert

product_name = input("Enter product name: ")
stock = int(input("Enter current stock quantity: "))
minimum_stock = int(input("Enter minimum stock level: "))

print(" Inventory Report ")
print("Product:", product_name)
print("Current Stock:", stock)
print("Minimum Stock:", minimum_stock)

if stock < minimum_stock:
    print("Restock Required!")
else:
    print("Stock Level is Sufficient.")