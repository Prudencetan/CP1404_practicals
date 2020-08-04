min_length = 5


def main():
    password = get_password(min_length)
    while len(password) <= min_length:
        password = get_password()

    print_asterisks(password)


def print_asterisks(password):
    for i in password:
        print("*", end=' ')


def get_password(x):
    return input("Enter password of at least {} characters: ".format(x))


if __name__ == '__main__':
    main()
