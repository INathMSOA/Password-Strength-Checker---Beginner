import pytest

# -----------------------------
# Main password checker function
# -----------------------------
def check_password_strength(password):
    if len(password) < 8:
        return "Password is too short! Must be at least 8 characters. Example: Example1Password"
    if not any(c.isalpha() for c in password):
        return "Password must contain at least one letter. Example: Example1Password"
    if not any(c.isdigit() for c in password):
        return "Password must contain at least one number. Example: Example1Password"
    return "Password is strong!"

# -----------------------------
# Main program entry point
# -----------------------------
if __name__ == "__main__":
    user_password = input("Enter your password: ")
    print(check_password_strength(user_password))

# -----------------------------
# Unit tests (used by pytest)
# -----------------------------
def test_short_password():
    result = check_password_strength("short")
    assert result == "Password is too short! Must be at least 8 characters. Example: Example1Password"

def test_no_letters():
    result = check_password_strength("12345678")
    assert result == "Password must contain at least one letter. Example: Example1Password"

def test_no_numbers():
    result = check_password_strength("abcdefgh")
    assert result == "Password must contain at least one number. Example: Example1Password"

def test_strong_password():
    result = check_password_strength("Strong1Password")
    assert result == "Password is strong!"
