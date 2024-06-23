COLOUR_CODES = {
    "RED": "#ff0000", "GREEN": "#00ff00",
    "BLUE": "#0000ff", "YELLOW": "#ffff00",
    "CYAN": "#00ffff", "MAGENTA": "#ff00ff",
    "WHITE": "#ffffff", "BLACK": "#000000",
    "ORANGE": "#ffa500", "PURPLE": "#800080"
}

colour_name = input("Enter a colour name: ").upper()

while colour_name != "":
    print(f"The code for \"{colour_name}\" is {COLOUR_CODES.get(colour_name)}")
    colour_name = input("Enter a colour name: ").upper()
