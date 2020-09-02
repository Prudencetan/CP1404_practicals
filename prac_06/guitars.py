from guitar import Guitar


def main():
    guitar_list = []
    name = input("Enter guitar name: ")
    while name != "":
        year = int(input("Enter production year: "))
        cost = float(input("Enter cost: "))
        add_guitar = Guitar(name, year, cost)
        guitar_list.append(add_guitar)
        print(add_guitar, "added")
        name = input("Enter guitar name: ")

    print("These are my guitars:\n")
    for i, guitar in enumerate(guitar_list):
        age = guitar.get_age()
        vintage_string = ""
        if guitar.is_vintage():
            vintage_string = "(vintage)"
        print("Guitar {}: {:>20} ({}), worth ${:10,.2f}{}".format(i + 1, guitar.name, guitar.year, guitar.cost,
                                                                  vintage_string))


if __name__ == '__main__':
    main()
