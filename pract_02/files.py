def main():
    #Question 1
    name_file=open("name.txt", 'w')
    name=input("Enter your name: ")
    print(name, file=name_file)
    name_file.close()

    # Question 2
    name_file=open("name.txt", 'r')
    print("Your name is", name_file.read())
    name_file.close()

    # Question 3
    numbers_file=open("numbers.txt", 'r')
    number1=int(numbers_file.readline())
    number2=int(numbers_file.readline())
    sum= number1+number2
    print(sum)
    numbers_file.close()

    # Question 4
    numbers_file = open("numbers.txt", 'r')
    number_list = numbers_file.readlines()
    total = 0
    for i in number_list:
        numbers = int(i)
        total += numbers
    print(total)
    numbers_file.close()

if __name__ == '__main__':
    main()