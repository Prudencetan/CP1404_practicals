import random

def main():
    input_file = open("temps_input.txt",'w')
    output_file = open("temps_output.txt",'w')

    for i in range(15):
        print(random.uniform(-200.0,200.0),file=input_file)

    input_file = open("temps_input.txt",'r')
    temps_in_fahrenheit = input_file.readlines()

    for line in temps_in_fahrenheit:
        temperature = float(line)
        print(fahrenheit_to_celsius(temperature),file=output_file)
    input_file.close()
    output_file.close()


def fahrenheit_to_celsius(f):
    c = 5 / 9 * (f - 32)
    return c

def celsius_to_fahrenheit(c):
    f = c * 9.0 / 5 + 32
    return f

if __name__ == '__main__':
    main()