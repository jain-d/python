# caesar cypher is a technique of cyphering in which we replace the letter with its third consecutive letter in the alphabets. 
def encode(message, shift=3):
    cyphered = ""
    for letter in message:
        ascii_value = ord(letter) + shift
        if ascii_value > 90 and ascii_value < 97:
            cyphered += chr((ascii_value - 91) + ord("A"))
        elif ascii_value > 120:
            cyphered += chr((ascii_value - 123) + ord("a"))
        else:
            cyphered += chr(ascii_value)
    return cyphered
        


def main():
    message = input("What is to be cyphered? ")
    print(f"cypher - {encode(message)}")

main()
