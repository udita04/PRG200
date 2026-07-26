def estimate_fare(distance_km, vehicle_type, surge=1.0):
    if vehicle_type == "bike":
        rate = 20
    else:
        rate = 35

    fare = distance_km * rate
    fare = fare * surge

    return fare


print(estimate_fare(8, "bike"))
print(estimate_fare(8, "car", surge=1.5))