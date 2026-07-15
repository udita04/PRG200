# Name: Udita Pudasaini
# Project 2: NEA Electricity Unit Cost

previous_reading = float(input("Enter previous meter reading: "))
current_reading = float(input("Enter current meter reading: "))
unit_rate = float(input("Enter cost per unit: "))
service_charge = float(input("Enter monthly service charge: "))

units_consumed = current_reading - previous_reading
electricity_cost = units_consumed * unit_rate
total_bill = electricity_cost + service_charge

print(f"Units Consumed: {units_consumed} kWh")
print(f"Electricity Cost: NPR {electricity_cost}")
print(f"Service Charge: NPR {service_charge}")
print(f"Total Bill: NPR {total_bill}")