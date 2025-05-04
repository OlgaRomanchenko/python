alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt or 'decode' to decrypt:\n").lower()
text = input('Type your message:\n').lower()
shift = int(input('Type the shift number:\n'))


def ceaser(original_text, shift_amount, decode_or_encode):
    output_text = ''

    if decode_or_encode == 'encode':
        shift_amount *= -1

    for i in original_text:
        shifted = alphabet.index(i) + shift_amount
        shifted %= len(alphabet)
        output_text += alphabet[shifted]

    print(output_text)

ceaser(text, shift, direction)