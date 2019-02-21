def encode():
    print("A------------------------------A")
    message = input("Write the string you want to be encrypted: ")
    encoded = ""
    for char in message:
        if char == "a" or char == "A":
            encoded += "#"
        elif char == "b" or char == "B":
            encoded += "*"
        elif char == "c" or char == "C":
            encoded += "3"
        elif char == "d" or char == "D":
            encoded += "f"
        elif char == "e" or char == "E":
            encoded += "@"
        elif char == "f" or char == "F":
            encoded += "4"
        elif char == "g" or char == "G":
            encoded += "!"
        elif char == "h" or char == "H":
            encoded += "j"
        elif char == "i" or char == "I":
            encoded += ")"
        elif char == "j" or char == "J":
            encoded += "l"
        elif char == "k" or char == "K":
            encoded += "w"
        elif char == "l" or char == "L":
            encoded += "n"
        elif char == "m" or char == "M":
            encoded += "0"
        elif char == "n" or char == "N":
            encoded += "p"
        elif char == "o" or char == "O":
            encoded += "q"
        elif char == "p" or char == "P":
            encoded += "r"
        elif char == "q" or char == "Q":
            encoded += "$"
        elif char == "r" or char == "R":
            encoded += "t"
        elif char == "s" or char == "S":
            encoded += "u"
        elif char == "t" or char == "T":
            encoded += "v"
        elif char == "u" or char == "U":
            encoded += "m"
        elif char == "v" or char == "V":
            encoded += "x"
        elif char == "w" or char == "W":
            encoded += "y"
        elif char == "x" or char == "X":
            encoded += "z"
        elif char == "y" or char == "Y":
            encoded += "a"
        elif char == "z" or char == "Z":
            encoded += "b"
        else:
            encoded += char
    print("")
    print(("+")+"-"*len(message)+("+"))
    print(encoded)
    print(("+")+"-"*len(message)+("+"))

def decode():
    print("A------------------------------A")
    melding = input("Write the string you want to be decrypted: ")
    decoded = ""
    for char in melding:
        if char == "#":
            decoded += "a"
        elif char == "*":
            decoded += "b"
        elif char == "3":
            decoded += "c"
        elif char == "f":
            decoded += "d"
        elif char == "@":
            decoded += "e"
        elif char == "4":
            decoded += "f"
        elif char == "!":
            decoded += "g"
        elif char == "j":
            decoded += "h"
        elif char == ")":
            decoded += "i"
        elif char == "l":
            decoded += "j"
        elif char == "w":
            decoded += "k"
        elif char == "n":
            decoded += "l"
        elif char == "0":
            decoded += "m"
        elif char == "p":
            decoded += "n"
        elif char == "q":
            decoded += "o"
        elif char == "r":
            decoded += "p"
        elif char == "$":
            decoded += "q"
        elif char == "t":
            decoded += "r"
        elif char == "u":
            decoded += "s"
        elif char == "v":
            decoded += "t"
        elif char == "m":
            decoded += "u"
        elif char == "x":
            decoded += "v"
        elif char == "y":
            decoded += "w"
        elif char == "z":
            decoded += "x"
        elif char == "a":
            decoded += "y"
        elif char == "b":
            decoded += "z"
        else:
            decoded += char
    print("Decoding string...")
    print("")
    print(("A")+"-"*len(melding)+("A"))
    print(decoded)
    print(("A")+"-"*len(melding)+("A"))


print ('''

       +-------------------------------------------------------------+


    _____________________.____     
    \______   \_   _____/|    |                                        
    |     ___/|    __)_  |    |                                          
    |    |    |        \ |    |___     +--Personal Encryption Language--+
    |____|   /_______  / |_______ \                                       
                     \/          \/                                    


       +-----------------------SamuelTheodore-------------------------+

       Disclaimer: this script is not case sensetive!
''')

choice = input("Do you want to (D)ecrypt or (E)ncrypt: ").upper()

if choice == "E":
    encode()

if choice == "D":
    decode()
