import re
import getpass


def check_password_strength(password):
    score = 0
    suggestions = []

    checks = {
        "Length (>=8 characters)": len(password) >= 8,
        "Lowercase letter": re.search(r"[a-z]", password),
        "Uppercase letter": re.search(r"[A-Z]", password),
        "Digit": re.search(r"\d", password),
        "Special character": re.search(r"[!@#$%^&*(),.?\":{}|<>]", password),
    }

    for rule, passed in checks.items():
        if passed:
            score += 1
        else:
            suggestions.append(f"Add {rule.lower()}.")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, suggestions


def main():
    print("=" * 40)
    print("        Password Strength Checker")
    print("=" * 40)

    while True:
        password = getpass.getpass("Enter your password: ")

        strength, suggestions = check_password_strength(password)

        print("\nPassword Strength:", strength)

        if suggestions:
            print("\nSuggestions to Improve:")
            for suggestion in suggestions:
                print("-", suggestion)
        else:
            print("Excellent! Your password is secure.")

        choice = input("\nDo you want to test another password? (y/n): ")
        if choice.lower() != 'y':
            print("\nExiting program. Stay secure!")
            break


if __name__ == "__main__":
    main()
