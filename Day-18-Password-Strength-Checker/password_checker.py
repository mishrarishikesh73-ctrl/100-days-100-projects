
import string
import getpass


def check_password(password):
    score = 0
    suggestions = []

    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    # Check uppercase
    if any(char.isupper() for char in password):
        score += 1
    else:
        suggestions.append("Add an uppercase letter.")

    # Check lowercase
    if any(char.islower() for char in password):
        score += 1
    else:
        suggestions.append("Add a lowercase letter.")

    # Check digits
    if any(char.isdigit() for char in password):
        score += 1
    else:
        suggestions.append("Add a number.")

    # Check special characters
    if any(char in string.punctuation for char in password):
        score += 1
    else:
        suggestions.append("Add a special character.")

    # Check strength
    if score <= 2:
        strength = "WEAK"
    elif score <= 4:
        strength = "MEDIUM"
    else:
        strength = "STRONG"

    return strength, score, suggestions


def main():
    print("\n====== PASSWORD STRENGTH CHECKER ======")

    password = getpass.getpass("Enter your password: ")

    if not password:
        print("Password cannot be empty!")
        return

    strength, score, suggestions = check_password(password)

    print("\n====== PASSWORD REPORT ======")
    print(f"Strength: {strength}")
    print(f"Score: {score}/5")

    if suggestions:
        print("\nSuggestions:")
        for suggestion in suggestions:
            print("-", suggestion)
    else:
        print("Great! All basic checks passed.")


if __name__ == "__main__":
    main()
