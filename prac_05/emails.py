"""
emails
Estimate: 30 minutes
Actual:   40 minutes
"""


def main():
    email_dict = {}
    email = input("Email: ").strip()

    while email != "":
        name_from_email = extract_name_from_email(email)
        default_name = name_from_email.replace('.', ' ').title()

        # Prompt user if the extracted name is correct
        confirmation = input(f"Is your name {default_name}? (Y/n) ").strip().lower()

        if confirmation == '' or confirmation == 'y':
            name = default_name
        else:
            name = input("Name: ").strip().title()

        email_dict[email] = name
        email = input("Email: ").strip()

    print("\nResults:")
    for email, name in email_dict.items():
        print(f"{name} ({email})")


def extract_name_from_email(email):
    username = email.split('@')[0]
    return username.title()


main()
