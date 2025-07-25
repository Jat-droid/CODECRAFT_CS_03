import string

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Include lowercase letters.")

    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Include uppercase letters.")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Include numbers.")

    if any(c in string.punctuation for c in password):
        score += 1
    else:
        feedback.append("Include special characters.")

    # Determine strength level
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, feedback

# Main program
password = input("Enter your password: ")
strength, feedback = check_password_strength(password)

print(f"Password Strength: {strength}")
if feedback:
    print("Suggestions:")
    for tip in feedback:
        print(f"- {tip}")
