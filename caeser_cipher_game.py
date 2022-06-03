alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
    'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
should_continue = True
def caeser(text, shift, direction):
    cipher_text = ""
    if direction == "decrypt":
        shift *= -1
    for char in text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = position + shift
            new_letter = alphabets[new_position]
            cipher_text += new_letter
        else:
            cipher_text += char
    print(f"\nYour {direction}ed text is: {cipher_text}")
while should_continue:
    direction = input("\nType 'encrypt' for encrpytion, 'decrypt' for decryption:\n").lower()
    text = input("\nEnter your message:\n").lower()
    shift = int(input("\nEnter the shifts you want to do:\n"))
    shift = shift % 26
    caeser(text, shift, direction)
    result = input("\nType 'yes' if you wish to continue, otherwise type 'no'\n").lower()
    if result == "no":
        should_continue = False
        print("Goodbye...!!\n")