# Name: Udita Pudasaini
# Project 1: Foreign Remittance Converter

usd_amount = float(input("Enter amount sent in USD: "))
exchange_rate = float(input("Enter current exchange rate: "))
fee_percentage = float(input("Enter service fee percentage: "))

npr_amount = usd_amount * exchange_rate
service_fee = npr_amount * fee_percentage / 100
final_amount = npr_amount - service_fee

print(f"Converted Amount: NPR {npr_amount}")
print(f"Service Fee: NPR {service_fee}")
print(f"Final Amount Received: NPR {final_amount}")