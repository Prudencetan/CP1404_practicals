def main():
    colour_names = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7", "black": "#000000",
                    "cadetblue": "#5f9ea0", "chocolate": "#d2691e", "cornflowerblue": "#6495ed",
                    "hotpink": "#ff69b4", "indianred": "#cd5c5c", "lavender": "#e6e6fa",
                    "linen": "#faf0e6", "mintcream": "#f5fffa"}

    colour = input("Enter colour name: ").lower()
    while colour != "":
        if colour in colour_names:
            print(colour_names[colour])
        else:
            print("Invalid colour")
        colour = input("Enter colour name: ").lower()

if __name__ == '__main__':
    main()