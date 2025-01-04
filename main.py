import re

def check_password_complexity(password):
    min_length = 8
    has_upper = bool(re.search(r"[A-Z]", password)) 
    has_lower = bool(re.search(r"[a-z]", password)) 
    has_digit = bool(re.search(r"\d", password))     
    has_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))  

    
    length_ok = len(password) >= min_length
    complexity_score = sum([length_ok, has_upper, has_lower, has_digit, has_special])

    if complexity_score == 5:
        return "Strong password! It meets all complexity requirements."
    elif complexity_score >= 3:
        return "Moderate password. Consider adding more complexity (e.g., special characters or digits)."
    else:
        return "Weak password. Make sure it's at least 8 characters long and includes uppercase, lowercase, digits, and special characters."


password = input("Enter your password: ")
result = check_password_complexity(password)
print(result)