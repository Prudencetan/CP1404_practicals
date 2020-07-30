def main():
    for i in range(1, 21, 2):
        print(i, end=' ')
    print()

    for i in range(0,101,10):
        print(i, end=' ')
    print()

    for i in reversed(range(1,21)):
        print(i, end=' ')
    print()

    stars=int(input("Number of stars: "))
    for i in range(stars+1):
        print("*"* i)

if __name__ == '__main__':
    main()