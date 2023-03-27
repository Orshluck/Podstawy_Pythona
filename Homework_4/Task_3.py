#Szyfr cezara
def encode(message, shift, letters_in_alphabet=26):
    encoded_message = ""
    shift %= letters_in_alphabet # So this is default for english max
    for char in message:
        print(f"{ord(char)} - {char}")
        if (is_small_letter(char) or is_capital_letter(char)): # is A to Z or a to z
            new_asci_for_Char = ord(char) + shift
            if( new_asci_for_Char > 90 and new_asci_for_Char < 97) or ( new_asci_for_Char > 122 and new_asci_for_Char < 97):
                encoded_message += chr(new_asci_for_Char)
        else:
            encoded_message += char

    return encoded_message


def is_small_letter(char):
    if ord(char) > 65 and ord(char) < 90:
        return True
    return False

def is_capital_letter(char):
    if ord(char) > 97 and ord(char) < 122:
        return True
    return False

x = encode("Franek jest super",5)
print(x)