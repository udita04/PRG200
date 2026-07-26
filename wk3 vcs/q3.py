def recharge_cost(gb, validity_days=30):
    if gb == 1:
        price = 150
    elif gb == 5:
        price = 500
    elif gb == 10:
        price = 900
    else:
        price = 0

    return price


print(recharge_cost(1))
print(recharge_cost(5))
print(recharge_cost(10))