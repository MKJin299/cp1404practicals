COLOUR_CODES = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aqua": "#00ffff",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "beige": "#f5f5dc",
    "bisque": "#ffe4c4",
    "black": "#000000",
    "blanchedalmond": "#ffebcd",
    "blue": "#0000ff"
}

def main():
    print("Hexadecimal Colour Code Lookup")
    print("Enter a blank name to exit")
    while True:
        colour = input("Enter a colour name: ").strip()
        if colour == "":
            break
        print(f"The hex code for {colour} is {get_colour_code(colour)}")
    print("Thank you for using the colour code lookup program!")

def get_colour_code(colour_name):
    return COLOUR_CODES.get(colour_name.lower(), "Colour not found")

if __name__ == "__main__":
    main()