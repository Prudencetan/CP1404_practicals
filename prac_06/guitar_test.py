from guitar import Guitar

def main():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = ("Another Guitar", 2013, )
    print(gibson.get_age())
    print(gibson.is_vintage())

if __name__ == '__main__':
    main()