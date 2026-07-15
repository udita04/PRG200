def ticket_price(seat_type, count):
    if seat_type == "regular":
        price = 300
    else:
        price = 500

    total = price * count
    return total


print(ticket_price("regular", 2))
print(ticket_price("recliner", 3))
