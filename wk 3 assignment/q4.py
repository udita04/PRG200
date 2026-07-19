# Name: Udita Pudasaini
# Week 3 Assignment
# Question 4 - Password Strength Checker

password = input("Enter your password: ")

has_uppercase = False
has_digit = False

for character in password:
    if character.isupper():
        has_uppercase = True

    if character.isdigit():
        has_digit = True

if len(password) >= 8 and has_uppercase and has_digit:
    print("Strong Password")
else:
    print("Weak Password")