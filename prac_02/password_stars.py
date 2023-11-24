def get_password():
    password = input("Enter a password: ")

    min_length = 6
    while len(password) < min_length:
        print("Your password is too short. It must be at least", min_length, "characters long.")
        password = input("Enter a password: ")

    return password

def print_asterisks(password):
    print("*" * len(password)))

def main():
    password = get_password()
    print_asterisks(password)

if __name__ == "__main__":
    main()