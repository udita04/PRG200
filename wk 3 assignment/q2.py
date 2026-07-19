# Name: Udita Pudasaini
# Week 3 Assignment
# Question 2 - Online Store Discount System

purchase = float(input("Enter total purchase amount (NPR): "))
member = input("Are you a loyalty member? (yes/no): ")

discount = 0

if purchase < 1000:
    discount = 0

elif purchase < 5000:
    discount = 5

elif purchase < 15000:
    discount = 10

else:
    discount = 20

if member.lower() == "yes":
    discount = discount + 5

discount_amount = purchase * discount / 100
final_amount = purchase - discount_amount

print("\n Bill")
print(f"Purchase Amount : NPR {purchase:.2f}")
print(f"Discount : {discount}%")
print(f"Discount Amount : NPR {discount_amount:.2f}")
print(f"Final Amount : NPR {final_amount:.2f}")