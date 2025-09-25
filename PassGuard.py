# PassGuard - Password Strength Checker
# This program assesses the strength of a password based on length,
# uppercase/lowercase letters, numbers, and special characters.

import re

def check_password_strength(password):
    score = 0

    # Check length
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1  # Extra point for longer passwords

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1

    # Check for digits
    if re.search(r'\d', password):
        score += 1

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1

    # Determine strength
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, score

# Main program
if __name__ == "__main__":
    print("===== PassGuard - Password Strength Checker =====")
    password = input("Enter your password to check strength: ")
    strength, score = check_password_strength(password)
    print(f"\nPassword Strength: {strength} (Score: {score}/6)")

