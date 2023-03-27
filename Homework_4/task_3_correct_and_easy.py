import math
def encode(message,shift,list_of_letters= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z']):
    encoded_message = ""
    shift %= len(list_of_letters)
    message = message.lower()
    for char in message:
        if list_of_letters.count(char) == 0:
            encoded_message += char
            continue
        index = list_of_letters.index(char)
        index += shift
        if index > len(list_of_letters):
            index %= len(list_of_letters)
        encoded_message += list_of_letters[index]
    return encoded_message


def decode(message,shift,list_of_letters= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z']):
    encoded_message = ""
    shift %= len(list_of_letters)
    message = message.lower()
    for char in message:
        if list_of_letters.count(char) == 0:
            encoded_message += char
            continue
        index = list_of_letters.index(char)
        index -= shift
        if index < 0:
            index = math.abs(index)
        encoded_message += list_of_letters[index]
    return encoded_message


var = encode("Franek jest super",1)
var3 = encode("Franek jest super",53)
var2 = decode(var,53)
print(var)
print(var2)
print(var3)