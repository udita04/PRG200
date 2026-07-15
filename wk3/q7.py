orders = [
    ("Order1", 30),
    ("Order2", 15),
    ("Order3", 45),
    ("Order4", 20)
]

orders.sort(key=lambda order: order[1])

print(orders)