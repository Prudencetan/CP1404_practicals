def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        full_name = email.split("@")[0]
        parts = full_name.split(".")
        name = " ".join(parts).title()
        confirmation = input("Is your name {}? (Y/n) ".format(name)).upper()
        if confirmation == "N":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print("{} ({})".format(name, email))


if __name__ == '__main__':
    main()