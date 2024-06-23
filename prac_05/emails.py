"""
Emails
Estimate: 30 minutes
Actual: 35 minutes
"""


def main():
    email_to_name = {}

    print("Enter email addresses (blank to finish):")
    while True:
        email = input("Email: ").strip()
        if email == "":
            break

        name = extract_name(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()

        if confirmation not in ['', 'y', 'yes']:
            name = input("Name: ").strip()

        email_to_name[email] = name

    print("\nStored email addresses and names:")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    parts = email.split('@')[0].split('.')
    return ' '.join(part.title() for part in parts)


if __name__ == "__main__":
    main()