# Name: Udita Pudasaini
# Project 7: Age Calculator (BS Birth Year)

name = input("Enter your name: ")
birth_year = int(input("Enter your birth year in BS: "))
current_year = int(input("Enter current BS year: "))

age = current_year - birth_year

print(f"Hello {name}! You are approximately {age} years old.")