name = input("Enter customer name: ")
people = int(input("Enter number of people in the group: "))

total_price = 0

for i in range(1, people + 1):
    price = float(input(f"Enter food price {i}: NPR "))
    total_price += price

print("\nTotal Bill Before Discount: NPR", total_price)

if total_price > 2000:
    discount = total_price * 0.10
    total_price -= discount
    print("10% Discount Applied: NPR", discount)
else:
    print("No Discount Applied")

split_amount = total_price / people

print("Customer Name:", name)
print("Total Bill After Discount: NPR", total_price)
print("Amount Each Person Pays: NPR", round(split_amount, 2))