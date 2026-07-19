# Name: Udita Pudasaini
# Week 3 Assignment
# Question 5 - Taxi Fare Calculator

base_fare = float(input("Enter base fare (NPR): "))
distance = float(input("Enter distance travelled (km): "))
cost_per_km = float(input("Enter cost per kilometer: "))
waiting_time = float(input("Enter waiting time (minutes): "))
waiting_charge = float(input("Enter waiting charge per minute: "))

distance_fare = distance * cost_per_km
waiting_fare = waiting_time * waiting_charge
total_fare = base_fare + distance_fare + waiting_fare

print("Taxi Fare")
print(f"Base Fare: NPR {base_fare:.2f}")
print(f"Distance Fare: NPR {distance_fare:.2f}")
print(f"Waiting Charge: NPR {waiting_fare:.2f}")
print(f"Total Fare: NPR {total_fare:.2f}")