# Name: Udita Pudasaini
# Project 3: Trekking Permit Cost Calculator

number_of_trekkers = int(input("Enter number of trekkers: "))
tims_fee = float(input("Enter TIMS fee per person: "))
acap_fee = float(input("Enter ACAP fee per person: "))

permit_cost_per_person = tims_fee + acap_fee
group_permit_cost = permit_cost_per_person * number_of_trekkers

service_charge = group_permit_cost * 5 / 100
total_cost = group_permit_cost + service_charge
average_cost = total_cost / number_of_trekkers

print(f"Group Permit Cost: NPR {group_permit_cost}")
print(f"Agency Service Charge: NPR {service_charge}")
print(f"Total Cost: NPR {total_cost:.2f}")
print(f"Average Cost Per Person: NPR {average_cost}")