def main():
    finished = False
    while not finished:
        try:
            numerator = int(input("Enter the numerator: "))
            denominator = int(input("Enter the denominator: "))
            fraction = numerator / denominator
            print(fraction)
            print("Finished.")
            finished = True
        except ValueError:
            print("Numerator and denominator must be valid numbers!")
        except ZeroDivisionError:
            print("Cannot divide by zero!")

if __name__ == '__main__':
    main()