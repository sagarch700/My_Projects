from ceaser_cipher_logo import logo

# Shift the position of the input text by the shift value
def ceaser_cipher(choice, input_text, shift):
    ascii_value = 0
    output_cipher = ""
    if choice == "encode":
        for position in range(0, len(input_text)):
            ascii_value = ord(input_text[position]) + int(shift)
            output_cipher = output_cipher + chr(ascii_value)
        print(f"The encoded text is {output_cipher}")
    elif choice == "decode":
        for position in range(0, len(input_text)):
            ascii_value = ord(input_text[position]) - int(shift)
            output_cipher = output_cipher + chr(ascii_value)
        print(f"The decoded text is {output_cipher}")
    else:
        print("You have to choose either 'encode' or 'decode'")

end_game = False
print(logo)

while not end_game:

    choice = input("Type 'encode' to encrypt and 'decode' to decrypt: ").lower()
    input_text = input("Type your message: ")
    shift = input("Type your shift number: ")
    
    ceaser_cipher(choice= choice, input_text= input_text, shift= shift)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no': ").lower()

    if restart == "no":
        end_game = True
        print("Goodbye")


