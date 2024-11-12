import re

def assess_password_strength(password: str) -> str:
    # Criteria for strength
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[\W_]', password) is not None

    # Checking how many criteria are met
    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])

    # Strength evaluation
    if criteria_met == 5:
        return "Very Strong"
    elif criteria_met == 4:
        return "Strong"
    elif criteria_met == 3:
        return "Moderate"
    elif criteria_met == 2:
        return "Weak"
    else:
        return "Very Weak"

# Test the function
password = input("Enter a password to assess its strength: ")
strength = assess_password_strength(password)
print(f"Password strength: {strength}")