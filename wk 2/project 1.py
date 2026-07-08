drinks = ["Coke", "Pepsi", "Sprite", "Water", "Juice"]
prices = [50, 50, 45, 20, 60]
stock = [5, 5, 5, 10, 3]

running = True

while running:
    print("\n VENDING MACHINE")
    
    for i in range(len(drinks)):
        print(i + 1, "-", drinks[i], "| Price: Rs.", prices[i], "| Stock:", stock[i])
    
    choice = int(input("\nEnter the number of the drink you want (0 to Exit): "))
    
    if choice == 0:
        print("Thank you for using the vending machine!")
        running = False
        continue  
    
    index = choice - 1
    
    if index < 0 or index >= len(drinks):
        print("Invalid choice! Try again.")
        continue
    
    qty = int(input("Enter quantity: "))
    
    if qty > stock[index]:
        print("Sorry, not enough stock available! Only", stock[index], "left.")
        continue
    
    total_price = prices[index] * qty
    print("Total price for", qty, drinks[index], "(s) is Rs.", total_price)
    
    amount = int(input("Insert amount: Rs. "))
    
    if amount < total_price:
        print("Insufficient amount! Purchase cancelled.")
    else:
        change = amount - total_price
        print("Purchase successful! Your change is Rs.", change)
        
        stock[index] = stock[index] - qty
    
    again = input("\nDo you want to buy another drink? (yes/no): ")
    if again.lower() != "yes":
        print("Thank you! Have a nice day.")
        running = False