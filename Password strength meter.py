
import re

def password_strength_meter(password):
    strength = 0
    errors = []

    print("\nPassword Strength Meter")
    print("---------------------------")

    # Check password length
    if len(password) < 8:
        errors.append("Password is too short. It should be at least 8 characters.")
    else:
        strength += 1
        print("Password length: Strong")

    # Check for digits
    if not re.search(r"\d", password):
        errors.append("Password should have at least one digit.")
    else:
        strength += 1
        print("Digits: Strong")

    # Check for uppercase letters
    if not re.search(r"[A-Z]", password):
        errors.append("Password should have at least one uppercase letter.")
    else:
        strength += 1
        print("Uppercase letters: Strong")

    # Check for lowercase letters
    if not re.search(r"[a-z]", password):
        errors.append("Password should have at least one lowercase letter.")
    else:
        strength += 1
        print("Lowercase letters: Strong")

    # Check for special characters
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        errors.append("Password should have at least one special character.")
    else:
        strength += 1
        print("Special characters: Strong")

    print("\nPassword Strength:")
    if strength == 5:
        print("Strong")
    elif strength >= 3:
        print("Medium")
    else:
        print("Weak")

    if errors:
        print("\nErrors:")
        for error in errors:
            print(error)

password = input("Enter your password: ")
password_strength_meter(password)


# Password ki strength ko 5 categories mein check kiya jata hai:

#- Password length
#- Digits
#- Uppercase letters
#- Lowercase letters
#- Special characters

#Agar password mein 5 categories mein se 5 categories pass hoti hain, to password ki strength "strong" hoti hai. Agar 3 ya 4 categories pass hoti hain, to password ki strength "medium" hoti hai. Agar 2 ya kam categories pass hoti hain, to password ki strength "weak" hoti hai.