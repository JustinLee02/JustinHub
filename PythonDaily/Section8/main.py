alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(get_text, get_shift):
    get_text = list(get_text)

    for i in range(len(get_text)):
        get_text[i] = alphabet[(alphabet.index(get_text[i])+get_shift)%26]
    get_text = ''.join(get_text)
    print(f"The encoded text is {get_text}")

def decrypt(get_text, get_shift):
    get_text = list(get_text)

    for i in range(len(get_text)):
        get_text[i] = alphabet[(alphabet.index(get_text[i])-get_shift)]
    get_text = ''.join(get_text)
    print(f"The decoded text is {get_text}")

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

while direction == "encode" or direction == "decode":

    if direction == "encode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        encrypt(text,shift)

    elif direction == "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        decrypt(text,shift)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")