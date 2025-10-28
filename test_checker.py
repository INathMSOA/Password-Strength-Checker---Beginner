import pytest
from checker import check_password_strength

def test_short_password():
    # Test for a password that is too short
    result = check_password_strength("short")
    assert result == "Password is too short! Must be at least 8 characters. Example: Example1Password"

def test_no_letters():
    # Test for a password that contains only numbers
    result = check_password_strength("12345678")
    assert result == "Password must contain at least one letter. Example: Example1Password"

def test_no_numbers():
    # Test for a password that contains only letters
    result = check_password_strength("abcdefgh")
    assert result == "Password must contain at least one number. Example: Example1Password"

def test_strong_password():
    # Test for a valid strong password
    result = check_password_strength("Strong1Password")
    assert result == "Password is strong!"
