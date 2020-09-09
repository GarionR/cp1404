# Code reviewed, I cannot see anywhere you need to change.

email_names = {}
email = input("Email: ")
while email:
    email_parts = email.split("@")
    name_part = email_parts[0]
    name_part = name_part.split(".")
    name = " ".join(name_part).title()
    is_name = input("Is your name {}? (Y/n) ".format(name)).lower()
    if is_name == "n" or is_name == "no":
        name = input("Name: ")
    email_names[email] = name

    email = input("Email: ")

print()

for email_key in email_names:
    print("{} ({})".format(email_names[email_key], email_key))
