import re

def check_password_strength(password):
    score = 0
    suggestions = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Increase length to at least 8 characters")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter (A-Z)")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter (a-z)")

    # Numbers
    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Add at least one number (0-9)")

    # Special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Add at least one special character (!@#$...)")

    # Strength result
    if score <= 2:
        strength = "Weak ❌"
    elif score == 3 or score == 4:
        strength = "Medium ⚠️"
    else:
        strength = "Strong 🔥"

    return strength, suggestions


if __name__ == "__main__":
    print("🔐 Password Strength Checker\n")

    while True:
        password = input("Enter password: ")

        strength, suggestions = check_password_strength(password)

        print(f"\nPassword Strength: {strength}")

        if strength == "Strong 🔥":
            print("\n✅ Your password is strong. Accepted!")
            break
        else:
            print("\n⚠️ Suggestions to improve your password:")
            for s in suggestions:
                print(f"- {s}")

            print("\n🔁 Try again...\n")