"""
CP1404/CP5632 - Practical 2
Password checker program with functions
"""

MIN_LENGTH = 8

def main():
    """Get password from user and print asterisks"""
    password = get_password()
    print_asterisks(password)

def get_password():
    """Get password from user with error-checking"""
    password = input("Enter a password: ")
    while len(password) < MIN_LENGTH:
        print(f"Password must be at least {MIN_LENGTH} characters long.")
        password = input("Enter a password: ")
    return password

def print_asterisks(password):
    """Print asterisks as long as the password"""
    print('*' * len(password))

main()