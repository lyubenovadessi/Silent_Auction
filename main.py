import caeser_logo, string

print(caeser_logo.logo)

alphabet = string.ascii_lowercase

def caeser(original_text, shift_amount, encode_decode):
    output_text = ""

    shift_amount = shift_amount if encode_decode == "encode" else -shift_amount

    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = (alphabet.index(letter) + shift_amount) % len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_decode}d result: {output_text}")

should_continue = True
while should_continue:
    while (direction := input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()) not in ("encode", "decode"):
        print("Wrong input")
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n")) % len(alphabet)

    caeser(text, shift, direction)
    restart = input("Type 'yes' to continue. Otherwise, type 'no': \n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye!")