# Name: Udita Pudasaini
# Project 5: BMI for a Community Health Camp

weight = float(input("Enter weight in kg: "))
height_cm = float(input("Enter height in cm: "))

height_m = height_cm / 100
bmi = weight / (height_m ** 2)

print(f"Height in Meters: {height_m} m")
print(f"BMI: {bmi}")