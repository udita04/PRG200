# Name: Udita Pudasaini
# Project 4: Dashain Bonus Calculator

monthly_salary = float(input("Enter monthly basic salary: "))
deduction_percentage = float(input("Enter deduction percentage: "))

dashain_bonus = monthly_salary
deduction = dashain_bonus * deduction_percentage / 100
take_home_bonus = dashain_bonus - deduction

print(f"Dashain Bonus: NPR {dashain_bonus:}")
print(f"Deduction: NPR {deduction}")
print(f"Take-Home Bonus: NPR {take_home_bonus}")