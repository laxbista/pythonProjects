from art import logo

print(logo)

alphabet = alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                       't', 'u', 'v', 'w', 'x', 'y', 'z',
                       'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                       't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(plain_text, shiftNumber, cipher_option):
    """Encode&Decode messages based on shift amout"""
    end_text = ""
    if cipher_option == "decode":
        shiftNumber *= -1
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shiftNumber
            end_text += alphabet[new_position]
        else:
            # leave number, symbol and spaces unchanged
            end_text += char
    print(f"Your {cipher_option}d result: {end_text}")


# Continue the loop if user types yes
should_end = False
while not should_end:
    # Ask user if they want to encode or decode text
    option = input("Type 'encode' to encrypt and 'decode' to decrypt. ").lower()

    # Get user's input to encode/decode
    message = input("Type your message: ").lower()

    # Ask user for shift amount
    shift_amount = int(input("Tye the shift Number: "))

    # Shift amount shouldn't be greater than length of alphabet
    shift_amount = shift_amount % 26

    # Calling function with keyword arguments
    caesar(plain_text=message, shiftNumber=shift_amount, cipher_option=option)

    restart = input("Type 'yes' if you want to go again. or type 'no'")
    # end program if user types no
    if restart == "no":
        should_end = True
        print("Goodbye")