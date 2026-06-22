import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    # Check uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters (A-Z).")

    # Check lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters (a-z).")

    # Check numbers
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add numbers (0-9).")

    # Check special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add special characters (!@#$%).")

    # Classify password
    if score == 5:
        strength = "Strong Password"
    elif score >= 3:
        strength = "Medium Password"
    else:
        strength = "Weak Password"

    print("\nPassword Strength:", strength)
    
    if feedback:
        print("Suggestions to improve:")
        for item in feedback:
            print("-", item)
    else:
        print("Your password is secure!")


# Main program
password = input("Enter your password: ")
check_password_strength(password)