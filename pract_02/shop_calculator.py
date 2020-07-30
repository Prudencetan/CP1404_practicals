def main():
    total=0
    items=int(input("Number of items: "))
    for i in range(items):
        price_of_items=float(input("Price of item: "))
        total += price_of_items

    if total>100:
        total=total*0.9
        print("{:.2f}".format(total))
    else:
        total = "{:.2f}".format(total)
        print(total)

if __name__ == '__main__':
    main()