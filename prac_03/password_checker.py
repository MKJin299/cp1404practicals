"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"

def main():
    print_intro()
    password = get_password()
    while not validate_password(password):
        print("Invalid password!")
        password = get_password()
    print_valid(password)

def print_intro():
    print("Please enter a valid password.")
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARACTERS_REQUIRED:
        print("\tand 1 or more special characters:", " ".join(SPECIAL_CHARACTERS))
    else:
        print("\tbut it can have any other characters")

def get_password():
    password = input("> ")
    return password

def validate_password(password):
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False
    count_lower = sum(1 for char in password if char.islower())
    count_upper = sum(1 for char in password if char.isupper())
    count_digit = sum(1 for char in password if char.isdigit())
    count_special = sum(1 for char in password if char in SPECIAL_CHARACTERS)
    if any(count == 0 for count in [count_lower, count_upper, count_digit, count_special]) and SPECIAL_CHARACTERS_REQUIRED:
        return False
    return True

def print_valid(password):
    print(f"Your {len(password)} character password is valid: {password}")

def print_why_not():
    print("> whyNot?CanIhave This?")

if __name__ == "__main__":
    main()