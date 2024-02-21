 import base64

# Encoded passwords
encoded_passwords = ["ZG9neQ==", "RG9neQ==", "RE9HWA=="]

# Decode the passwords
correct_passwords = [base64.b64decode(encoded).decode('utf-8') for encoded in encoded_passwords]

# Start an infinite loop to keep asking for the password until it's correct
while True:
    # Ask for the password, ensuring it's treated as a string
    password_guess = str(input("Enter the password: "))

    # Check if the password guess is correct
    if password_guess in correct_passwords:
        print("Correct, Yay!")
        break  # Exit the loop since the password is correct
    else:
        print("Try again.")
