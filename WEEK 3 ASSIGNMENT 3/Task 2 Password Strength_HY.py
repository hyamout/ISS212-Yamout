#Password Strength Checker - WK3-pwstrcheck.py

import re  # Import the re module for regular expressions

# Function to check the strength of a password
def check_password_strength(password):
    # Initialize a list to hold any weakness messages
    weaknesses = []

    # Check for minimum 8 characters
    if len(password) < 8:
        weaknesses.append("Less than 8 characters")

    # Check for at least one uppercase letter
    if not re.search(r"[A-Z]", password):
        weaknesses.append("No uppercase letter")

    # Check for at least one lowercase letter
    if not re.search(r"[a-z]", password):
        weaknesses.append("No lowercase letter")

    # Check for at least one number
    if not re.search(r"[0-9]", password):
        weaknesses.append("No number")

    # Check for at least one special character
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        weaknesses.append("No special character")

    # If there are any weaknesses, return them in a single line; otherwise, return that the password is strong
    if weaknesses:
        return "Weak password: " + ", ".join(weaknesses)
    else:
        return "Strong password"  # If all conditions are met, the password is strong

# Main function to run the script
if __name__ == "__main__":
    # Prompt the user to enter a password
    user_password = input("Enter your password: ")
    # Check the strength of the entered password
    result = check_password_strength(user_password)
    # Print the result
    print(result)
