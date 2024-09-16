import sys
# Dictionary to map alphabet and numbers to their respective braille values
ALPHABET_TO_BRAILLE = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO"}
NUMBER_TO_BRAILLE = {
    "0": ".OOO..", "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..",
    "5": "O..O..", "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO..."
}

CAPITAL = ".....O"  # Capital letter Declaration
NUMBER = ".O.OOO"   # Digit Declaration
SPACE = "......"    # Space value declartion
# Reversal of the dictionary to map braille to alphabet/numbers
BRAILLE_TO_ALPHABET ={v: k for k, v in ALPHABET_TO_BRAILLE.items()}
BRAILLE_TO_NUMBER ={v: k for k, v in NUMBER_TO_BRAILLE.items()}


# This function checks to see if values inputted are braille or english
def is_braille(text):
    return all(c in 'O.' for c in text )

# Function that converts english to braille
def english_to_braille(text):

    result = []
    is_number = False
    # Loop through the values in text and translate them to braille
    for c in text:
        if c.isupper():
            result.append(CAPITAL)
            result.append(ALPHABET_TO_BRAILLE[c.lower()])
            is_number = False
        elif c.isdigit():
            if not is_number:
                result.append(NUMBER)
                is_number = True
            result.append(NUMBER_TO_BRAILLE[c])
        elif c ==" ":
            result.append(SPACE)
            is_number = False
        else:
            result.append(ALPHABET_TO_BRAILLE[c])
            is_number = False

    return "".join(result) # return all values in list result and join them together

# This function converts braille into english
def braille_to_englsih(text):

    result = []
    is_capital = False
    is_number = False
    braille_list = [text[i:i+6] for i in range(0,len(text), 6)] # increment in values of 6 as braille characters are 6 characters long

    for c in braille_list:
        if c == CAPITAL:
            is_capital = True
            is_number = False
        elif c == NUMBER:
            is_number = True
            is_capital = False
        elif c == SPACE:
            result.append(" ")
            is_number = False
        elif is_number:
            result.append(BRAILLE_TO_NUMBER[c])
        elif is_capital:
            result.append(BRAILLE_TO_ALPHABET[c].upper())
            is_capital = False
        else:
            result.append(BRAILLE_TO_ALPHABET[c])
    return "".join(result)






# Main function for input and output
if __name__ == '__main__':

    text = " ".join(sys.argv[1:]) # To handle input from terminal


    if is_braille(text):
        print(braille_to_englsih(text))
    else:
        print(english_to_braille(texsdex34t))


