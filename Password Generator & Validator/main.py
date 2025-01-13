                                    # Password Generator & Validator

# Modules
import string
import random

special_characters = ['!', '@', '#', '$', '*', '.', '?', '_']

# Function to generate random password based on specific conditions using the random library
def generate_password(length, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits + "!@#$%^&*()"):
    return ''.join(random.choices(chars, k = length))

# Function to validate password strength against specific conditions
def validate_password():
    y = input("Enter the password to validate: ")
    if len(y) >= 12 and any(char.isdigit for char in y) and any(char.isupper for char in y) and any(char.islower for char in y) and any(char in special_characters for char in y):
        print("Password is valid!")
    else:
        print("Password is not valid...")

# User input, call function(s), output result
while True:
    user_input = int(input("Do you want to (1) generate a password or (2) validate a password?"))
    if user_input == 1:
        x = int(input("Enter the desired password length (minimum 12): "))
        password = generate_password(x)
        print("Generated password:", password)
    elif user_input == 2:
        validate_password()
    else:
        break