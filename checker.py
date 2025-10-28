import re

def check_password_strength(password):
    # Define a good password example
    example_password = "Example1Password"

    # Check password length
    if len(password) < 8:
        return f"Password is too short! Must be at least 8 characters. Example: {example_password}"

    # Check if it contains at least one letter and one number
    if not re.search(r'[A-Za-z]', password):
        return f"Password must contain at least one letter. Example: {example_password}"

    if not re.search(r'\d', password):
        return f"Password must contain at least one number. Example: {example_password}"

    return "Password is strong!"

if __name__ == "__main__":
    password = input("Enter a password to check: ")
    print(check_password_strength(password))
