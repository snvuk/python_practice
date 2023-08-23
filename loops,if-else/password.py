while True:
    password = input("Enter a password: ")

    if len(password) < 8:
        print("Password is too short")
    elif not any(char.isupper() for char in password):
        print("Password must contain at least one uppercase letter")
    elif not any(char.islower() for char in password):
        print("Password must contain at least one lowercase letter")
    elif not any(char.isdigit() for char in password):
        print("Password must contain at least one digit")
    elif all(char.isalnum() for char in password):
        print("Password must contain at least one special character")
    else:
        print("Password is valid.")
